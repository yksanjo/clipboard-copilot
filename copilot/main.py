import sys
from .clipboard import ClipboardWatcher
from .rules import RuleEngine
from .plugins import load_plugins


def run():
    plugins = load_plugins()
    engine = RuleEngine(plugins)

    def on_change(text):
        actions = engine.suggest(text)
        if not actions:
            return
        best = actions[0]
        try:
            result = best.apply(text)
        except Exception:
            return
        ClipboardWatcher.set_clipboard_text(result)
        sys.stdout.write(f"applied:{best.name}\n")
        sys.stdout.flush()

    watcher = ClipboardWatcher(on_change=on_change)
    watcher.start()