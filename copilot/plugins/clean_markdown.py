import re
from ..rules import ActionPlugin


def looks_like_markdown(text):
    if re.search(r"^\s*#", text, re.M):
        return True
    if re.search(r"^\s*[-*]\s+", text, re.M):
        return True
    if "```" in text:
        return True
    return False


def clean_md(text):
    s = text.replace("\r\n", "\n").replace("\r", "\n")
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = re.sub(r"^[ \t]+", "", s, flags=re.M)
    s = re.sub(r"^([-*])([A-Za-z0-9])", r"\1 \2", s, flags=re.M)
    s = re.sub(r"^#+", lambda m: "#" * len(m.group(0)), s, flags=re.M)
    return s.strip()


class CleanMarkdown(ActionPlugin):
    name = "clean_markdown"

    def confidence(self, text: str) -> float:
        return 0.8 if looks_like_markdown(text) else 0.0

    def apply(self, text: str) -> str:
        return clean_md(text)