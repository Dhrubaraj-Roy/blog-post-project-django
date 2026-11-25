from django.contrib import admin

from .models import Author, Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "date")
    list_filter = ("author", "tags", "category", "date")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
