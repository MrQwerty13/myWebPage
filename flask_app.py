import os
import json
from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

FEEDBACK_FILE = os.path.join("static", "feedback.json")  # файл для хранения сообщений

# ===== FEEDBACK PAGE =====
@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "GET":
        return render_template("feedback.html")

    # POST - добавление нового сообщения
    data = request.get_json()
    username = data.get("username")
    message = data.get("message")

    if not (username and message):
        return jsonify({"status": "error", "message": "Заполните все поля"}), 400

    # Загружаем существующие данные
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
            feedback_list = json.load(f)
    else:
        feedback_list = []

    # Добавляем новое сообщение
    feedback_list.append({"username": username, "message": message})

    # Сохраняем обратно
    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump(feedback_list, f, ensure_ascii=False, indent=2)

    return jsonify({"status": "ok"}), 200


# ===== ANIME DATA FUNCTIONS =====
def get_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(BASE_DIR, "static", "anime.json"), encoding="utf-8") as f_json:
        data = json.load(f_json)
    anime_dict = {
        genre: [
            [item["title"], item["description"], item["link"]]
            for item in items
        ]
        for genre, items in data.items()
    }
    return anime_dict


def get_random_anime():
    anime_dict = get_data()
    all_anime = []
    for items in anime_dict.values():
        all_anime.extend(items)
    return random.choice(all_anime)


# ===== ROUTES =====
@app.route("/")
def show_home():
    random_anime = get_random_anime()
    return render_template("home.html", anime=random_anime)


@app.route("/anime")
def show_anime():
    anime_dict = get_data()
    return render_template("anime.html", anime=anime_dict)


@app.route("/author")
def show_author():
    return render_template("author.html")


if __name__ == "__main__":
    app.run(host="192.168.1.106", port=5000, debug=True)

