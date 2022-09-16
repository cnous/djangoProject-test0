from django.urls.conf import path
from ticketing import views

app_name = 'ticketing'
urlpatterns = [
    path('movie/list', views.movie_list, name='movie_list'),
    path('movie/detail/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('cinema/list', views.cinema_list, name='cinema_list'),
    path('cineama/detail/<int:cinema_id>/ ', views.cinema_detail, name='cinema_detail'),
    path('showtime/list', views.showtime_list, name='showtime_list'),
    path('showtime/details/<int:showtime_id>/', views.showtime_details, name='showtime_details'),
    path('ticket/list', views.ticket_list, name='ticket_list'),
    path('ticket/details/<int:ticket_id>', views.ticket_details, name='ticket_details'),
]
