from collections import defaultdict
from flask import Flask, render_template, request, redirect

from BackEnd.Services.DrinkKeeper import DrinkKeeper
from BackEnd.Entities.Drinks.DrinkClass import DrinkClass
from BackEnd.Entities.Drinks.BrandEnum import BrandEnum
from BackEnd.Entities.Authors.AuthorEnum import AuthorEnum
from BackEnd.Files.consts import FILE_PATH

app = Flask(__name__)
keeper = DrinkKeeper(FILE_PATH)

# Данные для формы (объёмы и вкусы по брендам)
BRAND_VOLUMES = {
    BrandEnum.RED_BULL: [0.25, 0.355, 0.473],
    BrandEnum.MONSTER: [0.5],
    BrandEnum.MILKY: [0.33]
}

BRAND_TASTES = {
    BrandEnum.RED_BULL: [
        "Classic", "Sugar Free", "Peach Edition(White Peach)",
        "Red Edition(Watermelon)", "Blue Edition(Blueberry)",
        "Sea Blue Edition(Irgi)", "Tropical Edition(Tropical Fruits)",
        "Summer Edition(Lime Sudachi)"
    ],
    BrandEnum.MONSTER: ["Classic", "White Peach"],
    BrandEnum.MILKY: ["Classic", "Strawberry", "Pear", "Peach", "Grape"]
}

# Преобразуем для передачи в шаблон (JSON)
brand_data = {
    "volumes": {b.value: BRAND_VOLUMES[b] for b in BrandEnum},
    "tastes": {b.value: BRAND_TASTES[b] for b in BrandEnum}
}

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/drinks")
def drinks_view():
    drinks = keeper.get_all()
    groups = defaultdict(list)
    for d in drinks:
        groups[d.brand.value].append(d)
    groups = dict(sorted(groups.items()))
    for brand in groups:
        groups[brand].sort(key=lambda d: d.assessment, reverse=True)

    return render_template(
        "drinks.html",
        groups=groups,
        brands=BrandEnum,
        authors=AuthorEnum,
        brand_data=brand_data
    )

@app.route("/add", methods=["POST"])
def add_drink():
    brand = BrandEnum(request.form["brand"])
    drink = DrinkClass(
        name=request.form["name"],
        brand=brand,
        volume=float(request.form["volume"]),
        taste=request.form["taste"],
        assessment=float(request.form["assessment"]),
        description=request.form["description"],
        author=AuthorEnum(request.form["author"])
    )
    keeper.add(drink)
    return redirect("/drinks")

@app.route("/delete", methods=["POST"])
def delete_drink():
    brand = BrandEnum(request.form["brand"])
    drink = DrinkClass(
        name=request.form["name"],
        brand=brand,
        volume=float(request.form["volume"]),
        taste=request.form["taste"],
        assessment=float(request.form["assessment"]),
        description=request.form["description"],
        author=AuthorEnum(request.form["author"])
    )
    keeper.delete(drink)
    return redirect("/drinks")

@app.route("/increment", methods=["POST"])
def increment_drink():
    brand = BrandEnum(request.form["brand"])
    drink = DrinkClass(
        name=request.form["name"],
        brand=brand,
        volume=float(request.form["volume"]),
        taste=request.form["taste"],
        assessment=float(request.form["assessment"]),
        description=request.form["description"],
        author=AuthorEnum(request.form["author"])
    )
    keeper.increment_counter(drink)
    return redirect("/drinks")

if __name__ == "__main__":
    app.run(debug=True)