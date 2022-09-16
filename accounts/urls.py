from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/details', views.profile_details, name='profile_details'),
    path('payment/list/', views.payment_list, name='payment_list'),
    path('payment/create/', views.payment_creat, name = 'payment_create'),
    path('profile/edit/', views.profile_edit, name='profile_edit')
]