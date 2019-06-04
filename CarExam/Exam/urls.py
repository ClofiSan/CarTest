from django.contrib import admin
from django.urls import path
from .views import *
# from .models import Users
urlpatterns = [
    path('regsiterUser/', RegsiterUserAPI),
    path('userLogin/',UserLoginAPI),
    path('regsiterStudent/',RegsiterStudentAPI),
    path('StudentLogin/',StudentLoginAPI),
    path('test/',JustForTest)

]