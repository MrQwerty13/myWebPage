import flask as f

app = f.Flask(__name__)


app = f.Flask(__name__)

@app.route('/')
def show_home():
    return f.render_template("home.html")


@app.route('/anime')
def show_anime():
    fileOpening = {"file": "anime.txt", "mode": "r+"}
    all_in_file = [t for t in open(fileOpening['file'], fileOpening["mode"]).readlines()]
    anime = {}
    for unit in all_in_file:
        current_type: str
        if ":\n" in unit:
            current_type = unit[:unit.find(":\n")]
            anime[current_type] = []
        if not (":\n" in unit):
            unit = ((unit.replace("\n", "")).replace('   -', ''))[1:]
            anime[current_type].append(unit)
    return f.render_template("anime.html", anime=anime)

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()