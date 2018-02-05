from trivia.views import trivia, score,mostrarpregunta,templated
from django.urls import path

urlpatterns = [
    path('trivia/', templated, name='templated'),

    path('mostrarpregunta/',mostrarpregunta,name='mostrarpregunta')
]
