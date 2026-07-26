from BackEnd.Sevices.CanStorage import CanStorage
from BackEnd.Sevices.CanSorter import CanSorter # fixed typo

from BackEnd.Entities.Can.CanClass import CanClass


class TheCanKeeper:
    def __init__(self, path: str):
        self.storage = CanStorage(path)
        self.sorter = CanSorter(self.storage)

    def add(self, can: CanClass) -> None:
        self.storage.add(can)

    def get_all(
        self,
        have_sorting: bool = False,
        sort: str = ""
    ) -> list[CanClass]:

        if not have_sorting:
            return self.storage.get_all()

        sort_methods = {
            "name": self.sorter.by_name,
            "volume": self.sorter.by_volume,
            "taste": self.sorter.by_taste,
            "assessment": self.sorter.by_assessment,
            "author": self.sorter.by_author,
        }

        return sort_methods.get(sort, self.storage.get_all)()

    def clear(self) -> None:
        self.storage.clear()

    def count(self) -> int:
        return self.storage.count()