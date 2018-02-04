from trivia.views import trivia, score
from django.urls import path

urlpatterns = [
    path('', trivia, name='trivia'),
    path('score/', score, name='score')
]
