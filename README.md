# Dhruba's Blog — Django Web App

Welcome to my personal blog project! I built this web application using Django and modern UI components from Flowbite Publisher. My goal with this project is to create a clean, responsive, and maintainable blogging platform from the ground up while following Django's best architectural practices.

---

## Tech Stack

- **Backend Framework:** Django 6.0 / Python 3.13
- **Styling & UI:** Tailwind CSS & Flowbite (Publisher UI theme)
- **Custom Styles:** Vanilla CSS (`app.css`)
- **Database:** SQLite (default Django database engine)

---

## How I Built This App Step by Step

Here is a breakdown of how I designed and built this project from scratch:

### 1. Project Initialization & Architecture
I started by initializing the Django project configuration named `config`. To keep concerns separated and maintainable, I created a dedicated Django application named `blog`:
```bash
python manage.py startapp blog
```
I then registered `'blog'` into `INSTALLED_APPS` inside `config/settings.py` so Django is aware of the app and its resources.

### 2. URL Routing & Modular App Structure
Instead of dumping all routing into the root configuration, I decoupled the routing:
- **Project URL Configuration (`config/urls.py`):** Uses Django's `include()` function to forward all root traffic directly to the `blog` app.
- **App URL Configuration (`blog/urls.py`):** Set up three primary routes:
  1. `""` (named `starting-page`) — The landing/home page.
  2. `"posts"` (named `posts-page`) — The archive page for all posts.
  3. `"posts/<slug:slug>"` (named `post-detail-page`) — A dynamic route utilizing Django's built-in `slug` path converter to display individual post articles cleanly.

### 3. View Logic Setup
In `blog/views.py`, I defined the corresponding view functions:
- `starting_page(request)`: Handles rendering the home page (`blog/index.html`).
- `posts(request)`: Prepared for listing all posts.
- `post_detail(request, slug)`: Prepared to accept the URL slug parameter to load specific articles.

### 4. Two-Tier Template System & Inheritance
To keep the markup DRY (Don't Repeat Yourself), I set up a two-tier template architecture:
1. **Global Templates (`templates/`):**
   - Configured `TEMPLATES['DIRS']` in `config/settings.py` to point to `BASE_DIR / 'templates'`.
   - Created `templates/base.html` containing the global HTML skeleton, meta tags, CDNs, header navigation, and footer.
2. **App-Level Templates (`blog/templates/blog/`):**
   - Created `index.html` which inherits from `base.html` via `{% extends "base.html" %}` and injects custom page content into the `{% block content %}` region.

### 5. UI Design with Flowbite Publisher & Custom Styling
For the frontend, I wanted a polished, modern look without heavy setup overhead:
- **Navigation:** Created a responsive top navigation bar in `base.html` displaying **"Dhruba's Blog"** on the left corner and an **"All posts"** link on the right.
- **Hero & Bio:** On the starting page, I added a personalized welcome section featuring my profile photo, a welcoming greeting, and a short introduction.
- **Article Grid:** Built a responsive 3-column card grid powered by Flowbite Publisher components, complete with category tags, publication dates, author avatars, post excerpts, and call-to-action buttons.
- **Static Assets (`blog/static/blog/app.css`):** Added a custom stylesheet for color variables, smooth scrolling, custom scrollbars, and card hover micro-interactions.

---

## Project Structure

```text
blog-post-project-django/
├── manage.py
├── config/                  # Project configuration
│   ├── settings.py          # Settings (INSTALLED_APPS, TEMPLATES, etc.)
│   ├── urls.py              # Root URL dispatcher
│   ├── wsgi.py
│   └── asgi.py
├── blog/                    # Blog application
│   ├── urls.py              # App-level URL routes
│   ├── views.py             # View functions (starting_page, posts, post_detail)
│   ├── models.py            # Data models
│   ├── static/
│   │   └── blog/
│   │       └── app.css      # Custom styling & Flowbite enhancements
│   └── templates/
│       └── blog/
│           └── index.html   # Starting/landing page template
├── templates/               # Global templates
│   └── base.html            # Master layout with navbar & footer
└── README.md
```

---

## Running the Project Locally

If you'd like to run this project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Dhrubaraj-Roy/blog-post-project-django.git
   cd blog-post-project-django
   ```

2. **Make sure Python and Django are installed:**
   ```bash
   python3 -m pip install django
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

5. Open your browser and navigate to `http://127.0.0.1:8000/`.
