from django.contrib import admin

# Register your models here.
from ticketing.models import Movie, Cinema, Showtime

admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(Showtime)