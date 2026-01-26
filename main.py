import flask as f

app = f.Flask(__name__)


app = f.Flask(__name__)

@app.route('/')
def show_home():
    return f.render_template("home.html")


@app.route('/anime')
def show_anime(t = types, w_anime = watched_anime):
    return f.render_template("anime.html")

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()