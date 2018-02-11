from trivia.views import  score,mostrarpregunta,templated,templatetrivia
from django.urls import path

urlpatterns = [
    path('trivia/', templated, name='templated'),
path('score/', score, name='Score'),
    path('mostrarpregunta/',mostrarpregunta,name='mostrarpregunta'),
    path('creartrivia/',templatetrivia,name='creartrivia')
    ]
