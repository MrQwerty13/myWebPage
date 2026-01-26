def get_data():
    import json

    with open("anime.json", encoding="utf-8") as f:
        data = json.load(f)

    anime_dict = {genre: [[item['title'], item['description']] for item in items]
                  for genre, items in data.items()}

    return anime_dict


import flask as f

app = f.Flask(__name__)

app = f.Flask(__name__)
@app.route('/')
def show_home():
    return f.render_template("home.html")
@app.route('/anime')
def show_anime():
    anime_dict = get_data()
    return f.render_template("anime.html", anime=anime_dict)



def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()