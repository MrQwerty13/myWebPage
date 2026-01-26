def get_data():
    import json

    with open("anime.json", encoding="utf-8") as f:
        data = json.load(f)

    anime_dict = {
        genre: [
            {
                "title": item["title"],
                "description": item["description"],
                "link": item["link"]
            }
            for item in items
        ]
        for genre, items in data.items()
    }

    return anime_dict



import flask as f

app = f.Flask(__name__)

app = f.Flask(__name__)
@app.route('/')
def show_home():
    return f.render_template("home.html")
@app.route('/anime')
@app.route('/anime')
def show_anime():
    anime_dict = get_data()
    return f.render_template("anime.html", anime=anime_dict)

@app.route('/author')
def show_author():
    return f.render_template("author.html")

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()