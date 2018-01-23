from . import views
from django.urls import path
from users.views import index
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from users import views as core_views




urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('signup/', core_views.signup, name='signup'),
    path('index/', core_views.index, name='index')


]
