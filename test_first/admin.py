from django.contrib import admin

from test_first.models import User, Post, Comment

# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
