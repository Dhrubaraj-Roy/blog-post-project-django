from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Author, Post, Tag


class BlogModelsAndViewsTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="Dhruba",
            last_name="Roy",
            email_address="dhruba@example.com",
        )
        self.tag_django = Tag.objects.create(name="Django")
        self.tag_python = Tag.objects.create(name="Python")

        self.post = Post.objects.create(
            title="Getting Started with Django",
            excerpt="Explore Django's MVT pattern and project setup.",
            category="Tutorial",
            date=date(2026, 11, 18),
            slug="getting-started-with-django",
            content="Django is a high-level Python web framework for rapid development.",
            author=self.author,
        )
        self.post.tags.add(self.tag_django, self.tag_python)

    def test_post_relations(self):
        self.assertEqual(self.post.author, self.author)
        self.assertEqual(self.author.posts.count(), 1)
        self.assertEqual(self.post.tags.count(), 2)
        self.assertEqual(str(self.author), "Dhruba Roy")
        self.assertEqual(str(self.tag_django), "Django")
        self.assertEqual(str(self.post), "Getting Started with Django")

    def test_starting_page_view(self):
        response = self.client.get(reverse("starting-page"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Getting Started with Django")
        self.assertContains(response, "Dhruba Roy")

    def test_all_posts_view(self):
        response = self.client.get(reverse("posts-page"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Getting Started with Django")

    def test_post_detail_view(self):
        response = self.client.get(
            reverse("post-detail-page", args=[self.post.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Getting Started with Django")
        self.assertContains(response, "#Django")
        self.assertContains(response, "#Python")
        self.assertContains(response, 'href="mailto:dhruba@example.com"')

    def test_post_detail_404(self):
        response = self.client.get(
            reverse("post-detail-page", args=["non-existent-slug"])
        )
        self.assertEqual(response.status_code, 404)
