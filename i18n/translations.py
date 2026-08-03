from __future__ import annotations

STRINGS: dict[str, dict[str, str]] = {
    # Nav / chrome
    "nav.write": {"en": "Write a take", "ru": "Написать отзыв"},
    "nav.sign_out": {"en": "Sign out", "ru": "Выйти"},
    "nav.log_in": {"en": "Log in", "ru": "Войти"},
    "nav.join": {"en": "Join", "ru": "Регистрация"},
    "prefs.theme": {"en": "Theme", "ru": "Тема"},
    "prefs.theme_light": {"en": "Light", "ru": "Светлая"},
    "prefs.theme_dark": {"en": "Dark", "ru": "Тёмная"},
    "prefs.lang": {"en": "Lang", "ru": "Язык"},
    "prefs.lang_en": {"en": "EN", "ru": "EN"},
    "prefs.lang_ru": {"en": "RU", "ru": "RU"},
    "prefs.accent": {"en": "Color", "ru": "Цвет"},
    "prefs.accent_lime": {"en": "Lime", "ru": "Лайм"},
    "prefs.accent_red": {"en": "Red", "ru": "Красный"},
    "prefs.accent_blue": {"en": "Blue", "ru": "Синий"},
    "prefs.accent_amber": {"en": "Amber", "ru": "Янтарный"},
    "prefs.accent_teal": {"en": "Teal", "ru": "Бирюза"},
    "prefs.look": {"en": "Look", "ru": "Вид"},
    # Feed
    "feed.title": {
        "en": "Aftertaste — drinks, then opinions",
        "ru": "Aftertaste — сначала напиток, потом мнение",
    },
    "feed.kicker": {"en": "Drink first. Talk later.", "ru": "Сначала выпей. Потом расскажи."},
    "feed.lede": {
        "en": "Short takes on what you just sipped — coffee, cocktails, tea, anything in a glass.",
        "ru": "Короткие отзывы о том, что только что выпили — кофе, коктейли, чай, всё что в бокале.",
    },
    "feed.create_account": {"en": "Create an account", "ru": "Создать аккаунт"},
    "feed.latest": {"en": "Latest takes", "ru": "Свежие отзывы"},
    "feed.latest_lede": {
        "en": "What people finished drinking, and what they thought.",
        "ru": "Что люди допили и что об этом подумали.",
    },
    "feed.empty": {
        "en": "No takes yet. Be the first to post what you drank.",
        "ru": "Пока пусто. Станьте первым — напишите, что пили.",
    },
    "feed.by": {"en": "by {name}", "ru": "от {name}"},
    "feed.open": {"en": "Open", "ru": "Открыть"},
    "like": {"en": "Like", "ru": "Нравится"},
    "liked": {"en": "Liked", "ru": "Оценено"},
    "like.login": {"en": "Log in to like", "ru": "Войдите, чтобы оценить"},
    "like.error": {
        "en": "Could not update like. Try again.",
        "ru": "Не удалось обновить оценку. Попробуйте ещё раз.",
    },
    "unknown_author": {"en": "Unknown", "ru": "Неизвестно"},
    # Auth
    "register.title": {"en": "Join — Aftertaste", "ru": "Регистрация — Aftertaste"},
    "register.heading": {"en": "Join Aftertaste", "ru": "Присоединяйтесь к Aftertaste"},
    "register.lede": {
        "en": "Create an account, then post what you drank.",
        "ru": "Создайте аккаунт и напишите, что пили.",
    },
    "register.submit": {"en": "Create account", "ru": "Создать аккаунт"},
    "register.foot": {"en": "Already here?", "ru": "Уже с нами?"},
    "login.title": {"en": "Log in — Aftertaste", "ru": "Вход — Aftertaste"},
    "login.heading": {"en": "Log in", "ru": "Вход"},
    "login.lede": {
        "en": "Pick up where you left your glass.",
        "ru": "Продолжайте с того места, где оставили бокал.",
    },
    "login.submit": {"en": "Log in", "ru": "Войти"},
    "login.foot": {"en": "New here?", "ru": "Впервые здесь?"},
    "field.username": {"en": "Username", "ru": "Имя пользователя"},
    "field.email": {"en": "Email", "ru": "Email"},
    "field.password": {"en": "Password", "ru": "Пароль"},
    # Compose / detail
    "compose.title": {"en": "Write a take — Aftertaste", "ru": "Новый отзыв — Aftertaste"},
    "compose.heading": {"en": "What did you drink?", "ru": "Что вы пили?"},
    "compose.lede": {
        "en": "Name the drink, then leave your honest aftertaste.",
        "ru": "Назовите напиток и оставьте честный послевкус.",
    },
    "compose.drink": {"en": "Drink name", "ru": "Название напитка"},
    "compose.drink_ph": {
        "en": "e.g. Oat flat white, Negroni, Matcha latte",
        "ru": "напр. Флэт уайт на овсе, Негрони, Матча-латте",
    },
    "compose.take": {"en": "Your take", "ru": "Ваш отзыв"},
    "compose.take_ph": {
        "en": "How it smelled, tasted, hit — keep it personal.",
        "ru": "Запах, вкус, ощущение — пишите по-своему.",
    },
    "compose.submit": {"en": "Publish", "ru": "Опубликовать"},
    "detail.kicker": {"en": "One take", "ru": "Один отзыв"},
    "detail.back": {"en": "Back to feed", "ru": "К ленте"},
    # Flashes / errors
    "flash.welcome": {"en": "Welcome to Aftertaste.", "ru": "Добро пожаловать в Aftertaste."},
    "flash.hello": {"en": "Hey, {username}.", "ru": "Привет, {username}."},
    "flash.signed_out": {"en": "Signed out.", "ru": "Вы вышли."},
    "flash.post_live": {"en": "Your take is live.", "ru": "Ваш отзыв опубликован."},
    "flash.post_missing": {"en": "Post not found.", "ru": "Отзыв не найден."},
    "flash.login_required": {"en": "Log in to continue.", "ru": "Войдите, чтобы продолжить."},
    "username_too_short": {
        "en": "Username must be at least 3 characters.",
        "ru": "Имя пользователя — минимум 3 символа.",
    },
    "email_invalid": {
        "en": "Enter a valid email address.",
        "ru": "Введите корректный email.",
    },
    "password_too_short": {
        "en": "Password must be at least 6 characters.",
        "ru": "Пароль — минимум 6 символов.",
    },
    "username_taken": {
        "en": "That username is already taken.",
        "ru": "Это имя пользователя уже занято.",
    },
    "email_taken": {
        "en": "That email is already registered.",
        "ru": "Этот email уже зарегистрирован.",
    },
    "invalid_credentials": {
        "en": "Invalid username or password.",
        "ru": "Неверное имя пользователя или пароль.",
    },
    "drink_name_required": {
        "en": "Drink name is required.",
        "ru": "Укажите название напитка.",
    },
    "drink_name_too_long": {
        "en": "Drink name is too long.",
        "ru": "Название напитка слишком длинное.",
    },
    "content_too_short": {
        "en": "Write at least 10 characters about the drink.",
        "ru": "Напишите хотя бы 10 символов о напитке.",
    },
    "content_too_long": {
        "en": "Opinion is too long (max 2000 characters).",
        "ru": "Отзыв слишком длинный (макс. 2000 символов).",
    },
    # Moderation
    "mod.title": {"en": "Moderate takes", "ru": "Модерация отзывов"},
    "mod.unlock_heading": {"en": "Moderator access", "ru": "Доступ модератора"},
    "mod.unlock_lede": {
        "en": "Enter the moderation key to manage drinks.",
        "ru": "Введите ключ модерации, чтобы управлять отзывами.",
    },
    "mod.key": {"en": "Moderation key", "ru": "Ключ модерации"},
    "mod.unlock": {"en": "Unlock", "ru": "Открыть"},
    "mod.lock": {"en": "Lock panel", "ru": "Закрыть панель"},
    "mod.delete": {"en": "Delete", "ru": "Удалить"},
    "mod.confirm": {
        "en": "Delete this take permanently?",
        "ru": "Удалить этот отзыв навсегда?",
    },
    "mod.empty": {"en": "Nothing to moderate.", "ru": "Нечего модерировать."},
    "mod.unlocked": {"en": "Moderator mode on.", "ru": "Режим модератора включён."},
    "mod.locked": {"en": "Moderator mode off.", "ru": "Режим модератора выключен."},
    "mod.bad_key": {"en": "Wrong moderation key.", "ru": "Неверный ключ модерации."},
    "mod.deleted": {"en": "Take deleted.", "ru": "Отзыв удалён."},
}

SUPPORTED_LANGS = ("en", "ru")
SUPPORTED_THEMES = ("light", "dark")
SUPPORTED_ACCENTS = ("lime", "red", "blue", "amber", "teal")
DEFAULT_LANG = "en"
DEFAULT_THEME = "light"
DEFAULT_ACCENT = "lime"

# Swatch colors shown in the accent picker (UI only).
ACCENT_SWATCHES = {
    "lime": "#b6d63a",
    "red": "#e85d4c",
    "blue": "#4c8dff",
    "amber": "#e6a23c",
    "teal": "#2db8a0",
}
