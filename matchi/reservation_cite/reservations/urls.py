from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'terrains', views.TerrainViewSet, basename='terrain')

urlpatterns = [
   path('index', views.index , name='index'),
#    path('ajouter_cite', views.ajouter_cite , name='ajouter_cite'),
   path('gestion_client', views.gestion_client , name='gestion_client'),
#    path('gestion_cite', views.gestion_cite , name='gestion_cite'),
#    path('modifier_client/', views.modifier_client, name='modifier_client'),
   path('supprimer_client/', views.supprimer_client, name='supprimer_client'),
   path('ajouter_client/', views.ajouter_client, name='ajouter_client'),
#    path('modifier_cite/<int:cite_id>/', views.modifier_cite, name='modifier_cite'),
#    path('supprimer_cite/<int:cite_id>/', views.supprimer_cite, name='supprimer_cite'),
#    path('', views.page_acceuil , name='page_acceuil'),
   path('register/', views.register_client, name='register_client'),
    path('login/', views.login_client, name='login_client'),
    path('register/', views.ClientCreateView.as_view(), name='register_client'),
    path('add_terrain/', views.TerrainsCreateView.as_view(), name='add_terrain'),
    path('clients/', views.ClientListView.as_view(), name='list_clients'),
    path('get_user_info/', views.get_user_info, name='get_user_info'),
    path('get_terrain_info/<int:client_id>/', views.get_terrain_info, name='get_terrain_info'),
    path('get_all_terrains/', views.get_all_terrains, name='get_all_terrains'),
    path('', include(router.urls)),
    path('heures-disponibles/<int:client_id>/', views.heures_disponibles, name='heures_disponibles'),
    path('terrains/', views.TerrainsListView.as_view(), name='terrains-list'),
    path('terrains/<int:terrain_id>/available-schedules/', views.terrain_heures_disponibles, name='available_schedules'),
    path('joueurs/', views.JoueursListView.as_view(), name='joueurs-list'),
    path('joueurs/<int:joueur_id>/', views.joueur_detail, name='joueur_details'),
    path('faire_reservation/', views.faire_reservation, name='faire_reservation'),
    path('annuler_reservation/<int:reservation_id>/', views.annuler_reservation, name='annuler_reservation'),
    path('get_reservations/<int:joueur_id>/', views.get_reservations, name='get_reservations'),
    path('reservations/<int:joueur_id>/', views.ReservationsJoueurView.as_view(), name='reservations-joueur'),
    path('reservations/', views.list_reservations, name='joueur_reservations'),
    path('joueurs/<int:player_id>/update/', views.update_player, name='update_player'),
    path('joueurs/register/', views.JoueurCreateView.as_view(), name='joueur-register'),
    path('client/<int:client_id>/reservations/', views.client_reservations, name='client_reservations'),
    path('add-indisponibilite/', views.AddIndisponibiliteView.as_view(), name='add_indisponibilite'),
    path('wilayes/', views.WilayeList.as_view(), name='wilaye-list'),
    path('moughataas/', views.MoughataaList.as_view(), name='moughataa-list'),





    # **************************************************************************( mobile APIs)********************************************************************

    path('AddPlayer/', views.add_player, name='AddPlayer'),
    path("LoginPlayer/", views.login_joueur, name='LoginPlayer')

  
]






if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

































