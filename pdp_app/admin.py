from django.contrib import admin
from pdp_app.models import Post, Comment, State

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(State)