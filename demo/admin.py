from django.contrib import admin

from .models import GameReservation
from .models import GameRequest


admin.site.register(GameReservation)
admin.site.register(GameRequest)