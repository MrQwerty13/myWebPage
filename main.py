import flask as f



app = f.Flask(__name__)

@app.route('/')
def show_home():
    return f.render_template("home.html")



def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()