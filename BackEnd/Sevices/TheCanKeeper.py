from CanStorage import CanStorage
from CanSorter import CanSorter

from BackEnd.Entities.Can.CanClass import CanClass



class TheCanKeeper:
    def __init__(self, path: str):
        self.path = path
        self.storage = CanStorage(path)
        self.sorter = CanSorter(self.storage)

    def add(self, can) -> None:
        self.storage.add(can)

    def get_all(self, have_sorting: bool = False, sort: str = "") -> list[CanClass]:
        if have_sorting:
            if sort == "name":
                return self.sorter.by_name()
            if sort == "volume":
                return self.sorter.by_volume()
            if sort == "taste":
                return self.sorter.by_taste()
            if sort == "assessment":
                return self.sorter.by_assessment()
            if sort == "author":
                return self.sorter.by_author()
        return self.storage.get_all()

    def clear(self) -> None:
        self.storage.clear()

    def count(self) -> int:
        return self.storage.count()