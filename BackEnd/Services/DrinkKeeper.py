from BackEnd.Services.DrinkStorage import DrinkStorage
from BackEnd.Services.DrinkSorter import DrinkSorter
from BackEnd.Entities.Drinks.DrinkClass import DrinkClass

class DrinkKeeper:
    def __init__(self, path: str):
        self.storage = DrinkStorage(path)
        self.sorter = DrinkSorter(self.storage)

    def add(self, drink: DrinkClass) -> None:
        self.storage.add(drink)

    def get_all(self, have_sorting: bool = False, sort: str = "") -> list[DrinkClass]:
        if not have_sorting:
            return self.storage.get_all()
        sort_methods = {
            "name": self.sorter.by_name,
            "brand": self.sorter.by_brand,
            "volume": self.sorter.by_volume,
            "taste": self.sorter.by_taste,
            "assessment": self.sorter.by_assessment,
            "author": self.sorter.by_author,
            "counter": self.sorter.by_counter,
        }
        return sort_methods.get(sort, self.storage.get_all)()

    def clear(self) -> None:
        self.storage.clear()

    def count(self) -> int:
        return self.storage.count()

    def delete(self, drink: DrinkClass) -> bool:
        return self.storage.delete(drink)

    def increment_counter(self, drink: DrinkClass) -> bool:
        return self.storage.increment_counter(drink)