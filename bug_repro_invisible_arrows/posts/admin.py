from django.contrib import admin
from django.contrib.admin.decorators import register

from posts.models import Post


@register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
