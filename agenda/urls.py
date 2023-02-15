from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user),
    path('login/submit', views.submit),
    path('logout/', views.logout_user),
    path('agenda/', views.listar_eventos),
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit', views.submit_evento),
    path('agenda/evento/delete/<int:id_evento>', views.delete_evento),
    path('', RedirectView.as_view(url='/agenda/'))
]
