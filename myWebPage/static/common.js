/* Theme + Language switcher for Drink Tracker */

const translations = {
  en: {
    // Homepage
    "hero.title": "🥤 Drink Tracker",
    "hero.subtitle": "Discover, rate, and share your favourite drinks",
    "hero.cta": "View Collection →",
    "hero.authors": "Meet the Authors →",
    "why.title": "Why Drink Tracker?",
    "why.ratings": "Track Ratings",
    "why.ratings.desc": "Rate every drink from 0 to 10 and see how it compares to others.",
    "why.popularity": "Popularity Counter",
    "why.popularity.desc": "Give a 👍 to your favourites and watch their popularity grow.",
    "why.brands": "Multiple Brands",
    "why.brands.desc": "Red Bull, Monster, Milky’s – all in one place, with more coming.",
    "why.community": "Community Driven",
    "why.community.desc": "Add your own drinks and see what others are enjoying.",
    "footer": "Drink Tracker • Flask + Python",

    // Drinks page
    "drinks.title": "🥤 Drink Tracker",
    "drinks.subtitle": "Track your favorite drinks!",
    "drinks.sort": "Sort by:",
    "drinks.sort.author": "Author",
    "drinks.sort.brand": "Brand",
    "drinks.sort.rating": "Rating",
    "drinks.sort.popularity": "Popularity",
    "drinks.sort.name": "Name",
    "drinks.add": "Add a Drink",
    "drinks.name": "Drink name",
    "drinks.brand": "Select Brand",
    "drinks.volume": "Select Volume",
    "drinks.taste": "Select Taste",
    "drinks.assessment": "Assessment",
    "drinks.description": "Description",
    "drinks.author": "Select Author",
    "drinks.save": "Save",
    "drinks.popularity": "Popularity:",
    "drinks.confirm_delete": "Are you sure you want to delete this drink?",
    "drinks.empty": "No drinks yet. Add the first one!",

    // Authors page
    "authors.title": "Meet the Authors",
    "authors.subtitle": "The people behind Drink Tracker",
    "authors.role": "Role",
    "authors.favorite": "Favourite drink",
    "authors.back": "← Back to Home",
    "authors.view_drinks": "View Collection →",
  },
  ru: {
    "hero.title": "🥤 Drink Tracker",
    "hero.subtitle": "Открывай, оценивай и делись любимыми напитками",
    "hero.cta": "Смотреть коллекцию →",
    "hero.authors": "Познакомиться с авторами →",
    "why.title": "Почему Drink Tracker?",
    "why.ratings": "Оценки",
    "why.ratings.desc": "Оценивай каждый напиток от 0 до 10 и сравнивай с остальными.",
    "why.popularity": "Счётчик популярности",
    "why.popularity.desc": "Ставь 👍 любимым и смотри, как растёт их популярность.",
    "why.brands": "Несколько брендов",
    "why.brands.desc": "Red Bull, Monster, Milky’s — всё в одном месте, и это только начало.",
    "why.community": "Сообщество",
    "why.community.desc": "Добавляй свои напитки и смотри, что нравится другим.",
    "footer": "Drink Tracker • Flask + Python",

    "drinks.title": "🥤 Drink Tracker",
    "drinks.subtitle": "Отслеживай любимые напитки!",
    "drinks.sort": "Сортировка:",
    "drinks.sort.author": "Автор",
    "drinks.sort.brand": "Бренд",
    "drinks.sort.rating": "Оценка",
    "drinks.sort.popularity": "Популярность",
    "drinks.sort.name": "Название",
    "drinks.add": "Добавить напиток",
    "drinks.name": "Название напитка",
    "drinks.brand": "Выберите бренд",
    "drinks.volume": "Выберите объём",
    "drinks.taste": "Выберите вкус",
    "drinks.assessment": "Оценка",
    "drinks.description": "Описание",
    "drinks.author": "Выберите автора",
    "drinks.save": "Сохранить",
    "drinks.popularity": "Популярность:",
    "drinks.confirm_delete": "Вы уверены, что хотите удалить этот напиток?",
    "drinks.empty": "Пока нет напитков. Добавьте первый!",

    "authors.title": "Знакомьтесь с авторами",
    "authors.subtitle": "Люди, стоящие за Drink Tracker",
    "authors.role": "Роль",
    "authors.favorite": "Любимый напиток",
    "authors.back": "← На главную",
    "authors.view_drinks": "Смотреть коллекцию →",
  },
};

function getLang() {
  return localStorage.getItem("dt_lang") || "en";
}

function setLang(lang) {
  localStorage.setItem("dt_lang", lang);
  applyTranslations(lang);
  document.documentElement.lang = lang;
  // Update active button
  document.querySelectorAll(".lang-btn").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.lang === lang);
  });
}

function applyTranslations(lang) {
  const dict = translations[lang] || translations.en;
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.getAttribute("data-i18n");
    if (dict[key]) {
      if (el.tagName === "INPUT" || el.tagName === "TEXTAREA") {
        el.placeholder = dict[key];
      } else if (el.tagName === "OPTION") {
        el.textContent = dict[key];
      } else {
        el.textContent = dict[key];
      }
    }
  });
  // Also update confirm message if needed
  window._confirmDeleteMsg = dict["drinks.confirm_delete"] || "Are you sure?";
}

function getTheme() {
  return localStorage.getItem("dt_theme") || "light";
}

function setTheme(theme) {
  localStorage.setItem("dt_theme", theme);
  document.documentElement.setAttribute("data-theme", theme);
  document.querySelectorAll(".theme-btn").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.theme === theme);
  });
}

function toggleTheme() {
  const next = getTheme() === "light" ? "dark" : "light";
  setTheme(next);
}

// Init on load
document.addEventListener("DOMContentLoaded", () => {
  setTheme(getTheme());
  setLang(getLang());
});
