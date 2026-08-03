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
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000).

## MVP features

1. Create an account / log in
2. Write a post about a drink
3. Browse the feed
4. Like (or unlike) posts

Data is saved under `storage/data/*.json` (created automatically on first run).
