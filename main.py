from collections import defaultdict
from flask import Flask, render_template

from BackEnd.Sevices.TheCanKeeper import TheCanKeeper

from BackEnd.Entities.Can.CanClass import CanClass
from BackEnd.Entities.Can.Enums.CanEnumVolume import CanEnumVolume
from BackEnd.Entities.Can.Enums.CanEnumTaste import CanEnumTaste

from BackEnd.Entities.Authors.AuthorEnum import AuthorEnum

from BackEnd.Files.consts import *

app = Flask(__name__)

keeper = TheCanKeeper(FILE_PATH)


@app.route("/rb")
def rb_cans():
    cans = keeper.get_all()

    groups = defaultdict(list)

    # Group by taste
    for can in cans:
        groups[can.taste.value].append(can)

    # Sort groups alphabetically by taste
    groups = dict(sorted(groups.items()))

    # Sort cans inside each group by assessment (highest first)
    for taste in groups:
        groups[taste].sort(
            key=lambda can: can.assessment,
            reverse=True
        )

    return render_template("red_bull_cans.html", groups=groups)

from flask import request, redirect

@app.route("/add", methods=["POST"])
def add_can():

    can = CanClass(
        name=request.form["name"],
        volume=CanEnumVolume(float(request.form["volume"])),
        taste=CanEnumTaste(request.form["taste"]),
        assessment=float(request.form["assessment"]),
        description=request.form["description"],
        author=AuthorEnum(request.form["author"])
    )

    keeper.add(can)

    return redirect("/rb")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6767, debug=True)


