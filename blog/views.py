from django.http import Http404
from django.shortcuts import render

# Create your views here.

all_posts = [
    {
        "slug": "getting-started-with-django",
        "author": "Dhruba",
        "category": "Tutorial",
        "date": "Nov 18, 2026",
        "title": "Getting Started with Django: The Foundations",
        "excerpt": "Explore Django's MVT pattern, project initialization, settings management, and how to structure apps cleanly.",
        "content": """Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

At the core of Django is the Model-View-Template (MVT) architectural pattern. Models handle database structure and queries, Views contain the business logic and request processing, and Templates render the final HTML presented to the user.

When starting a new Django project, creating focused, modular apps (like our blog app) keeps your codebase organized and easy to maintain as your project grows. By separating project-level settings from app-specific routing, you ensure modularity and code reusability across your application.""",
        "tags": ["Django", "Python", "WebDev", "Backend"],
    },
    {
        "slug": "mastering-urls-and-views",
        "author": "Dhruba",
        "category": "Architecture",
        "date": "Nov 15, 2026",
        "title": "Mastering URLs, Slugs and Dynamic Routing",
        "excerpt": "How Django path converters work, transforming slugs into model queries, and building SEO-friendly URL patterns.",
        "content": """URL routing and view dispatching are the heart of Django's request-response lifecycle. Every HTTP request begins by matching against the urlpatterns list defined in your URL configuration files.

Django provides built-in path converters like str, int, and slug. A slug is a short label for something, containing only letters, numbers, underscores, or hyphens. They are commonly used in URLs to make them human-readable and SEO-friendly.

By configuring dynamic route parameters such as `<slug:slug>`, Django captures the matched segment and passes it cleanly as a keyword argument into your view function. This enables clean database lookups and beautiful URLs without relying on messy query strings.""",
        "tags": ["Routing", "URLs", "Django", "Architecture"],
    },
    {
        "slug": "building-sleek-uis-with-flowbite",
        "author": "Dhruba",
        "category": "Design & UI",
        "date": "Nov 10, 2026",
        "title": "Building Sleek UIs with Flowbite Publisher",
        "excerpt": "Integrating Flowbite Publisher blocks into Django templates with responsive layouts, dark mode, and typography.",
        "content": """Flowbite Publisher offers modern, accessible, and responsive components built with clean design principles. Integrating these patterns into Django templates gives your blog a polished, professional look with minimal overhead.

By utilizing template inheritance with a master base template, child templates can extend standard layouts while overriding specific blocks like content and css_files. This keeps your templates DRY (Don't Repeat Yourself).

Organizing static stylesheets into dedicated scoped files—such as app.css for global rules, post.css for cards, and post-detail.css for articles—guarantees maintainability, fast load times, and an exceptional user experience across both light and dark modes.""",
        "tags": ["UI/UX", "Flowbite", "Design", "CSS"],
    },
]


def starting_page(request):
    return render(request, "blog/index.html", {
        "posts": all_posts[-3:]
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next((post for post in all_posts if post["slug"] == slug), None)
    if identified_post is None:
        raise Http404("Post not found!")
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
