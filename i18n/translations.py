from __future__ import annotations

STRINGS: dict[str, dict[str, str]] = {
    # Nav / chrome
    "nav.write": {"en": "Write a take", "ru": "Написать отзыв"},
    "nav.settings": {"en": "Settings", "ru": "Настройки"},
    "nav.about": {"en": "Founder", "ru": "Основатель"},
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
    "prefs.accent_hint": {
        "en": "Drag the strip to pick an accent.",
        "ru": "Потяните полоску, чтобы выбрать акцент.",
    },
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
    "feed.comments": {
        "en": "{count} comments",
        "ru": "Комментарии: {count}",
    },
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
    "edit.title": {"en": "Edit take — Aftertaste", "ru": "Редактировать — Aftertaste"},
    "edit.heading": {"en": "Edit your take", "ru": "Редактировать отзыв"},
    "edit.lede": {
        "en": "Tweak the drink name or what you thought — then save.",
        "ru": "Подправьте название напитка или отзыв — и сохраните.",
    },
    "edit.submit": {"en": "Save changes", "ru": "Сохранить"},
    "edit.cancel": {"en": "Cancel", "ru": "Отмена"},
    "detail.kicker": {"en": "One take", "ru": "Один отзыв"},
    "detail.back": {"en": "Back to feed", "ru": "К ленте"},
    "detail.edited": {"en": "Edited {when}", "ru": "Изменено {when}"},
    "post.edit": {"en": "Edit", "ru": "Изменить"},
    "post.delete": {"en": "Delete", "ru": "Удалить"},
    "post.delete_confirm": {
        "en": "Delete this take permanently?",
        "ru": "Удалить этот отзыв навсегда?",
    },
    "comments.heading": {"en": "Comments", "ru": "Комментарии"},
    "comments.lede": {
        "en": "React to the take — keep it short and honest.",
        "ru": "Ответьте на отзыв — коротко и честно.",
    },
    "comments.empty": {
        "en": "No comments yet. Start the conversation.",
        "ru": "Пока нет комментариев. Начните разговор.",
    },
    "comments.field": {"en": "Your comment", "ru": "Ваш комментарий"},
    "comments.ph": {
        "en": "What did this take make you think?",
        "ru": "О чём заставил задуматься этот отзыв?",
    },
    "comments.submit": {"en": "Post comment", "ru": "Отправить"},
    "comments.login": {"en": "Log in to leave a comment", "ru": "Войдите, чтобы комментировать"},
    "comments.delete": {"en": "Delete", "ru": "Удалить"},
    "comments.delete_confirm": {
        "en": "Delete this comment?",
        "ru": "Удалить этот комментарий?",
    },
    "about.title": {"en": "Founder — Aftertaste", "ru": "Основатель — Aftertaste"},
    "about.kicker": {"en": "The person behind the glass", "ru": "Человек за бокалом"},
    "about.heading": {"en": "Mikhail", "ru": "Михаил"},
    "about.role": {
        "en": "Founder of Aftertaste · developer-engineer",
        "ru": "Основатель Aftertaste · разработчик-инженер",
    },
    "about.p1": {
        "en": "I built Aftertaste as a small place for honest notes on drinks — coffee, cocktails, tea, whatever is in the glass. Short takes, no noise.",
        "ru": "Я сделал Aftertaste как небольшое место для честных заметок о напитках — кофе, коктейли, чай, всё что в бокале. Короткие отзывы, без шума.",
    },
    "about.p2": {
        "en": "I write Python for the web, tinker with Bash, C++, C#, and Swift, and live on macOS. When I am not shipping code, I am usually watching Formula 1.",
        "ru": "Пишу на Python для веба, вожусь с Bash, C++, C# и Swift, живу на macOS. Когда не пишу код — обычно смотрю Формулу-1.",
    },
    "about.p3": {
        "en": "This project started as my own webpage and grew into a tiny social feed for taste. If you post something you drank, you are already part of it.",
        "ru": "Проект начинался как личная страница и вырос в маленькую ленту вкусов. Если вы написали о том, что пили — вы уже часть этого.",
    },
    "about.based": {"en": "Based in", "ru": "Город"},
    "about.based_value": {"en": "Moscow", "ru": "Москва"},
    "about.stack": {"en": "Tools", "ru": "Инструменты"},
    "about.stack_value": {
        "en": "Python, Flask, SQLite, Bash, C++, C#, Swift",
        "ru": "Python, Flask, SQLite, Bash, C++, C#, Swift",
    },
    "about.elsewhere": {"en": "Elsewhere", "ru": "Ещё"},
    "about.back": {"en": "Back to feed", "ru": "К ленте"},
    "about.repo": {"en": "View the repo", "ru": "Репозиторий"},
    # Flashes / errors
    "flash.welcome": {"en": "Welcome to Aftertaste.", "ru": "Добро пожаловать в Aftertaste."},
    "flash.hello": {"en": "Hey, {username}.", "ru": "Привет, {username}."},
    "flash.signed_out": {"en": "Signed out.", "ru": "Вы вышли."},
    "flash.post_live": {"en": "Your take is live.", "ru": "Ваш отзыв опубликован."},
    "flash.post_updated": {"en": "Take updated.", "ru": "Отзыв обновлён."},
    "flash.post_deleted": {"en": "Take deleted.", "ru": "Отзыв удалён."},
    "flash.post_missing": {"en": "Post not found.", "ru": "Отзыв не найден."},
    "flash.comment_added": {"en": "Comment posted.", "ru": "Комментарий добавлен."},
    "flash.comment_deleted": {"en": "Comment deleted.", "ru": "Комментарий удалён."},
    "flash.comment_missing": {"en": "Comment not found.", "ru": "Комментарий не найден."},
    "flash.login_required": {"en": "Log in to continue.", "ru": "Войдите, чтобы продолжить."},
    "post_missing": {"en": "Post not found.", "ru": "Отзыв не найден."},
    "post_forbidden": {
        "en": "You can only change your own takes.",
        "ru": "Можно менять только свои отзывы.",
    },
    "comment_empty": {
        "en": "Write something before posting a comment.",
        "ru": "Напишите текст комментария.",
    },
    "comment_too_long": {
        "en": "Comment is too long (max 1000 characters).",
        "ru": "Комментарий слишком длинный (макс. 1000 символов).",
    },
    "comment_forbidden": {
        "en": "You can only delete your own comments.",
        "ru": "Можно удалять только свои комментарии.",
    },
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
        "en": "Invalid email or password.",
        "ru": "Неверный email или пароль.",
    },
    # Settings
    "settings.title": {"en": "Settings — Aftertaste", "ru": "Настройки — Aftertaste"},
    "settings.heading": {"en": "Settings", "ru": "Настройки"},
    "settings.lede": {
        "en": "Tune how Aftertaste looks, and manage your account.",
        "ru": "Настройте внешний вид Aftertaste и управляйте аккаунтом.",
    },
    "settings.appearance": {"en": "Appearance", "ru": "Внешний вид"},
    "settings.appearance_lede": {
        "en": "Theme, accent color, and language for this browser.",
        "ru": "Тема, цвет акцента и язык для этого браузера.",
    },
    "settings.account": {"en": "Account", "ru": "Аккаунт"},
    "settings.signed_in_as": {
        "en": "Signed in as {name}.",
        "ru": "Вы вошли как {name}.",
    },
    "settings.signed_out_hint": {
        "en": "Sign in to post takes and manage your account.",
        "ru": "Войдите, чтобы публиковать отзывы и управлять аккаунтом.",
    },
    "settings.danger": {"en": "Danger zone", "ru": "Опасная зона"},
    "settings.delete_lede": {
        "en": "Permanently delete your account, your takes, likes, and comments. This cannot be undone.",
        "ru": "Навсегда удалит аккаунт, ваши отзывы, оценки и комментарии. Это нельзя отменить.",
    },
    "settings.delete_password": {
        "en": "Confirm with your password",
        "ru": "Подтвердите паролем",
    },
    "settings.delete_submit": {"en": "Delete account", "ru": "Удалить аккаунт"},
    "settings.delete_confirm": {
        "en": "Delete your account and all your takes permanently?",
        "ru": "Удалить аккаунт и все ваши отзывы навсегда?",
    },
    "settings.delete_bad_password": {
        "en": "Wrong password. Account was not deleted.",
        "ru": "Неверный пароль. Аккаунт не удалён.",
    },
    "flash.account_deleted": {
        "en": "Your account was deleted.",
        "ru": "Ваш аккаунт удалён.",
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
DEFAULT_LANG = "en"
DEFAULT_THEME = "light"
DEFAULT_ACCENT_HUE = 95  # lime-green default

# Map legacy named accent cookies to hues.
LEGACY_ACCENT_HUES = {
    "lime": 95,
    "red": 8,
    "blue": 217,
    "amber": 38,
    "teal": 170,
}
