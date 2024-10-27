from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index', views.index , name='index'),
    path('ajouter_terrain', views.ajouter_terrain, name='ajouter_terrain'),
    path('gestion_client', views.gestion_client, name='gestion_client'),
    path('gestion_terrain', views.gestion_terrain, name='gestion_terrain'),
    path('modifier_client', views.modifier_client, name='modifier_client'),
    path('supprimer_client', views.supprimer_client, name='supprimer_client'),
    path('ajouter_client', views.ajouter_client, name='ajouter_client'),
    path('modifier_terrain/<int:terrain_id>/', views.modifier_terrain, name='modifier_terrain'),
    path('supprimer_terrain/<int:terrain_id>/', views.supprimer_terrain, name='supprimer_terrain'),
    path('listes_joueurs', views.listes_joueurs, name='listes_joueurs'),
    path('supprimer_joueur/<int:joueur_id>/', views.supprimer_joueur, name='supprimer_joueur'),
    path('page_acceuil', views.page_acceuil, name='page_acceuil'),
    path('inscription', views.inscription, name='inscription'),
    path('academie', views.academie, name='academie'),
    path('ajouter_academie', views.ajouter_academie, name='ajouter_academie'),
    path('modifier_academie/<int:academie_id>/', views.modifier_academie, name='modifier_academie'),
    path('supprimer_academie/<int:academie_id>/', views.supprimer_academie, name='supprimer_academie'),
    path('', views.login, name='login'),




  
]






if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

































