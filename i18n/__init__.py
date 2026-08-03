from __future__ import annotations

from flask import g, request

from i18n.translations import (
    ACCENT_SWATCHES,
    DEFAULT_ACCENT,
    DEFAULT_LANG,
    DEFAULT_THEME,
    STRINGS,
    SUPPORTED_ACCENTS,
    SUPPORTED_LANGS,
    SUPPORTED_THEMES,
)

THEME_COOKIE = "aftertaste_theme"
LANG_COOKIE = "aftertaste_lang"
ACCENT_COOKIE = "aftertaste_accent"
COOKIE_MAX_AGE = 60 * 60 * 24 * 365


def normalize_theme(value: str | None) -> str:
    if value in SUPPORTED_THEMES:
        return value
    return DEFAULT_THEME


def normalize_lang(value: str | None) -> str:
    if value in SUPPORTED_LANGS:
        return value
    return DEFAULT_LANG


def normalize_accent(value: str | None) -> str:
    if value in SUPPORTED_ACCENTS:
        return value
    return DEFAULT_ACCENT


def current_theme() -> str:
    return getattr(g, "theme", DEFAULT_THEME)


def current_lang() -> str:
    return getattr(g, "lang", DEFAULT_LANG)


def current_accent() -> str:
    return getattr(g, "accent", DEFAULT_ACCENT)


def translate(key: str, **kwargs) -> str:
    entry = STRINGS.get(key, {})
    text = entry.get(current_lang()) or entry.get(DEFAULT_LANG) or key
    if kwargs:
        return text.format(**kwargs)
    return text


def load_prefs() -> None:
    g.theme = normalize_theme(request.cookies.get(THEME_COOKIE))
    g.lang = normalize_lang(request.cookies.get(LANG_COOKIE))
    g.accent = normalize_accent(request.cookies.get(ACCENT_COOKIE))
