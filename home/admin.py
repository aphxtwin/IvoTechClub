from django.contrib import admin
from .models import Posts, Categories, Inventions
# Register your models here.

admin.site.register(Posts)
admin.site.register(Categories)
admin.site.register(Inventions)