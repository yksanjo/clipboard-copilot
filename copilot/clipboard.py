import threading
import time
import tkinter as tk


class ClipboardWatcher:
    def __init__(self, on_change, interval_ms=800):
        self.on_change = on_change
        self.interval_ms = interval_ms
        self._last = None
        self._stop = threading.Event()
        self._root = tk.Tk()
        self._root.withdraw()

    def _get_text(self):
        try:
            data = self._root.clipboard_get()
            return data
        except tk.TclError:
            return None

    def start(self):
        def loop():
            while not self._stop.is_set():
                val = self._get_text()
                if val is not None and val != self._last:
                    self._last = val
                    self.on_change(val)
                time.sleep(self.interval_ms / 1000.0)

        t = threading.Thread(target=loop, daemon=True)
        t.start()
        self._root.mainloop()

    @staticmethod
    def set_clipboard_text(text):
        r = tk.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(text)
        r.update()
        r.destroy()