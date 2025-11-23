import csv
import io
import json
from ..rules import ActionPlugin


def looks_like_csv(text):
    lines = [l for l in text.splitlines() if l.strip()]
    if len(lines) < 2:
        return False
    sep_counts = [l.count(",") for l in lines[:10]]
    if max(sep_counts) == 0:
        return False
    return True


class CsvToJson(ActionPlugin):
    name = "csv_to_json"

    def confidence(self, text: str) -> float:
        return 0.9 if looks_like_csv(text) else 0.0

    def apply(self, text: str) -> str:
        reader = csv.DictReader(io.StringIO(text))
        rows = list(reader)
        return json.dumps(rows, ensure_ascii=False, indent=2)