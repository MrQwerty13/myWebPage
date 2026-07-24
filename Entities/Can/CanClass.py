from Enums.CanEnumVolume import CanEnumVolume
from Enums.CanEnumTaste import CanEnumTaste

from Entities.Authors.AuthorEnum import AuthorEnum



class CanClass:
    def __init__(
            self,
            name: str = "Example Can",
            volume: CanEnumVolume = CanEnumVolume.small,
            taste: CanEnumTaste = CanEnumTaste.Classic,
            assessment: float = 8.5,
            description: str = "The classic but boring",
            author: AuthorEnum = AuthorEnum.Mikhail
    ) -> None:
        self.name = name
        self.volume = volume
        self.taste = taste
        self.assessment = assessment
        self.description = description
        self.author = author

    def get_info(self) -> str:
        return (
            f"=== Name: {self.name} ===\n"
            f"Volume: {self.volume.value} ml\n"
            f"Taste: {self.taste.value}\n"
            f"Description: {self.description}\n"
            f"Assessment: {self.assessment}/10\n"
            f"=== By {self.author.value} ===\n"
        )