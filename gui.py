import tkinter as tk
from clipboard import set_clipboard
from history import get_recent

def show_history_gui():
    root = tk.Tk()
    root.title("📋 剪貼簿歷史")
    root.geometry("400x300")

    def copy_and_close(text):
        set_clipboard(text)
        root.destroy()

    recent = get_recent()
    for idx, item in enumerate(reversed(recent)):
        btn = tk.Button(root, text=item[:50], anchor="w", justify="left",
                        command=lambda t=item: copy_and_close(t))
        btn.pack(fill="x", padx=10, pady=5)

    root.mainloop()