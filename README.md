# Aftertaste

Web app where people post short opinions about drinks they’ve had, and others like those takes.

## Stack

- Python + Flask
- JSON file storage
- OOP models (`User`, `Post`, `Like`)
- HTML / CSS / JS (Jinja templates)

## Run locally

```bash
source .venv/bin/activate
pip install -r requirements.txt
FLASK_DEBUG=1 python app.py
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080).

## MVP features

1. Create an account / log in
2. Write a post about a drink
3. Browse the feed
4. Like (or unlike) posts
5. Theme: light / dark (saved in a cookie)
6. Accent color: lime / red / blue / amber / teal (saved in a cookie)
7. Language: English / Russian (saved in a cookie)
8. Secret moderation panel at `/del` (not linked in the UI)

### Moderation

1. Open `/del`
2. Enter the moderation key (default: `aftertaste-mod`)
3. Delete takes as needed

Override with env vars:

```bash
export MODERATION_KEY='your-secret'
export SECRET_KEY='your-flask-secret'
```

Data is saved under `storage/data/*.json` (created automatically on first run).


### Hosting

The current url of the web-app is https://drink.pythonanywhere.com
