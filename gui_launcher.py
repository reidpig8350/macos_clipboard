import tkinter as tk
from history import get_history
from pynput.keyboard import Controller

class Launcher:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # 隱藏主窗口
        self.current_window = None  # 用於追蹤當前的剪貼簿窗口

    def show(self):
        # 如果已有窗口，先關閉舊窗口
        if self.current_window is not None:
            self.current_window.destroy()

        # 創建一個新窗口
        new_window = tk.Toplevel(self.root)
        self.current_window = new_window  # 更新當前窗口的引用
        new_window.title("剪貼簿")
        
        # 設置窗口為無邊框窗口，並顯示在最上層
        new_window.attributes("-topmost", True)  # 確保窗口顯示在最上層
        new_window.overrideredirect(True)  # 移除標題欄

        # 顯示歷史記錄
        tk.Label(new_window, text="選擇要貼上的文字").pack()
        history_list = tk.Listbox(new_window, width=50, height=10)
        history_list.pack()

        # 加入歷史記錄到 Listbox
        for item in get_history():
            history_list.insert(tk.END, item)

        # 當用戶點擊某個項目時，直接執行 clipboard_append 並模擬輸入
        def on_select(event):
            selected = history_list.get(history_list.curselection())  # 獲取當前選中的文字
            new_window.clipboard_clear()
            new_window.clipboard_append(selected)
            new_window.destroy()  # 關閉窗口
            self.current_window = None  # 清除當前窗口的引用

        # 綁定 Listbox 的選擇事件
        history_list.bind("<<ListboxSelect>>", on_select)

        # 添加關閉按鈕
        def close_window():
            new_window.destroy()
            self.current_window = None  # 清除當前窗口的引用

        tk.Button(new_window, text="關閉", command=close_window).pack()

    def run(self):
        self.root.mainloop()

launcher = Launcher()
