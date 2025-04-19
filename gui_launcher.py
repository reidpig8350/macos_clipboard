import tkinter as tk
from history import get_history

class Launcher:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # 隱藏主窗口

    def show(self):
        # 每次調用時創建一個新窗口
        new_window = tk.Toplevel(self.root)
        new_window.title("剪貼簿")
        
        # 顯示歷史記錄
        tk.Label(new_window, text="選擇要貼上的文字").pack()
        history_list = tk.Listbox(new_window, width=50, height=10)
        history_list.pack()

        # 加入歷史記錄到 Listbox
        for item in get_history():
            history_list.insert(tk.END, item)

        # 添加按鈕來選擇文字
        def on_select():
            selected = history_list.get(tk.ACTIVE)  # 獲取當前選中的文字
            new_window.clipboard_clear()
            new_window.clipboard_append(selected)
            new_window.destroy()

        tk.Button(new_window, text="貼上選擇的文字", command=on_select).pack()
        tk.Button(new_window, text="關閉", command=new_window.destroy).pack()

    def run(self):
        self.root.mainloop()

launcher = Launcher()
