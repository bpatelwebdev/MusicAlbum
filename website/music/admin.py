from django.contrib import admin

# Register your models here.
from.models import Album
from.models import Song

admin.site.register(Song)
admin.site.register(Album)