from django.contrib import admin
from django.urls import include, path
from . import mobile,views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'terrains', views.TerrainViewSet, basename='terrain')

urlpatterns = [
   path('index', mobile.index , name='index'),
#    path('ajouter_cite', mobile.ajouter_cite , name='ajouter_cite'),
   path('gestion_client', mobile.gestion_client , name='gestion_client'),
#    path('gestion_cite', mobile.gestion_cite , name='gestion_cite'),
#    path('modifier_client/', mobile.modifier_client, name='modifier_client'),
   path('supprimer_client/', mobile.supprimer_client, name='supprimer_client'),
   path('ajouter_client/', mobile.ajouter_client, name='ajouter_client'),
#    path('modifier_cite/<int:cite_id>/', mobile.modifier_cite, name='modifier_cite'),
#    path('supprimer_cite/<int:cite_id>/', mobile.supprimer_cite, name='supprimer_cite'),
#    path('', mobile.page_acceuil , name='page_acceuil'),
    path('register/', mobile.register_client, name='register_client'),
    path('login/', mobile.login_client, name='login_client'),
    path('getPassword/', mobile.getPassword, name='getPassword'),
    path('changePassword/', mobile.changePassword, name='changePassword'),
    
    path('registerr/', mobile.ClientCreateView.as_view(), name='register_client'),
    path('add_terrain/', mobile.TerrainsCreateView.as_view(), name='add_terrain'),
    path('clients/', mobile.ClientListView.as_view(), name='list_clients'),
    path('get_user_info/', mobile.get_user_info, name='get_user_info'),
    path('get_terrain_info/<int:client_id>/', mobile.get_terrain_info, name='get_terrain_info'),
    path('get_all_terrains/', mobile.get_all_terrains, name='get_all_terrains'),
    path('', include(router.urls)),
    path('heures-disponibles/<int:client_id>/<str:date>/', mobile.heures_disponibles, name='heures_disponibles'),
    path('terrains/', mobile.TerrainsListView.as_view(), name='terrains-list'),
    path('terrains/<int:terrain_id>/available-schedules/', mobile.terrain_heures_disponibles, name='available_schedules'),
    path('joueurs/', mobile.JoueursListView.as_view(), name='joueurs-list'),
    path('joueurs/<int:joueur_id>/', mobile.joueur_detail, name='joueur_details'),
    path('faire_reservation/', mobile.faire_reservation, name='faire_reservation'),
    path('annuler_reservation/<int:reservation_id>/', mobile.annuler_reservation, name='annuler_reservation'),
    path('get_reservations/<int:joueur_id>/', mobile.get_reservations, name='get_reservations'),

    path('joueurs/<int:player_id>/update/', mobile.update_player, name='update_player'),
    path('joueurs/<int:player_id>/uploadProfileImage/', mobile.uploadProfileImage, name='uploadProfileImage'),
    # /joueurs/$playerId/uploadProfileImage/
    path('joueurs/register/', mobile.JoueurCreateView.as_view(), name='joueur-register'),
    path('client/<int:client_id>/reservations/', mobile.client_reservations, name='client_reservations'),
    path('add-indisponibilite/', mobile.AddIndisponibiliteView.as_view(), name='add_indisponibilite'),
    path('wilayes/', mobile.WilayeList.as_view(), name='wilaye-list'),
    path('moughataas/<int:code_wilaye>/', mobile.get_moughataas, name='get_moughataas'),
    path('ActiveDesactive/<int:joueur_id>/', mobile.ActiveDesactive, name='ActiveDesactive'),
    path('academies/', mobile.AcademieListCreateAPIView.as_view(), name='academie-list-create'),







    # **************************************************************************( mobile APIs)********************************************************************

    path('AddPlayer/', mobile.add_player, name='AddPlayer'),
    path("LoginPlayer/", mobile.login_joueur, name='LoginPlayer'),
    path('update-token/', mobile.update_token, name='update_token'),
    path('create_reservation_request/', mobile.create_reservation_request, name='create_reservation_request'),
    path('client/<int:client_id>/demandes-reservation/', mobile.DemandeReservationClientView.as_view(), name='demandes-reservation-client'),
    path('updateFCMToken_joueur/<int:joueur_id>/', mobile.update_fcm_token_joueur, name='update_fcm_token_joueur'),
    path('reservations/<int:reservation_id>/', mobile.update_reservation_status, name='update_reservation_status'),
    path('client/<int:client_id>/reservations_confirmees/', mobile.nombre_reservations_confirmees, name='reservations_confirmees'),
    path('DemandsCount', mobile.DemandsCount, name='/DemandsCount'),
    
]

  







if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

































