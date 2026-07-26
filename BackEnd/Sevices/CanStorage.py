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

        # CanStorage.py (добавить в конец класса)

    def delete(self, can: CanClass) -> bool:
        """Удаляет указанную банку из хранилища (по совпадению всех полей)."""
        cans = self.get_all()
        initial_count = len(cans)

        # Ищем совпадение по всем полям (исключая возможные дубли)
        for i, existing in enumerate(cans):
            if (existing.name == can.name and
                    existing.volume == can.volume and
                    existing.taste == can.taste and
                    existing.assessment == can.assessment and
                    existing.description == can.description and
                    existing.author == can.author):
                del cans[i]
                break

        # Если ничего не удалили – возвращаем False
        if len(cans) == initial_count:
            return False

        # Перезаписываем файл заново
        with self.file.open("w", encoding="utf-8") as f:
            for c in cans:
                data = {
                    "name": c.name,
                    "volume": c.volume.value,
                    "taste": c.taste.value,
                    "assessment": c.assessment,
                    "description": c.description,
                    "author": c.author.value
                }
                f.write(json.dumps(data, ensure_ascii=False))
                f.write("\n\n")
        return True