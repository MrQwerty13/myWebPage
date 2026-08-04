# Aftertaste

Web app where people post short opinions about drinks they’ve had, and others like and comment on those takes.

## Stack

- Python + Flask
- SQLite storage
- OOP models (`User`, `Post`, `Like`, `Comment`)
- HTML / CSS / JS (Jinja templates)

## Run locally

```bash
source .venv/bin/activate
pip install -r requirements.txt
FLASK_DEBUG=1 python app.py
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080).

Optional demo data:

```bash
python seed.py
```

## MVP features

1. Create an account / log in
2. Write a post about a drink
3. Edit or delete your own posts
4. Browse the feed
5. Like (or unlike) posts
6. Comment on posts
7. Theme: light / dark (saved in a cookie)
8. Accent color: RGB hue strip slider (saved in a cookie)
9. Language: English / Russian (saved in a cookie)
10. Founder / about page at `/about`
11. Secret moderation panel at `/del` (not linked in the UI)

### Moderation

1. Open `/del`
2. Enter the moderation key (default: `wanna_clean`)
3. Delete takes as needed

Override with env vars:

```bash
export MODERATION_KEY='your-secret'
export SECRET_KEY='your-flask-secret'
```

Data is saved in `storage/data/aftertaste.db` (created automatically on first run). Legacy JSON files under `storage/data/*.json` are imported once if the database is empty.

### Hosting

The current url of the web-app is https://drink.pythonanywhere.com
