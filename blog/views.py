from django.shortcuts import get_object_or_404, render

from .models import Post


def starting_page(request):
    latest_posts = Post.objects.select_related("author").order_by("-date", "-id")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts,
    })


def posts(request):
    all_posts = Post.objects.select_related("author").order_by("-date", "-id")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts,
    })


def post_detail(request, slug):
    identified_post = get_object_or_404(
        Post.objects.select_related("author").prefetch_related("tags"),
        slug=slug,
    )
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all(),
    })
