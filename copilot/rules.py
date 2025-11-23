from typing import List


class ActionPlugin:
    name: str

    def confidence(self, text: str) -> float:
        raise NotImplementedError

    def apply(self, text: str) -> str:
        raise NotImplementedError


class RuleEngine:
    def __init__(self, plugins: List[ActionPlugin]):
        self.plugins = plugins

    def suggest(self, text: str) -> List[ActionPlugin]:
        scored = []
        for p in self.plugins:
            try:
                c = p.confidence(text)
            except Exception:
                c = 0.0
            if c > 0.5:
                scored.append((c, p))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [p for _, p in scored]