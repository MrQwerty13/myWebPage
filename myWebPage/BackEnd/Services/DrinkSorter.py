from BackEnd.Services.DrinkStorage import DrinkStorage
from BackEnd.Entities.Drinks.DrinkClass import DrinkClass

class DrinkSorter:
    def __init__(self, storage: DrinkStorage):
        self.storage = storage

    def by_name(self, reverse: bool = False) -> list[DrinkClass]:
        return sorted(self.storage.get_all(), key=lambda d: d.name, reverse=reverse)

    def by_brand(self, reverse: bool = False) -> list[DrinkClass]:
        return sorted(self.storage.get_all(), key=lambda d: d.brand.value, reverse=reverse)

    def by_volume(self, reverse: bool = False) -> list[DrinkClass]:
        return sorted(self.storage.get_all(), key=lambda d: d.volume, reverse=reverse)

    def by_taste(self, reverse: bool = False) -> list[DrinkClass]:
        return sorted(self.storage.get_all(), key=lambda d: d.taste, reverse=reverse)

    def by_assessment(self, reverse: bool = True) -> list[DrinkClass]:
        return sorted(self.storage.get_all(), key=lambda d: d.assessment, reverse=reverse)

    def by_author(self, reverse: bool = False) -> list[DrinkClass]:
        return sorted(self.storage.get_all(), key=lambda d: d.author.value, reverse=reverse)

    def by_counter(self, reverse: bool = True) -> list[DrinkClass]:
        return sorted(self.storage.get_all(), key=lambda d: d.counter, reverse=reverse)