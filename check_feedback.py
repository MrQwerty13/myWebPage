import os
import json

# Путь к файлу feedback.json
FEEDBACK_FILE = os.path.join("static", "feedback.json")

# Проверяем, существует ли файл
if not os.path.exists(FEEDBACK_FILE):
    print("Файл feedback.json не найден.")
    exit()

# Открываем и читаем JSON
with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
    feedback_list = json.load(f)

# Выводим в консоль в читаемом виде
if not feedback_list:
    print("Нет сообщений.")
else:
    for entry in feedback_list:
        username = entry.get("username", "неизвестно")
        message = entry.get("message", "")
        print(f"Сообщение от {username}:\n{message}\n{'-'*40}")
