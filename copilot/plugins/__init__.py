import importlib
import pkgutil


def load_plugins():
    plugins = []
    for m in pkgutil.iter_modules(__path__):
        if m.name.startswith("_"):
            continue
        mod = importlib.import_module(f"{__name__}.{m.name}")
        for attr in dir(mod):
            obj = getattr(mod, attr)
            if hasattr(obj, "apply") and hasattr(obj, "confidence") and hasattr(obj, "name"):
                try:
                    inst = obj()
                    plugins.append(inst)
                except Exception:
                    pass
    return plugins