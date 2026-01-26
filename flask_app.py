import os, json

def get_data():
    BASE_DIR = "/home/mikhail13/myWebPage/static"  # <-- путь к твоему проекту на PythonAnywhere
    with open(os.path.join(BASE_DIR, "anime.json"), encoding="utf-8") as f:
        data = json.load(f)

    anime_dict = {genre: [[item['title'], item['description'], item['link']] for item in items]
                  for genre, items in data.items()}

    return anime_dict


import flask as f



app = f.Flask(__name__)
@app.route('/')
def show_home():
    return f.render_template("home.html")
@app.route('/anime')
def show_anime():
    anime_dict = get_data()
    return f.render_template("anime.html", anime=anime_dict)

@app.route('/author')
def show_author():
    return f.render_template("author.html")

