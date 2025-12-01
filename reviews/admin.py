from django.contrib import admin
from .models import Names
# Register your models here.

class NamesAdmin(admin.ModelAdmin):
    list_display = ("name", "review_text", "rating", )

admin.site.register(Names, NamesAdmin)