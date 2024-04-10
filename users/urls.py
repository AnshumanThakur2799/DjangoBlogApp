from django.urls import path
from .views import *
urlpatterns = [
    path('registration/' , RegisterUser.as_view())
]
