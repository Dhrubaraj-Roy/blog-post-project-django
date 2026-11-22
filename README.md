# Dhruba's Blog — Django Web App

Welcome to my personal blog project! I built this web application using Django with a modern full dark theme inspired by Flowbite Publisher design principles. My goal with this project is to create a clean, responsive, and maintainable blogging platform from the ground up while strictly following Django's best architectural practices.

---

## Tech Stack

- **Backend Framework:** Django 6.0 / Python 3.13
- **Styling & Design System:** Custom Modular CSS with Full Dark Theme
- **UI Architecture:** Two-tier Django templates with reusable partial includes
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
- **Project URL Configuration (`config/urls.py`):** Uses Django's `include()` function to forward root traffic directly to the `blog` app.
- **App URL Configuration (`blog/urls.py`):** Set up three primary routes:
  1. `""` (named `starting-page`) — The landing/home page displaying the latest posts.
  2. `"posts"` (named `posts-page`) — The archive page for all published posts.
  3. `"posts/<slug:slug>"` (named `post-detail-page`) — A dynamic route utilizing Django's built-in `slug` path converter to display individual post articles cleanly.

### 3. View Logic & Dynamic Dummy Data
In `blog/views.py`, I structured the view logic and mock data:
- Defined an `all_posts` data structure containing post slugs, titles, authors, categories, dates, excerpts, full body paragraphs, and hashtags.
- `starting_page(request)`: Slices and passes the latest 3 posts to `blog/index.html`.
- `posts(request)`: Passes all posts to `blog/all-posts.html`.
- `post_detail(request, slug)`: Dynamically searches `all_posts` by matching the requested `slug`. If the slug is invalid or not found, it cleanly raises an `Http404` exception.

### 4. Template Architecture & Reusable Partials (DRY)
To keep the markup DRY (Don't Repeat Yourself), I established a modular template system:
1. **Global Base Template (`templates/base.html`):**
   - Configured `TEMPLATES['DIRS']` in `config/settings.py` to point to `BASE_DIR / 'templates'`.
   - Contains the global HTML skeleton, sticky navbar with branding and navigation links, footer, and dynamic `{% block content %}` and `{% block css_files %}` placeholders.
2. **Reusable Component Partials (`blog/templates/blog/includes/post.html`):**
   - Extracted the post card component markup into its own partial template.
   - Used Django's `{% include %}` tag inside loops in both `index.html` and `all-posts.html`, ensuring identical card formatting without code duplication.
3. **Dedicated Page Templates:**
   - `index.html`: Starting page featuring my personalized welcome hero section and latest posts grid.
   - `all-posts.html`: Archive page showing all posts with responsive grid columns.
   - `post-detail.html`: Article reading page with back navigation, author metadata, lead excerpt, formatted content paragraphs, and tag badges.

### 5. Scoped CSS Architecture & Full Dark Theme
Instead of using messy inline styles or utility clutter in the HTML, I extracted all styling into dedicated, modular stylesheets under `blog/static/blog/`:
- `app.css`: Design tokens, reset, typography, sticky navigation bar, and footer.
- `post.css`: Card layout, category badges, author avatar, hover transitions, and read-more actions.
- `index.css`: Welcome hero container, circular profile photo, and latest posts layout.
- `all-posts.css`: Header and responsive grid layout for the all-posts page.
- `post-detail.css`: Typography, reading column constraints, lead styling, and tag layout for article pages.
- **Theme:** Applied a cohesive Full Dark Theme utilizing deep slate backgrounds (`#0f172a`), elevated card surfaces (`#1e293b`), crisp text (`#f8fafc`), and vibrant blue accents (`#3b82f6` / `#60a5fa`).

### 6. Static File Serving Configuration
To ensure static files serve smoothly in local development across all sub-routes:
- Configured `STATIC_URL = '/static/'` with a leading slash in `config/settings.py`.
- Hooked `urlpatterns += staticfiles_urlpatterns()` into `config/urls.py` when `DEBUG = True` so Django explicitly routes and serves stylesheets with HTTP 200.

---

## Project Structure

```text
blog-post-project-django/
├── manage.py
├── config/                      # Project configuration
│   ├── settings.py              # App settings, TEMPLATES, and STATIC_URL
│   ├── urls.py                  # Root URL dispatcher + static files routing
│   ├── wsgi.py
│   └── asgi.py
├── blog/                        # Blog application
│   ├── urls.py                  # App-level routes (starting-page, posts, post-detail)
│   ├── views.py                 # Views (starting_page, posts, post_detail)
│   ├── models.py                # Database models
│   ├── static/
│   │   └── blog/                # Dedicated scoped stylesheets
│   │       ├── app.css          # Global theme, navbar, and footer styles
│   │       ├── post.css         # Reusable post card styles
│   │       ├── index.css        # Home page hero and latest posts styles
│   │       ├── all-posts.css    # All posts grid styles
│   │       └── post-detail.css  # Article detail view styles
│   └── templates/
│       └── blog/
│           ├── index.html       # Starting/landing page template
│           ├── all-posts.html   # All posts archive template
│           ├── post-detail.html # Single article detail template
│           └── includes/
│               └── post.html    # Reusable post card partial
├── templates/                   # Global templates
│   └── base.html                # Master layout with navbar & footer
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
