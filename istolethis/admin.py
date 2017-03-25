from django.contrib import admin
from .models import *


class GametextInline(admin.TabularInline):
    model = GameText


class GameAdmin(admin.ModelAdmin):
    inlines = [GametextInline]


admin.site.register(Game, GameAdmin)
