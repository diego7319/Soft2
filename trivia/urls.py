from trivia.views import trivia, score,mostrarpregunta
from django.urls import path

urlpatterns = [
    path('trivia/', trivia, name='trivia'),
    path('score/', score, name='score'),
    path('mostrarpregunta/',mostrarpregunta,name='mostrarpregunta')
]
