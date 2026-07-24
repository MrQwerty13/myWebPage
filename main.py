# Show can example
from Entities.Can.CanClass import CanClass

from Entities.Can.Enums.CanEnumVolume import CanEnumVolume
from Entities.Can.Enums.CanEnumTaste import CanEnumTaste

from Entities.Authors.AuthorEnum import AuthorEnum



cans = {
    "Classic Small Can": CanClass(
        name="Classic Small Can",
        volume=CanEnumVolume.small,
        taste=CanEnumTaste.Classic,
        assessment=8.5,
        description="The immortal classic",
        author=AuthorEnum.Mikhail
    ).get_info(),
    "Classic Medium Can": CanClass(
        name="Classic Medium Can",
        volume=CanEnumVolume.medium,
        taste=CanEnumTaste.Classic,
        assessment=8.0,
        description="Almost like great but not best among classic",
        author=AuthorEnum.Mikhail
    ).get_info(),
    "Classic Large Can": CanClass(
        name="Classic Large Can",
        volume=CanEnumVolume.large,
        taste=CanEnumTaste.Classic,
        assessment=8.5,
        description="Best of the best for getting energy",
        author=AuthorEnum.Mikhail
    ).get_info()
}

for can in cans.values():
    print(can, end="\n\n")