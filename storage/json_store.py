from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Callable, TypeVar

T = TypeVar("T")


class JsonStore:
    """Thread-safe JSON file store for list-shaped collections."""

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self._lock = threading.Lock()
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self._write([])

    def _read(self) -> list:
        with self.file_path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        if not isinstance(data, list):
            raise ValueError(f"{self.file_path} must contain a JSON array")
        return data

    def _write(self, items: list) -> None:
        with self.file_path.open("w", encoding="utf-8") as handle:
            json.dump(items, handle, indent=2, ensure_ascii=False)
            handle.write("\n")

    def all(self) -> list:
        with self._lock:
            return self._read()

    def save_all(self, items: list) -> None:
        with self._lock:
            self._write(items)

    def append(self, item: dict) -> dict:
        with self._lock:
            items = self._read()
            items.append(item)
            self._write(items)
            return item

    def find(self, predicate: Callable[[dict], bool]) -> dict | None:
        with self._lock:
            for item in self._read():
                if predicate(item):
                    return item
        return None

    def filter(self, predicate: Callable[[dict], bool]) -> list:
        with self._lock:
            return [item for item in self._read() if predicate(item)]

    def replace_where(
        self,
        predicate: Callable[[dict], bool],
        replacer: Callable[[dict], dict],
    ) -> dict | None:
        with self._lock:
            items = self._read()
            for index, item in enumerate(items):
                if predicate(item):
                    updated = replacer(item)
                    items[index] = updated
                    self._write(items)
                    return updated
        return None

    def delete_where(self, predicate: Callable[[dict], bool]) -> int:
        with self._lock:
            items = self._read()
            kept = [item for item in items if not predicate(item)]
            removed = len(items) - len(kept)
            if removed:
                self._write(kept)
            return removed
