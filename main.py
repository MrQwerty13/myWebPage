from collections import defaultdict
from flask import Flask, render_template, request, redirect, url_for

from BackEnd.Services.DrinkKeeper import DrinkKeeper
from BackEnd.Entities.Drinks.DrinkClass import DrinkClass
from BackEnd.Entities.Drinks.BrandEnum import BrandEnum
from BackEnd.Entities.Authors.AuthorEnum import AuthorEnum
from BackEnd.Files.consts import MAC_FILE_PATH

app = Flask(__name__)
keeper = DrinkKeeper(MAC_FILE_PATH)

# Volumes and tastes by brand (for the add form)
BRAND_VOLUMES = {
    BrandEnum.RED_BULL: [0.25, 0.355, 0.473],
    BrandEnum.MONSTER: [0.5],
    BrandEnum.MILKY: [0.33],
}

BRAND_TASTES = {
    BrandEnum.RED_BULL: [
        "Classic", "Sugar Free", "Peach Edition(White Peach)",
        "Red Edition(Watermelon)", "Blue Edition(Blueberry)",
        "Sea Blue Edition(Irgi)", "Tropical Edition(Tropical Fruits)",
        "Summer Edition(Lime Sudachi)",
    ],
    BrandEnum.MONSTER: ["Classic", "White Peach"],
    BrandEnum.MILKY: ["Classic", "Strawberry", "Pear", "Peach", "Grape"],
}

brand_data = {
    "volumes": {b.value: BRAND_VOLUMES[b] for b in BrandEnum},
    "tastes": {b.value: BRAND_TASTES[b] for b in BrandEnum},
}

# Author info for the authors page
AUTHOR_INFO = {
    "Diana": {
        "role": "Co-founder & Taste Expert",
        "emoji": "🌸",
        "color": "#e91e63",
        "bio_en": "Diana is the heart of Drink Tracker. She discovers new limited editions and rates them with surgical precision. Her favourite is anything peach-flavoured.",
        "bio_ru": "Диана — душа Drink Tracker. Она находит новые лимитированные выпуски и оценивает их с хирургической точностью. Её фаворит — всё со вкусом персика.",
        "favorite": "Red Bull Peach Edition",
    },
    "Mikhail": {
        "role": "Founder & Full-stack Developer",
        "emoji": "⚡",
        "color": "#2196f3",
        "bio_en": "Mikhail created Drink Tracker to never forget which energy drink he already tried. He loves clean code, dark themes and strong coffee (or Monster).",
        "bio_ru": "Михаил создал Drink Tracker, чтобы никогда не забывать, какой энергетик уже пробовал. Любит чистый код, тёмные темы и крепкий кофе (или Monster).",
        "favorite": "Monster Classic",
    },
    "Hamid": {
        "role": "Community Manager & Reviewer",
        "emoji": "🔥",
        "color": "#ff9800",
        "bio_en": "Hamid brings the community vibe. He writes the funniest descriptions and always finds the rarest cans. Currently hunting for every Milky’s flavour.",
        "bio_ru": "Хамид создаёт атмосферу сообщества. Он пишет самые смешные описания и всегда находит самые редкие банки. Сейчас охотится за всеми вкусами Milky’s.",
        "favorite": "Milky's Grape",
    },
}


def _build_groups(drinks, group_by: str):
    """Group drinks by author or brand and sort inside groups by assessment desc."""
    groups = defaultdict(list)
    for d in drinks:
        key = d.author.value if group_by == "author" else d.brand.value
        groups[key].append(d)

    groups = dict(sorted(groups.items()))

    for key in groups:
        groups[key].sort(key=lambda d: d.assessment, reverse=True)

    return groups


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/authors")
def authors_view():
    authors = [a for a in AuthorEnum if a.value != "Guest"]
    return render_template(
        "authors.html",
        authors=authors,
        author_info=AUTHOR_INFO,
    )


@app.route("/drinks")
def drinks_view():
    sort = request.args.get("sort", "author")
    valid_sorts = {"author", "brand", "rating", "popularity", "name"}
    if sort not in valid_sorts:
        sort = "author"

    drinks = keeper.get_all()

    if sort in ("author", "brand"):
        groups = _build_groups(drinks, group_by=sort)
        flat_list = None
    else:
        groups = None
        if sort == "rating":
            flat_list = sorted(drinks, key=lambda d: d.assessment, reverse=True)
        elif sort == "popularity":
            flat_list = sorted(drinks, key=lambda d: d.counter, reverse=True)
        else:
            flat_list = sorted(drinks, key=lambda d: d.name.lower())

    return render_template(
        "drinks.html",
        groups=groups,
        flat_list=flat_list,
        current_sort=sort,
        brands=BrandEnum,
        authors=AuthorEnum,
        brand_data=brand_data,
    )


@app.route("/add", methods=["POST"])
def add_drink():
    brand = BrandEnum(request.form["brand"])
    drink = DrinkClass(
        name=request.form["name"].strip(),
        brand=brand,
        volume=float(request.form["volume"]),
        taste=request.form["taste"],
        assessment=float(request.form["assessment"]),
        description=request.form.get("description", "").strip(),
        author=AuthorEnum(request.form["author"]),
    )
    keeper.add(drink)
    return redirect(url_for("drinks_view", sort=request.form.get("return_sort", "author")))


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
        author=AuthorEnum(request.form["author"]),
    )
    keeper.delete(drink)
    return redirect(url_for("drinks_view", sort=request.form.get("return_sort", "author")))


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
        author=AuthorEnum(request.form["author"]),
    )
    keeper.increment_counter(drink)
    return redirect(url_for("drinks_view", sort=request.form.get("return_sort", "author")))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)
