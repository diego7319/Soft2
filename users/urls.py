from . import views
from django.urls import path
from users.views import index,perfil,log_out
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView



urlpatterns = [
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #path('login/', login , name='login'),
    #path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    #path('signup/', core_views.signup, name='signup'),
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('logout/', log_out, name='logout')
    ]
