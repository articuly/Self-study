# coding: utf-8

import win32gui
import time
import pywintypes # 导入 pywintypes 用于异常处理

# 用于存储上一次获取到的活动窗口句柄
last_active_handle = None

def monitor_active_window():
    """监控当前活动窗口并在变化时打印日志"""
    global last_active_handle
    print("开始监控活动窗口... 按 Ctrl+C 停止。")
    try:
        while True:
            try:
                # 获取当前活动（前台）窗口的句柄
                current_handle = win32gui.GetForegroundWindow()
                # 如果活动窗口发生变化
                if current_handle != last_active_handle:
                    # 获取窗口标题
                    window_title = win32gui.GetWindowText(current_handle)
                    # 获取当前时间
                    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    # 如果标题不为空，则打印时间和标题
                    if window_title:
                        print(f"{current_time} - 活动窗口: {window_title}")
                        # 更新最后记录的句柄
                        last_active_handle = current_handle
                    else:
                        # 如果窗口标题为空，也记录下来（可能是某些特殊窗口或后台进程）
                        # print(f"{current_time} - 活动窗口句柄: {current_handle} (无标题)") # 可选：打印无标题窗口的句柄
                        last_active_handle = current_handle # 即使无标题，也更新句柄，避免重复检测同一个无标题窗口

            except pywintypes.error as e:
                # 处理获取窗口信息时可能发生的错误（例如窗口快速关闭）
                # print(f"获取窗口信息时出错: {e}")
                # 发生错误时，将 last_active_handle 设为 None，以便下次能检测到新窗口
                last_active_handle = None
                time.sleep(0.5) # 发生错误时稍作等待
                continue # 继续下一次循环

            # 短暂休眠，降低CPU占用率
            time.sleep(0.5) # 每 0.5 秒检查一次

    except KeyboardInterrupt:
        print("\n监控已停止。")

if __name__ == "__main__":
    monitor_active_window()