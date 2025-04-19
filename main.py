import time
import threading
from clipboard import get_clipboard
from history import add_to_history
from pynput import keyboard
from gui_launcher import launcher

def clipboard_monitor():
    last = ""
    while True:
        current = get_clipboard()
        if current != last:
            add_to_history(current)
            last = current
        time.sleep(1)

def start_hotkey_listener():
    def on_activate():
        print("🚀 Ctrl + V 被觸發！")
        launcher.root.after(0, launcher.show)  # 確保在主循環內執行

    def for_canonical(f):
        return lambda k: f(listener.canonical(k))

    hotkey = keyboard.HotKey(
        keyboard.HotKey.parse('<ctrl>+v'),
        on_activate
    )

    with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)
    ) as listener:
        listener.join()

if __name__ == "__main__":
    threading.Thread(target=clipboard_monitor, daemon=True).start()
    threading.Thread(target=start_hotkey_listener, daemon=True).start()
    launcher.run()  # 進入 tkinter 主循環
