from django.contrib import admin
from .models import *



@admin.register(Document)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Host)
class AuthorAdmin(admin.ModelAdmin):
    pass


