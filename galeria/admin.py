from django.contrib import admin
from galeria.models import Player

class ListandoPlayer(admin.ModelAdmin):
    list_display = ("id","nickname","role","team")
    list_display_links = ("id","nickname")
    search_fields = ("nickname","role")



admin.site.register(Player,ListandoPlayer)


# Register your models here.
