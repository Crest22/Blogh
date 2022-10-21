from django.contrib import admin

from .models import Comments,Category,Post


admin.site.register(Comments),
admin.site.register(Category),
admin.site.register(Post)
