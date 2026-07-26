import json
from pathlib import Path

from BackEnd.Entities.Can.CanClass import CanClass
from BackEnd.Entities.Can.Enums.CanEnumVolume import CanEnumVolume
from BackEnd.Entities.Can.Enums.CanEnumTaste import CanEnumTaste
from BackEnd.Entities.Authors.AuthorEnum import AuthorEnum


class CanStorage:
    def __init__(self, file_name: str = "cans.txt"):
        self.file = Path(file_name)
        if not self.file.exists():
            self.file.touch()

    def add(self, can: CanClass) -> None:
        """Adds a CanClass object to the file."""
        data = {
            "name": can.name,
            "volume": can.volume.value,
            "taste": can.taste.value,
            "assessment": can.assessment,
            "description": can.description,
            "author": can.author.value
        }
        with self.file.open("a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False))
            f.write("\n\n")

    def get_all(self) -> list[CanClass]:
        """Returns all CanClass objects from the file."""
        cans = []
        with self.file.open("r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                data = json.loads(line)
                cans.append(
                    CanClass(
                        name=data["name"],
                        volume=CanEnumVolume(data["volume"]),
                        taste=CanEnumTaste(data["taste"]),
                        assessment=data["assessment"],
                        description=data["description"],
                        author=AuthorEnum(data["author"])
                    )
                )
        return cans

    def clear(self) -> None:
        """Removes all stored cans (truncates the file)."""
        # Simplified: just write empty string using the file object
        self.file.write_text("", encoding="utf-8")

    def count(self) -> int:
        """Returns the number of stored cans."""
        return len(self.get_all())