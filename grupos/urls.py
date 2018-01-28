from . import views
from django.urls import path
from grupos.views import invitarusuario,usuariosgrupo,misgrupos,grupousuarios,agregargrupo,responderinvitacion,useradmingroup

urlpatterns = [
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #path('login/', login , name='login'),
    #path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    #path('signup/', core_views.signup, name='signup'),
    path('invitarusuario/', invitarusuario, name='invitarusuario'),
    path('agregargrupo/', agregargrupo, name='agregargrupo'),
    path('responderinvitacion/', responderinvitacion, name='responderinvitacion'),
    path('useradmingroup/', useradmingroup, name='useradmingroup'),
    path('misgrupos/', misgrupos, name='misgrupos'),
    path('grupousuarios/', grupousuarios, name='grupousuarios'),
    path('usuariosgrupo/', usuariosgrupo, name='usuariosgrupo')  ]
