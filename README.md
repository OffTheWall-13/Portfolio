![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
<h1 align="center">🌐 Personal Portfolio</h1>

<p align="center">
Backend Developer Portfolio built with FastAPI
</p>

Современный сайт-портфолио, разработанный на **FastAPI**, где можно познакомиться со мной, посмотреть мои проекты и связаться со мной через форму обратной связи.

При отправке сообщения с сайта информация автоматически отправляется мне в Telegram с помощью собственного бота.

---

## ✨ Возможности

- ⚡ Backend на FastAPI
- 🎨 Современный адаптивный интерфейс
- 📂 Страница с информацией обо мне
- 💼 Демонстрация проектов
- 📬 Форма обратной связи
- 🤖 Telegram-уведомления о новых сообщениях
- ✅ Валидация пользовательских данных
- 🚀 Готов к деплою

---

## 🛠️ Стек технологий

- Python 3
- FastAPI
- HTML5
- CSS3
- JavaScript
- Telegram Bot API
- Uvicorn

---

## 📁 Структура проекта

```

portfolio/
│
├── templates/
│   └── index.html/
│ 
├── notifications/
│   ├── init.py/
│   └── notifier.py/
│
├── requirements.txt
├── README.md
├── models.py
├── main.py
└── .env

````

---

## 🚀 Запуск проекта

### 1. Клонировать репозиторий

``` bash
git clone https://github.com/OffTheWall-13/portfolio.git
```

### 2. Перейти в папку проекта

``` bash
cd portfolio
```

### 3. Создать виртуальное окружение

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Установить зависимости

```bash
pip install -r requirements.txt
```

### 5. Создать файл `.env`

Пример:

```env
BOT_TOKEN=your_bot_token
CHAT_ID=your_chat_id
```

### 6. Запустить сервер

```bash
uvicorn app.main:app --reload
```

После запуска сайт будет доступен по адресу:

```
http://127.0.0.1:8000
```

---

## 📬 Обратная связь

После заполнения формы:

* данные проходят проверку;
* выполняется POST-запрос на сервер;
* сообщение автоматически отправляется в Telegram;
* пользователь получает подтверждение успешной отправки.
