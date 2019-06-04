from django.contrib import admin
from django.urls import path
from .views import RegsiterUserAPI,JustForTest
# from .models import Users
urlpatterns = [
    path('regsiterUser/', JustForTest),

]