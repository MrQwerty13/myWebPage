from BackEnd.Sevices.CanStorage import CanStorage
from BackEnd.Entities.Can.CanClass import CanClass


class CanSorter:
    def __init__(self, storage: CanStorage):
        self.storage = storage

    def by_name(self, reverse: bool = False) -> list[CanClass]:
        return sorted(
            self.storage.get_all(),
            key=lambda can: can.name,
            reverse=reverse
        )

    def by_volume(self, reverse: bool = False) -> list[CanClass]:
        return sorted(
            self.storage.get_all(),
            key=lambda can: can.volume.value,
            reverse=reverse
        )

    def by_taste(self, reverse: bool = False) -> list[CanClass]:
        return sorted(
            self.storage.get_all(),
            key=lambda can: can.taste.value,
            reverse=reverse
        )

    def by_assessment(self, reverse: bool = True) -> list[CanClass]:
        return sorted(
            self.storage.get_all(),
            key=lambda can: can.assessment,
            reverse=reverse
        )

    def by_author(self, reverse: bool = False) -> list[CanClass]:
        return sorted(
            self.storage.get_all(),
            key=lambda can: can.author.value,
            reverse=reverse
        )