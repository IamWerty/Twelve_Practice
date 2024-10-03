from django.urls import path
from .views import *

app_name = 'reviews'

urlpatterns = [
    path('', review_list, name='list'),
    path('add/', add_review, name='add'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]
