from django.contrib import admin
from django.urls import path
from .views import *
# from .models import Users
urlpatterns = [
    path('regsiterUser/', RegsiterUserAPI),
    path('userLogin/',UserLoginAPI),
    path('regsiterStudent/',RegsiterStudentAPI),
    path('studentLogin/',StudentLoginAPI),

    path('regsiterExam/',RegsiterExamAPI),
    path('examLogin/',ExamLoginAPI),

    path('JudgeMark/',JudgeMarkAPI),

    path('test/',JustForTest),

    path('login/',getUserLoginPage),
    path('new',UserSuc)


]