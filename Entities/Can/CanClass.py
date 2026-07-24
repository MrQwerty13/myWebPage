from Entities.Can.Enums.CanEnumVolume import CanEnumVolume
from Entities.Can.Enums.CanEnumTaste import CanEnumTaste

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

    def get_info(self, unit: str = "", is_value: bool = False):
        if unit == "n":
            return f"{self.name}"
        if unit == "v":
            if is_value:
                return f"{self.volume.value} ml"
            return f"{self.volume}"
        if unit == "t":
            if is_value:
                return f"{self.taste.value}"
            return f"{self.taste}"
        if unit == "as":
            return f"{self.assessment}"
        if unit == "d":
            return f"{self.description}"
        if unit == "au":
            if is_value:
                return f"{self.author.value}"
            return f"{self.author}"

        return (
            f"=== The {self.name} ===\n"
            f"Volume: {self.volume.value} ml\n"
            f"Taste: {self.taste.value}\n"
            f"Description: {self.description}\n"
            f"Assessment: {self.assessment}/10\n"
            f"=== By {self.author.value} ==="
        )