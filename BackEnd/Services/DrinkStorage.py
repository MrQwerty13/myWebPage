import json
from pathlib import Path
from BackEnd.Entities.Drinks.DrinkClass import DrinkClass
from BackEnd.Entities.Drinks.BrandEnum import BrandEnum
from BackEnd.Entities.Authors.AuthorEnum import AuthorEnum

class DrinkStorage:
    def __init__(self, file_name: str = "drinks.txt"):
        self.file = Path(file_name)
        if not self.file.exists():
            self.file.touch()

    def add(self, drink: DrinkClass) -> None:
        data = {
            "name": drink.name,
            "brand": drink.brand.value,
            "volume": drink.volume,
            "taste": drink.taste,
            "assessment": drink.assessment,
            "description": drink.description,
            "author": drink.author.value,
            "counter": drink.counter
        }
        with self.file.open("a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False))
            f.write("\n\n")

    def get_all(self) -> list[DrinkClass]:
        drinks = []
        with self.file.open("r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                data = json.loads(line)
                drinks.append(
                    DrinkClass(
                        name=data["name"],
                        brand=BrandEnum(data["brand"]),
                        volume=float(data["volume"]),
                        taste=data["taste"],
                        assessment=float(data["assessment"]),
                        description=data["description"],
                        author=AuthorEnum(data["author"]),
                        counter=int(data.get("counter", 0))
                    )
                )
        return drinks

    def delete(self, drink: DrinkClass) -> bool:
        drinks = self.get_all()
        initial_count = len(drinks)
        for i, d in enumerate(drinks):
            if (d.name == drink.name and
                d.brand == drink.brand and
                d.volume == drink.volume and
                d.taste == drink.taste and
                d.assessment == drink.assessment and
                d.description == drink.description and
                d.author == drink.author):
                del drinks[i]
                break
        if len(drinks) == initial_count:
            return False
        self._save_all(drinks)
        return True

    def increment_counter(self, drink: DrinkClass) -> bool:
        drinks = self.get_all()
        for d in drinks:
            if (d.name == drink.name and
                d.brand == drink.brand and
                d.volume == drink.volume and
                d.taste == drink.taste and
                d.assessment == drink.assessment and
                d.description == drink.description and
                d.author == drink.author):
                d.increment_counter()
                self._save_all(drinks)
                return True
        return False

    def _save_all(self, drinks: list[DrinkClass]) -> None:
        with self.file.open("w", encoding="utf-8") as f:
            for d in drinks:
                data = {
                    "name": d.name,
                    "brand": d.brand.value,
                    "volume": d.volume,
                    "taste": d.taste,
                    "assessment": d.assessment,
                    "description": d.description,
                    "author": d.author.value,
                    "counter": d.counter
                }
                f.write(json.dumps(data, ensure_ascii=False))
                f.write("\n\n")

    def clear(self) -> None:
        self.file.write_text("", encoding="utf-8")

    def count(self) -> int:
        return len(self.get_all())