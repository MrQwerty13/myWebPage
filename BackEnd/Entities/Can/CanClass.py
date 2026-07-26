from BackEnd.Entities.Can.Enums.CanEnumVolume import CanEnumVolume
from BackEnd.Entities.Can.Enums.CanEnumTaste import CanEnumTaste
from BackEnd.Entities.Authors.AuthorEnum import AuthorEnum


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

    def get_info(self, unit: str = "", is_value: bool = False) -> str:
        """
        Return a string representation of a selected attribute or the full info.

        :param unit:   One of 'n', 'v', 't', 'as', 'd', 'au', or empty for full info.
        :param is_value: If True, return the enum's value instead of its name
                         (only relevant for 'v', 't', and 'au').
        :return:        Formatted string.
        """
        # Full info fallback
        if not unit:
            return (
                f"=== The {self.name} ===\n"
                f"Volume: {self.volume.value} ml\n"
                f"Taste: {self.taste.value}\n"
                f"Description: {self.description}\n"
                f"Assessment: {self.assessment}/10\n"
                f"=== By {self.author.value} ==="
            )

        # Single‑attribute requests
        if unit == "n":
            return self.name

        if unit == "v":
            return f"{self.volume.value} ml" if is_value else str(self.volume)

        if unit == "t":
            return self.taste.value if is_value else str(self.taste)

        if unit == "as":
            return str(self.assessment)

        if unit == "d":
            return self.description

        if unit == "au":
            return self.author.value if is_value else str(self.author)

        # Unknown unit – return empty or raise? Here we mimic the original:
        # original returned full info for unknown unit, but that would be inconsistent.
        # The original code actually did: if unit not matching, it returned the full info.
        # However, the original had: after all ifs, it returned the full info.
        # So if unit is given but not recognised, it returns full info – that's what we keep.
        return (
            f"=== The {self.name} ===\n"
            f"Volume: {self.volume.value} ml\n"
            f"Taste: {self.taste.value}\n"
            f"Description: {self.description}\n"
            f"Assessment: {self.assessment}/10\n"
            f"=== By {self.author.value} ==="
        )