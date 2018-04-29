from django.contrib import admin
from Jared.models import User,Comment,Article,Tag

# Register your models here.

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Tag)

