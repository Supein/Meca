from django.contrib import admin

from .models import *


admin.site.register(Player)
admin.site.register(GameReservation)
admin.site.register(GameRequest)
admin.site.register(Image)
admin.site.register(Game)
admin.site.register(ImageChallenge)