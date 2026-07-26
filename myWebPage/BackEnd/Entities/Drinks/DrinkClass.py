from BackEnd.Entities.Authors.AuthorEnum import AuthorEnum
from BackEnd.Entities.Drinks.BrandEnum import BrandEnum

class DrinkClass:
    def __init__(self, name: str, brand: BrandEnum, volume: float, taste: str,
                 assessment: float, description: str, author: AuthorEnum, counter: int = 0):
        self.name = name
        self.brand = brand
        self.volume = volume
        self.taste = taste
        self.assessment = assessment
        self.description = description
        self.author = author
        self.counter = counter

    def increment_counter(self):
        self.counter += 1

    def get_info(self, unit: str = "", is_value: bool = False):
        if unit == "n":
            return self.name
        if unit == "v":
            return str(self.volume)
        if unit == "t":
            return self.taste
        if unit == "as":
            return str(self.assessment)
        if unit == "d":
            return self.description
        if unit == "au":
            if is_value:
                return self.author.value
            return self.author
        if unit == "br":
            if is_value:
                return self.brand.value
            return self.brand
        return (
            f"=== {self.name} ===\n"
            f"Brand: {self.brand.value}\n"
            f"Volume: {self.volume} L\n"
            f"Taste: {self.taste}\n"
            f"Description: {self.description}\n"
            f"Assessment: {self.assessment}/10\n"
            f"Counter: {self.counter}\n"
            f"=== By {self.author.value} ==="
        )