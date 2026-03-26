# coding: utf-8

import win32gui
import win32con
import win32api
import time
import random
import pywintypes
import ctypes
import re # 导入正则表达式模块

target_window_pattern = r'^remote_desktop(?:\s\(\d+\))? - int-ecert\.ha\.org\.hk:443 - 远程桌面连接$' # 目标窗口标题模式 (正则表达式)
# 交互间隔时间（秒）
interval_seconds = 270
# 模拟动作次数
num_actions = 3
# 模拟动作总时长（秒）
action_duration = 0.6
# 切换回原窗口后的等待时间（秒）
post_action_wait = 0.6

def get_mouse_position():
    """获取当前鼠标光标位置"""
    # 使用 win32api 获取鼠标位置
    return win32api.GetCursorPos()

def find_target_window_by_pattern(pattern):
    """根据正则表达式模式查找第一个匹配的窗口句柄"""
    target_handle = None
    target_title = ""

    def callback(hwnd, _):
        nonlocal target_handle, target_title
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            window_text = win32gui.GetWindowText(hwnd)
            if window_text and re.match(pattern, window_text):
                target_handle = hwnd
                target_title = window_text
                return False # 停止枚举
        return True # 继续枚举

    win32gui.EnumWindows(callback, None)
    return target_handle, target_title

