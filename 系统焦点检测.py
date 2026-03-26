# coding: utf-8

import threading
import time
import ctypes
import win32gui
import logging # 导入 logging 模块

# 配置日志记录
logging.basicConfig(filename='focus.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    encoding='utf-8') # 指定UTF-8编码

# 用于存储上一次获取到的焦点窗口句柄
last_focused_handle = None

def get_mouse_position():
    """获取当前鼠标光标位置"""
    # 定义 POINT 结构体
    class POINT(ctypes.Structure):
        _fields_ = [("x", ctypes.c_long),
                    ("y", ctypes.c_long)]

    # 创建 POINT 实例
    point = POINT()
    # 调用 GetCursorPos 获取鼠标位置
    ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
    return point.x, point.y

def log_mouse_position():
    """每隔3秒记录一次鼠标位置"""
    while True:
        x, y = get_mouse_position()
        logging.info(f"鼠标位置: ({x}, {y})") # 使用 logging 记录
        time.sleep(3)

def log_focused_window():
    """记录焦点窗口的变化"""
    global last_focused_handle
    while True:
        # 获取当前前台窗口（拥有焦点的窗口）的句柄
        current_handle = win32gui.GetForegroundWindow()
        # 如果焦点窗口发生变化
        if current_handle != last_focused_handle:
            # 获取窗口标题
            window_title = win32gui.GetWindowText(current_handle)
            # 如果标题不为空，则记录
            if window_title:
                logging.info(f"焦点窗口切换到: {window_title}") # 使用 logging 记录
                last_focused_handle = current_handle
        # 短暂休眠，避免CPU占用过高
        time.sleep(0.1)

if __name__ == "__main__":
    logging.info("开始监控鼠标位置和焦点窗口...") # 使用 logging 记录
    print("开始监控鼠标位置和焦点窗口... 日志将记录在 focus.log 文件中。") # 保留控制台提示
    print("按 Ctrl+C 停止监控。")

    # 创建并启动鼠标位置监控线程
    mouse_thread = threading.Thread(target=log_mouse_position, daemon=True)
    mouse_thread.start()

    # 创建并启动焦点窗口监控线程
    focus_thread = threading.Thread(target=log_focused_window, daemon=True)
    focus_thread.start()

    try:
        # 让主线程保持运行，以便子线程可以继续工作
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("\n监控停止。") # 使用 logging 记录
        print("\n监控停止。")