def get_data():
    import json

    with open("anime.json", encoding="utf-8") as f:
        data = json.load(f)

    anime_dict = {genre: [[item['title'], item['description']] for item in items]
                  for genre, items in data.items()}

    return anime_dict