def interact_with_target_window():
    """执行与目标窗口交互的完整流程"""
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - 开始执行交互流程...")

    try:
        # 1. 保存当前状态
        original_handle = win32gui.GetForegroundWindow()
        if original_handle:
            original_title = win32gui.GetWindowText(original_handle)
            print(f"    - 当前活动窗口: '{original_title}' (句柄: {original_handle})")
        else:
            print("    - 未能获取当前活动窗口句柄。")
        original_pos = get_mouse_position()
        print(f"    - 当前鼠标位置: {original_pos}")

        # 2. 查找目标窗口 (使用正则表达式)
        target_handle, found_title = find_target_window_by_pattern(target_window_pattern)
        if not target_handle:
            print(f"    - 未找到匹配模式 '{target_window_pattern}' 的目标窗口")
            return False # 未找到窗口，交互失败
        print(f"    - 找到目标窗口: '{found_title}' (句柄: {target_handle})")

        # 检查目标窗口是否最大化且为当前活动窗口
        try:
            placement = win32gui.GetWindowPlacement(target_handle)
            is_maximized = placement[1] == win32con.SW_SHOWMAXIMIZED
            # 检查目标窗口句柄是否等于 *当前实时* 的前台窗口句柄
            current_foreground_handle = win32gui.GetForegroundWindow()
            is_foreground = target_handle == current_foreground_handle

            # 诊断打印
            print(f"    - 诊断信息: placement[1]={placement[1]} (期望 SW_SHOWMAXIMIZED={win32con.SW_SHOWMAXIMIZED}), is_maximized={is_maximized}")
            print(f"    - 诊断信息: target_handle={target_handle}, current_foreground_handle={current_foreground_handle}, is_foreground={is_foreground}")

            if is_maximized and is_foreground:
                print(f"    - [条件满足] 目标窗口 '{found_title}' 已最大化且为当前活动窗口，跳过本次交互。")
                # 无需恢复鼠标位置，因为没有进行窗口切换和模拟点击
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - 交互流程跳过。")
                return True # 跳过交互，视为成功完成（避免短时间重试）
            else:
                print("    - [条件不满足] 目标窗口未同时处于最大化和前台状态，继续执行交互。")

        except pywintypes.error as e:
            if e.winerror == 1400: # 无效窗口句柄
                print(f"    - 检查窗口状态时出错: {e} (窗口可能已关闭)")
                return False
            else:
                print(f"    - 检查窗口状态时发生 win32 错误: {e}")
                return False
        except Exception as e:
            print(f"    - 检查窗口状态时发生未知错误: {e}")
            return False

        # 获取目标窗口大小 (移到检查条件之前，因为判断需要用到)
        try:
            left, top, right, bot = win32gui.GetWindowRect(target_handle)
            width = right - left
            height = bot - top
            if width <= 0 or height <= 0:
                print(f"    - 错误: 获取到的窗口尺寸无效 ({width}x{height})，可能窗口已关闭或隐藏。")
                # 如果无法获取有效尺寸，可能无法进行后续判断，选择继续交互或返回失败
                # 这里我们选择继续，让后续的 SetForegroundWindow 等尝试
                # return False
            else:
                print(f"    - 目标窗口位置和大小: 左={left}, 上={top}, 右={right}, 下={bot} (宽={width}, 高={height})")
        except pywintypes.error as e:
            if e.winerror == 1400: # 无效窗口句柄
                print(f"    - 获取窗口矩形时出错: {e} (窗口可能已关闭)")
                return False # 获取尺寸失败，直接返回
            else:
                print(f"    - 获取窗口矩形时发生 win32 错误: {e}")
                return False # 其他错误也返回
        except Exception as e:
            print(f"    - 获取窗口矩形时发生未知错误: {e}")
            return False

        # 重新检查条件：目标窗口是前台，并且 (最大化 或 尺寸满足条件)
        try:
            placement = win32gui.GetWindowPlacement(target_handle)
            is_maximized = placement[1] == win32con.SW_SHOWMAXIMIZED
            current_foreground_handle = win32gui.GetForegroundWindow()
            is_foreground = target_handle == current_foreground_handle
            # 增加尺寸判断逻辑
            is_large_enough = width > 2100 and height > 1200

            # 诊断打印更新
            print(f"    - 诊断信息: placement[1]={placement[1]} (期望 SW_SHOWMAXIMIZED={win32con.SW_SHOWMAXIMIZED}), is_maximized={is_maximized}")
            print(f"    - 诊断信息: target_handle={target_handle}, current_foreground_handle={current_foreground_handle}, is_foreground={is_foreground}")
            print(f"    - 诊断信息: width={width}, height={height}, is_large_enough={is_large_enough}")

            if is_foreground and (is_maximized or is_large_enough):
                skip_reason = "已最大化" if is_maximized else f"尺寸满足({width}x{height} > 2100x1200)"
                print(f"    - [条件满足] 目标窗口 '{found_title}' 为当前活动窗口且{skip_reason}，跳过本次交互。")
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - 交互流程跳过。")
                return True # 跳过交互
            else:
                print("    - [条件不满足] 目标窗口不满足跳过条件，继续执行交互。")

        except pywintypes.error as e:
            # 此处的错误处理保持不变
            if e.winerror == 1400: print(f"    - 再次检查窗口状态时出错: {e} (窗口可能已关闭)"); return False
            else: print(f"    - 再次检查窗口状态时发生 win32 错误: {e}"); return False
        except Exception as e:
            print(f"    - 再次检查窗口状态时发生未知错误: {e}"); return False

        # 3. 切换到目标窗口并确保其可见 (如果未跳过)
        # 注意：下面的代码依赖 placement 变量，它在上面的 try 块中被赋值
        try:
            # placement 变量已在上面获取
            # placement = win32gui.GetWindowPlacement(
            if placement[1] == win32con.SW_SHOWMINIMIZED:
                print("    - 目标窗口已最小化，正在恢复...")
                win32gui.ShowWindow(target_handle, win32con.SW_RESTORE)
                time.sleep(0.5) # 等待窗口恢复
            elif placement[1] == win32con.SW_SHOWMAXIMIZED:
                print("    - 目标窗口已最大化，正在恢复到普通窗口状态...")
                win32gui.ShowWindow(target_handle, win32con.SW_RESTORE)
                time.sleep(0.5) # 等待窗口恢复

            # 尝试将窗口带到前台
            win32gui.SetForegroundWindow(target_handle)
            time.sleep(0.5) # 等待窗口切换

            # 再次确认前台窗口是否为目标窗口
            if win32gui.GetForegroundWindow() != target_handle:
                # 有时SetForegroundWindow权限不足，尝试用alt+tab的方式（更hacky）
                try:
                    # 需要pywinauto库: pip install pywinauto
                    from pywinauto import Desktop
                    app = Desktop(backend="uia").window(handle=target_handle)
                    app.set_focus()
                    print("    - 使用 pywinauto 尝试激活窗口")
                    time.sleep(0.5)
                    if win32gui.GetForegroundWindow() != target_handle:
                        print("    - 警告: 切换到目标窗口失败，可能需要管理员权限或检查窗口状态。")
                        # return False # 如果切换失败，可以选择退出
                except ImportError:
                    print("    - 警告: 切换窗口失败，建议安装 pywinauto 以增强切换能力 (pip install pywinauto)")
                    # return False

        except pywintypes.error as e:
            print(f"    - 操作目标窗口时出错: {e}")
            return False # 操作窗口失败
        except Exception as e:
            print(f"    - 切换/恢复目标窗口时未知异常: {e}")
            return False

        try:
            left, top, right, bot = win32gui.GetWindowRect(target_handle)
            width = right - left
            height = bot - top
            if width <= 0 or height <= 0:
                print(f"    - 错误: 获取到的窗口尺寸无效 ({width}x{height})，可能窗口已关闭或隐藏。")
                return False
            print(f"    - 目标窗口位置和大小: 左={left}, 上={top}, 右={right}, 下={bot} (宽={width}, 高={height})")
        except pywintypes.error as e:
                print(f"    - 获取窗口矩形时出错: {e} (窗口可能已关闭)")
                return False

        # 5. 在目标窗口内模拟鼠标动作
        print(f"    - 在目标窗口内模拟 {num_actions} 次鼠标移动和点击 (总计 {action_duration} 秒)...")
        start_time = time.time()
        action_delay = action_duration / num_actions # 每个动作的平均时间

        for i in range(num_actions):
            action_start_time = time.time()
            # 在窗口客户区内生成随机坐标 (稍微缩小范围避免点到边框)
            padding = 10 # 边距
            if width > padding*2 and height > padding*2 : # 确保窗口足够大
                rand_x = random.randint(left + padding, right - padding)
                rand_y = random.randint(top + padding, bot - padding)
            else: # 窗口太小，就在中心点附近
                 rand_x = left + width // 2
                 rand_y = top + height // 2

            print(f"        - 动作 {i+1}: 移动到 ({rand_x}, {rand_y}) 并点击")
            # 移动鼠标
            win32api.SetCursorPos((rand_x, rand_y))
            time.sleep(0.05) # 短暂暂停确保移动完成
            # 模拟鼠标左键按下和抬起
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, rand_x, rand_y, 0, 0)
            time.sleep(0.05) # 按下和抬起之间短暂延迟
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, rand_x, rand_y, 0, 0)

            # 控制动作时间
            elapsed_time = time.time() - action_start_time
            sleep_time = max(0, action_delay - elapsed_time)
            time.sleep(sleep_time)

        total_elapsed= time.time() - start_time
        print(f"    - {num_actions} 次动作完成，耗时: {total_elapsed:.2f} 秒")

        # 6. 等待指定时间
        print(f"    - 等待 {post_action_wait} 秒...")
        time.sleep(post_action_wait)

        # 7. 最小化目标窗口
        # print(f"    - 最小化目标窗口: '{found_title}'")
        # try:
        #     win32gui.ShowWindow(target_handle, win32con.SW_MINIMIZE)
        #     time.sleep(0.5) # 等待窗口最小化
        # except pywintypes.error as e:
        #     # 如果此时窗口已关闭，忽略错误
        #     if e.winerror == 1400: # 无效窗口句柄
        #         print(f"    - 警告: 尝试最小化时目标窗口句柄失效 (窗口可能已关闭): {e}")
        #     else:
        #         print(f"    - 最小化目标窗口时出错: {e}")
        # except Exception as e:
        #     print(f"    - 最小化目标窗口时未知异常: {e}")

        # 8. 切换回原来的窗口
        if original_handle and original_handle != target_handle:
            print(f"    - 切换回原窗口: '{original_title}' (句柄: {original_handle})")
            try:
                win32gui.SetForegroundWindow(original_handle)
                time.sleep(0.5) # 等待切换完成
                # 再次尝试pywinauto
                if win32gui.GetForegroundWindow() != original_handle:
                        try:
                            from pywinauto import Desktop
                            app = Desktop(backend="uia").window(handle=original_handle)
                            app.set_focus()
                            print("    - 使用 pywinauto 尝试切换回原窗口")
                            time.sleep(0.5)
                            if win32gui.GetForegroundWindow() != original_handle:
                                print("    - 警告: 切换回原窗口失败。")
                        except ImportError:
                            print("    - 警告: 切换回原窗口失败，建议安装 pywinauto (pip install pywinauto)")

            except pywintypes.error as e:
                print(f"    - 切换回原窗口时出错: {e}")
            except Exception as e:
                print(f"    - 切换回原窗口时未知异常: {e}")
        elif original_handle == target_handle:
            print("    - 无需切换，原窗口就是目标窗口。")
        else:
            print("    - 没有有效的原窗口句柄可切换。")

        # 9. 恢复鼠标位置
        print(f"    - 恢复鼠标位置到: {original_pos}")
        win32api.SetCursorPos(original_pos)

        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - 交互流程执行完毕。")
        return True # 交互成功

    except pywintypes.error as e:
        # 捕捉窗口操作过程中可能出现的错误 (例如目标窗口被关闭)
        if e.winerror == 1400: # 无效窗口句柄
            print(f"    - 错误：操作过程中窗口句柄失效 (窗口可能已关闭): {e}")
        else:
            print(f"    - 执行交互时发生win32错误: {e}")
        return False # 交互失败
    except Exception as e:
        print(f"    - 执行交互时发生未知错误: {e}")
        import traceback
        traceback.print_exc() # 打印详细错误堆栈
        return False # 交互失败

if __name__ == "__main__":
    print("脚本启动，将每隔 {:.1f} 分钟尝试与匹配模式 '{}' 的窗口交互。".format(interval_seconds / 60, target_window_pattern))
    print("按 Ctrl+C 停止脚本。")

    try:
        while True:
            success = interact_with_target_window()
            # print('is_success', success)
            wait_time = interval_seconds
            if not success:
                print("    - 本次交互未完全成功，将在 1 分钟后重试。")
                wait_time = 60 # 如果失败，缩短等待时间为1分钟

            print(f"下一次交互将在 {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + wait_time))} 进行。 ({wait_time/60:.1f} 分钟后)")
            time.sleep(wait_time)

    except KeyboardInterrupt:
        print("\n脚本已由用户手动停止。")
    except Exception as e:
        print(f"\n脚本因意外错误停止: {e}")
        import traceback
        traceback.print_exc()