from django.contrib import admin

from .models import Books,Author,Published

admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Published)
