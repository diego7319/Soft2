from . import views
from django.urls import path
from grupos.views import invitarusuario,agregargrupo

urlpatterns = [
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #path('login/', login , name='login'),
    #path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    #path('signup/', core_views.signup, name='signup'),
    path('invitarusuario/', invitarusuario, name='invitarusuario'),
    path('agregargrupo/', agregargrupo, name='agregargrupo')

    ]