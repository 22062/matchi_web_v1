from django.test import TestCase

# # Create your tests here.
# from django.views import View
# from rest_framework.authtoken.models import Token
# from datetime import date, datetime, timedelta
# import re
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import DemandeReservation, Indisponibilites, Joueurs, Reservations, Wilaye , Moughataa,Client
# from django.contrib.auth.hashers import make_password
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from rest_framework import viewsets
# from rest_framework.views import APIView
# from django.contrib.auth import authenticate, login
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.generics import ListAPIView
# from .serializers import DemandeReservationSerializer, ReservationSerializer
# from django.views.decorators.http import require_POST
# import json
# import hashlib
# from .serializers import WilayeSerializer,ReservationSerializer_client
# from rest_framework import generics

# from .models import Wilaye, Moughataa,Academie
# from .serializers import WilayeSerializer, MoughataaSerializer,AcademieSerializer

# from .models import Wilaye, Moughataa
# from .serializers import WilayeSerializer, MoughataaSerializer,IndisponibiliteSerializer
# from django.views.decorators.http import require_http_methods
# import requests
# import google.auth
# from google.oauth2 import service_account
# import google.auth.transport.requests


# # import re
# # from .models import cite as CiteModel  # Renommer l'import pour éviter les conflits de noms

# def index(request):
#     return render(request, 'index.html')
# def ajouter_client(request):
#     return render(request, 'pages/ajouter_client.html')
# def gestion_client(request):
#     if request.method == 'POST':
#         nom = request.POST.get('nom')
#         prenom = request.POST.get('prenom')
#         numero_telephone = request.POST.get('numero_telephone')
#         modepass_clair = request.POST.get('modepass_chiffre')
#         modepass_chiffre = make_password(modepass_clair)
#         if not re.match(r'^\d{8}$', numero_telephone):
#             return redirect('gestion_client')
#         new_client = Client.objects.create(
#             nom=nom,
#             prenom=prenom,
#             numero_telephone=numero_telephone,
#             modepass_chiffre=modepass_chiffre
#         )
#         return redirect('gestion_client')
#     clients = Client.objects.all()
#     context = {
#         'clients': clients,
#     }
#     return render(request, 'pages/gestion_client.html', context)
# def modifier_client(request):
#     # data=  data=request.data

#     client_id = request.POST.get('client_id')
#     nom = request.POST.get('nom')
#     prenom = request.POST.get('prenom')
#     numero_telephone = request.POST.get('numero_telephone')
#     modepass_chiffre = request.POST.get('modepass_chiffre', '')
#     if not re.match(r'^\d{8}$', numero_telephone):
#         return redirect('gestion_client')

#     client = Client.objects.get(id=client_id)
#     client.nom = nom
#     client.prenom = prenom
#     client.numero_telephone = numero_telephone
#     if modepass_chiffre:
#         client.modepass_chiffre = make_password(modepass_chiffre)
#     client.save()
#     return redirect('gestion_client')
# def supprimer_client(request):
#     client_id = request.POST.get('client_id')
#     client = Client.objects.get(id=client_id)
#     client.delete()
#     return redirect('gestion_client')
  
# @api_view(['GET'])
# def get_user_info(request):
#     client_id = request.query_params.get('client_id')
#     if client_id is None:
#         return Response({'error': 'Client ID non fourni'}, status=status.HTTP_400_BAD_REQUEST)
#     try:
#         client = Client.objects.get(id=client_id)
#         serializer = ClientSerializer(client)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Client.DoesNotExist:
#         return Response({'error': 'Client non trouvé'}, status=status.HTTP_404_NOT_FOUND)


# from .models import Client, Terrains
# from .serializers import ClientSerializer, JoueurSerializer, TerrainSerializer,ReservationSerializer
# from django.contrib.auth.hashers import check_password
# from rest_framework import generics
# from django.contrib.auth.hashers import make_password



# def hash_password(password: str) -> str:
#     # Utilise pbkdf2_sha256 pour hacher le mot de passe avec 720000 itérations
#     hashed_password = make_password(password, hasher='pbkdf2_sha256')
#     return hashed_password

 
# @api_view(['POST'])
# def register_client(request):
#     serializer = ClientSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def login_client(request):
#     data=request.data

#     numero_telephone =  data.get('numero_telephone')
#     modepass_chiffre =  data.get('modepass_chiffre')
#     try:
#         client = Client.objects.get(numero_telephone=numero_telephone)
#         if check_password(modepass_chiffre, client.modepass_chiffre):
#             return Response({'message': 'Login successful', 'client_id': client.id}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
#     except Client.DoesNotExist:
#         print(";;;;;;;;;;;;;;;;")
#         return Response({'error': 'Client does not exist'}, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e :
#         print("--------------------------------------------------",e)



# @api_view(['POST'])
# def getPassword(request):
#     data=request.data
#     id =  data.get('client')
#     try:
#         client = Client.objects.get(id=id)
#         print(client.modepass_chiffre)
#         mot=client.modepass_chiffre
#         return Response(mot)

#     except Exception as e :
#         print("--------------------------------------------------",e)
#         return Response("Client does not exist", status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def changePassword(request):
#     data=request.data
#     id = data.get('client')
#     pwd= data.get('pwd')
#     pwd_hash=hash_password(pwd)
#     try:
#         client = Client.objects.get(id=id)
#         client.modepass_chiffre=pwd_hash
#         client.save()
#         return Response({"message":"done"})

#     except Exception as e :
#         print("--------------------------------------------------",e)
#         return Response({"message":"error"},  status=status.HTTP_400_BAD_REQUEST)







# @api_view(['POST'])
# def add_player(request):
#     data=request.data
#     numero_telephone =data.get('numero_telephone')
#     password = data.get('password')
#     nom_joueur = data.get('nom')
#     prenom_joueur = data.get('prenom')
#     #hashed_password = hashlib.md5(password.encode()).hexdigest()

#     try:
#         joueur = Joueurs.objects.create(
#     nom_joueur=nom_joueur,
#     prenom_joueur=prenom_joueur,
#     password=password,
#     numero_telephone=numero_telephone
# )
#         return Response({"message":"Done!"},status=201)
#         # if check_password(modepass_chiffre, client.modepass_chiffre):
#         #     return Response({'message': 'Login successful', 'client_id': client.id}, status=status.HTTP_200_OK)
#         # else:
#         #     return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
#     except Client.DoesNotExist:
#         return Response({'error': 'Client does not exist'}, status=status.HTTP_400_BAD_REQUEST)








# class ClientCreateView(generics.CreateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer

# class TerrainsCreateView(generics.CreateAPIView):
#     queryset = Terrains.objects.all()
#     serializer_class = TerrainSerializer
# class ClientListView(generics.ListAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
# @api_view(['GET'])
# def get_terrain_info(request, client_id):
#     try:
#         terrain = Terrains.objects.filter(client_id=client_id).first()
#         if not terrain:
#             return Response({'error': 'Terrain non trouvé'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = TerrainSerializer(terrain)
 
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# @api_view(['GET'])
# def get_all_terrains(request):
#     try:
#         # Récupérer tous les terrains avec les objets liés
#         terrains = Terrains.objects.all().select_related('wilaye', 'moughataa')
#         terrain_list = []
        
#         # Parcourir chaque terrain et construire la réponse
#         for terrain in terrains:
#             terrain_data = {
#                 'id': terrain.id,
#                 'nom_fr': terrain.nom_fr,
#                 'nom_ar': terrain.nom_ar,
#                 'longitude': terrain.longitude,
#                 'latitude': terrain.latitude,
#                 'nombre_joueur': terrain.nombre_joueur,
#                 'lieu_fr': terrain.lieu_fr,
#                 'lieu_ar': terrain.lieu_ar,
#                 'photo1': request.build_absolute_uri(terrain.photo1.url) if terrain.photo1 else None,
#                 'photo2': request.build_absolute_uri(terrain.photo2.url) if terrain.photo2 else None,
#                 'photo3': request.build_absolute_uri(terrain.photo3.url) if terrain.photo3 else None,
#                 'prix_par_heure': terrain.prix_par_heure,
#                 'client': terrain.client.nom,  # Utiliser le nom du client au lieu de l'ID
#                 'wilaye_nom_fr': terrain.wilaye.nom_wilaye_fr if terrain.wilaye else None,
#                 'wilaye_nom_ar': terrain.wilaye.nom_wilaye_Ar if terrain.wilaye else None,
#                 'moughataa_nom_fr': terrain.moughataa.nom_fr if terrain.moughataa else None,
#                 'moughataa_nom_ar': terrain.moughataa.nom_ar if terrain.moughataa else None,
#                 'heure_ouverture': terrain.heure_ouverture,
#                 'heure_fermeture': terrain.heure_fermeture,
#                 'ballon_disponible': terrain.ballon_disponible,
#                 'maillot_disponible': terrain.maillot_disponible,
#                 'eclairage_disponible': terrain.eclairage_disponible,
#                 'siffler': terrain.siffler,
#                 'parking': terrain.parking,
#                 'eau': terrain.eau,
#                 'gazon_artificiel': terrain.gazon_artificiel
#             }
#             terrain_list.append(terrain_data)
        
#         return Response(terrain_list, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# class TerrainViewSet(viewsets.ModelViewSet):
#     queryset = Terrains.objects.all()
#     serializer_class = TerrainSerializer





# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from datetime import datetime


# @api_view(['GET'])
# def get_terrinbyclient(request, client_id):
#     try:
#         client = get_object_or_404(Client, pk=client_id)
#         terrain = Terrains.objects.filter(client=client).first()  # Filter by client, get the first match

#         if terrain is not None:
#             return Response({"id": terrain.id}, status=200)
#         else:
#             return Response({"error": "No terrain found for this client."}, status=404)

#     except Exception as e:
#         print("Exception:", e)
#         return Response({"error": str(e)}, status=400)



# @api_view(['GET'])
# def heures_disponibles(request, client_id, date):
#     try:
#         date_obj = datetime.strptime(date, '%Y-%m-%d').date()
#         client = get_object_or_404(Client, pk=client_id)
#         terrains = Terrains.objects.filter(client=client)

#         heures_disponibles = []

#         for terrain in terrains:
#             current_time = datetime.now().time()
#             heure_ouverture = terrain.heure_ouverture
#             heure_fermeture = terrain.heure_fermeture
            
#             # Debugging current time, opening, and closing time
#             print(f"Terrain: {terrain.nom_fr}")
#             print(f"Heure d'ouverture: {heure_ouverture}, Heure de fermeture: {heure_fermeture}")
#             print(f"Heure actuelle: {current_time}")

#             # Check today's date and whether hours need to be restricted based on the current time
#             if date_obj == datetime.now().date():
#                 start_hour = max(heure_ouverture.hour, current_time.hour)
#             else:
#                 start_hour = heure_ouverture.hour

#             # Handle case where closing time is after midnight
#             if heure_fermeture.hour < heure_ouverture.hour:
#                 print("Closing time is after midnight")
#                 hours_before_midnight = set(range(start_hour, 24))  # From opening to midnight
#                 hours_after_midnight = set(range(0, heure_fermeture.hour))  # From midnight to closing
#                 all_hours = hours_before_midnight.union(hours_after_midnight)
#             else:
#                 all_hours = set(range(start_hour, heure_fermeture.hour))

#             # Debugging all_hours to check the number of hours
#             print(f"Generated all_hours: {all_hours}")
#             print(f"Number of hours in all_hours: {len(all_hours)}")

#             # Add more detailed debugging if all_hours is still empty
#             if not all_hours:
#                 print("No available hours found. Debugging:")
#                 print(f"Opening hour: {heure_ouverture.hour}, Closing hour: {heure_fermeture.hour}")
#                 print(f"Start hour: {start_hour}, Current time: {current_time}")

#             heures_reservees = set()
#             heures_indisponibles = set()

#             reservations = Reservations.objects.filter(terrain=terrain, date_reservation=date_obj)
#             indisponibilites = Indisponibilites.objects.filter(terrain=terrain, date_indisponibilite=date_obj)

#             for reservation in reservations:
#                 heures_reservees.update(range(reservation.heure_debut.hour, reservation.heure_fin.hour))

#             for indisponibilite in indisponibilites:
#                 heures_indisponibles.update(range(indisponibilite.heure_debut.hour, indisponibilite.heure_fin.hour))

#             heures_libres2 = []

#             for hour in all_hours:
#                 if hour in heures_reservees:
#                     heures_libres2.append({'heure': hour, 'etat': 'reservé'})
#                 elif hour in heures_indisponibles:
#                     heures_libres2.append({'heure': hour, 'etat': 'indisponible'})
#                 else:
#                     heures_libres2.append({'heure': hour, 'etat': 'libre'})

#             heures_disponibles.append({
#                 'terrain': terrain.id,
#                 'heures_libres': heures_libres2
#             })

#         return Response(heures_disponibles, status=status.HTTP_200_OK)

#     except Exception as e:
#         print("Error : ------------- ", e)
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





# @api_view(['GET'])
# def heures_disponibles_jouers(request, terrain_id, date):
#     try:
#         date_obj = datetime.strptime(date, '%Y-%m-%d').date()
#         terrain = get_object_or_404(Terrains, pk=terrain_id)  # Récupère un seul objet Terrains

#         heures_disponibles = []
#         current_time = datetime.now().time()
#         heure_ouverture = terrain.heure_ouverture
#         heure_fermeture = terrain.heure_fermeture

#         print(f"Terrain: {terrain.nom_fr}")
#         print(f"Heure d'ouverture: {heure_ouverture}, Heure de fermeture: {heure_fermeture}")
#         print(f"Heure actuelle: {current_time}")

#         # Limite des horaires selon l'heure actuelle si c'est aujourd'hui
#         if date_obj == datetime.now().date():
#             start_hour = max(heure_ouverture.hour, current_time.hour)
#         else:
#             start_hour = heure_ouverture.hour

#         # Gestion des horaires en cas de fermeture après minuit
#         if heure_fermeture.hour < heure_ouverture.hour:
#             hours_before_midnight = set(range(start_hour, 24))
#             hours_after_midnight = set(range(0, heure_fermeture.hour))
#             all_hours = hours_before_midnight.union(hours_after_midnight)
#         else:
#             all_hours = set(range(start_hour, heure_fermeture.hour))

#         print(f"Generated all_hours: {all_hours}")
        
#         # Récupération des réservations et indisponibilités
#         heures_reservees = set()
#         heures_indisponibles = set()

#         reservations = Reservations.objects.filter(terrain=terrain, date_reservation=date_obj)
#         indisponibilites = Indisponibilites.objects.filter(terrain=terrain, date_indisponibilite=date_obj)

#         for reservation in reservations:
#             heures_reservees.update(range(reservation.heure_debut.hour, reservation.heure_fin.hour))

#         for indisponibilite in indisponibilites:
#             heures_indisponibles.update(range(indisponibilite.heure_debut.hour, indisponibilite.heure_fin.hour))

#         # Filtrer uniquement les horaires "libres"
#         heures_libres2 = [{'heure': hour, 'etat': 'libre'} for hour in all_hours if hour not in heures_reservees and hour not in heures_indisponibles]

#         heures_disponibles.append({
#             'terrain': terrain.id,
#             'heures_libres': heures_libres2
#         })

#         return Response(heures_disponibles, status=status.HTTP_200_OK)

#     except Exception as e:
#         print("Error : ------------- ", e)
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)












# class TerrainsListView(APIView):
#     def get(self, request):
#         terrains = Terrains.objects.all()
#         serializer = TerrainSerializer(terrains, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
      
# from datetime import datetime, timedelta
# from django.utils.timezone import now

# @api_view(['GET'])
# def terrain_heures_disponibles(request, terrain_id):
#     try:
#         terrain = Terrains.objects.get(pk=terrain_id)
        
#         # Récupérer la date depuis les paramètres de requête ou définir demain par défaut
#         date_str = request.GET.get('date', (datetime.now() + timedelta(days=1)).date().strftime('%Y-%m-%d'))
#         date_today = datetime.strptime(date_str, '%Y-%m-%d').date()
#         now_time = datetime.now().time()
        
#         # Définir les heures d'ouverture et de fermeture
#         ouverture = terrain.heure_ouverture
#         fermeture = terrain.heure_fermeture
        
#         # Log des heures d'ouverture et de fermeture
#         print(f"Heures d'ouverture: {ouverture}, Heures de fermeture: {fermeture}")

#         # Préparer les heures totales disponibles
#         if fermeture < ouverture:
#             # Si la fermeture est le jour suivant
#             heures_libres = set(range(ouverture.hour, 24)) | set(range(0, fermeture.hour + 1))
#         else:
#             heures_libres = set(range(ouverture.hour, fermeture.hour + 1))
        
#         # Log des heures libres initiales
#         print(f"Heures libres initiales: {heures_libres}")

#         # Récupérer toutes les réservations et indisponibilités pour ce terrain à la date spécifiée
#         reservations = Reservations.objects.filter(terrain=terrain, date_reservation=date_today)
#         indisponibilites = Indisponibilites.objects.filter(terrain=terrain, date_indisponibilite=date_today)
        
#         heures_reservees = set()
#         heures_indisponibles = set()
        
#         for reservation in reservations:
#             start_hour = reservation.heure_debut.hour
#             end_hour = reservation.heure_fin.hour
            
#             # Gérer les réservations qui chevauchent minuit
#             if reservation.heure_fin < reservation.heure_debut:
#                 end_hour += 24
            
#             # Limiter les heures réservées à l'intérieur des heures d'ouverture et de fermeture
#             start_hour = max(start_hour, ouverture.hour)
#             end_hour = min(end_hour, fermeture.hour + 1)
            
#             heures_reservees.update(range(start_hour, end_hour))
            
#             # Log des heures réservées
#             print(f"Réservation === : {start_hour} à {end_hour}")

#         for indisponibilite in indisponibilites:
#             start_hour = indisponibilite.heure_debut.hour
#             end_hour = indisponibilite.heure_fin.hour
            
#             # Gérer les indisponibilités qui chevauchent minuit
#             if indisponibilite.heure_fin < indisponibilite.heure_debut:
#                 end_hour += 24
            
#             # Limiter les heures d'indisponibilité à l'intérieur des heures d'ouverture et de fermeture
#             start_hour = max(start_hour, ouverture.hour)
#             end_hour = min(end_hour, fermeture.hour + 1)
            
#             heures_indisponibles.update(range(start_hour, end_hour))
            
#             # Log des heures d'indisponibilité
#             print(f"Indisponibilité: === {start_hour} à {end_hour}")
        
#         heures_libres -= heures_reservees
#         heures_libres -= heures_indisponibles
        
#         # Exclure les heures passées de la date actuelle
#         if date_today == datetime.now().date():
#             heures_passées = set(hour for hour in heures_libres if hour < now_time.hour)
#             heures_libres -= heures_passées
        
#         heures_libres = sorted(heures_libres)
        
#         # Log des heures libres finales
#         print(f"Heures libres finales: {heures_libres}")
        
#         return Response({'terrain_id': terrain.id, 'date': date_str, 'heures_libres': heures_libres}, status=status.HTTP_200_OK)
    
#     except Terrains.DoesNotExist:
#         return Response({'error': 'Terrain not found'}, status=status.HTTP_404_NOT_FOUND)
      
# class JoueurCreateView(APIView):
#     def post(self, request):
#         serializer = JoueurSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class JoueursListView(generics.ListCreateAPIView):
#     queryset = Joueurs.objects.filter(visible=True)

#     serializer_class = JoueurSerializer

# def joueur_detail(request, joueur_id):
#     joueur = get_object_or_404(Joueurs, id=joueur_id)
    
#     # Sérialiser les objets Wilaye et Moughataa
#     wilaye_data = WilayeSerializer(joueur.wilaye).data if joueur.wilaye else None
#     moughataa_data = MoughataaSerializer(joueur.moughataa).data if joueur.moughataa else None
    
#     joueur_data = {
#         'id': joueur.id,
#         'nom_joueur': joueur.nom_joueur,
#         'prenom_joueur': joueur.prenom_joueur,
#         'numero_telephone': joueur.numero_telephone,
#         'poste': joueur.poste,
#         'age': joueur.age,
#         'photo_de_profile': joueur.photo_de_profile.url if joueur.photo_de_profile else None,
#         'height': joueur.height, 
#         'weight': joueur.weight,
#         'visible': joueur.visible,
#         'wilaye': wilaye_data,  # Utiliser les données sérialisées'moughataa': moughataa_data,  # Utiliser les données sérialisées
#     }

#     return JsonResponse(joueur_data)
  
# @api_view(['POST'])
# def faire_reservation(request):
#     data=request.data
#     joueur_id =  data.get('joueur_id')
#     terrain_id =  data.get('terrain_id')
#     date_reservation_str = data.get('date_reservation')
#     heure_debut_str =  data.get('heure_debut')
#     heure_fin_str =  data.get('heure_fin')

#     joueur = get_object_or_404(Joueurs, pk=joueur_id)
#     terrain = get_object_or_404(Terrains, pk=terrain_id)

#     try:
#         date_reservation = datetime.fromisoformat(date_reservation_str)
#         heure_debut = datetime.strptime(heure_debut_str, '%H:%M:%S').time()
#         heure_fin = datetime.strptime(heure_fin_str, '%H:%M:%S').time()
#     except ValueError:
#         return Response({'error': 'Invalid date or time format. Must be in ISO 8601 and HH:MM:SS format respectively.'}, status=status.HTTP_400_BAD_REQUEST)

#     # Create a new reservation instance
#     reservation = Reservations(
#         joueur=joueur,
#         terrain=terrain,
#         date_reservation=date_reservation.date(),
#         heure_debut=heure_debut,
#         heure_fin=heure_fin
#     )
#     reservation.save()

#     return Response({'message': 'Reservation successful'}, status=status.HTTP_201_CREATED)
# @api_view(['POST'])
# def annuler_reservation(request, reservation_id):
#     reservation = get_object_or_404(Reservations, pk=reservation_id)
#     reservation.delete()
#     return Response({'success': 'Réservation annulée avec succès'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def get_reservations(request, joueur_id):
#     reservations = Reservations.objects.filter(joueur_id=joueur_id).select_related('terrain')
#     data = []
#     for reservation in reservations:
#         data.append({
#             'terrain_name': reservation.terrain.nom,
#             'location': reservation.terrain.lieu,
#             'date_reservation': reservation.date_reservation.isoformat(),
#             'heure_debut': reservation.heure_debut.strftime('%H:%M'),
#             'heure_fin': reservation.heure_fin.strftime('%H:%M'),
#             'price': reservation.terrain.prix_par_heure,
#             'payment_method': 'amanty',
#         })
#     return JsonResponse(data, safe=False)
  
# class ReservationsJoueurView(APIView):

#     def get(self, request, joueur_id):
#         joueur = get_object_or_404(Joueurs, id=joueur_id)  # Récupérer le joueur par son ID
        
#         reservations = Reservations.objects.filter(joueur=joueur)

#         serializer = ReservationSerializer(reservations, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)
      
# @api_view(['GET'])
# def joueur_reservations(request, joueur_id):
#     try:
#         # Récupérer les réservations pour le joueur spécifié
#         reservations = Reservations.objects.filter(joueur_id=joueur_id)
#         serializer = ReservationSerializer(reservations, many=True)
#         return Response(serializer.data)
#     except Reservations.DoesNotExist:
#         return Response({'error': 'Aucune réservation trouvée pour ce joueur.'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      

# @api_view(['POST'])
# def ActiveDesactive(request, joueur_id):
#     try:
#         # Récupérer le joueur spécifié par son ID
#         joueur = Joueurs.objects.get(id=joueur_id)  # Use 'id' if it's the primary key
#         value = request.data.get('visible', joueur.visible)  # Get 'visible' from the request, default to current value
        
#         # Mettre à jour la visibilité du joueur
#         joueur.visible = value
#         joueur.save()  # Save the changes to the database
        
#         return Response({"message": "ok", "visible": joueur.visible}, status=status.HTTP_200_OK)
    
#     except Joueurs.DoesNotExist:
#         return Response({"error": "Player not found"}, status=status.HTTP_404_NOT_FOUND)
    
#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      


# @api_view(['GET'])
# def list_reservations(request):
#     try:
#         reservations = Reservations.objects.all()
#         serializer = ReservationSerializer(reservations, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# @api_view(['PATCH'])
# def update_player(request, player_id):
#     try:
#         joueur = get_object_or_404(Joueurs, pk=player_id)

#         # Mise à jour des champs avec les données fournies dans la requête
#         if 'nom_joueur' in request.data:
#             joueur.nom_joueur = request.data['nom_joueur']
#         if 'prenom_joueur' in request.data:
#             joueur.prenom_joueur = request.data['prenom_joueur']
#         if 'numero_telephone' in request.data:
#             joueur.numero_telephone = request.data['numero_telephone']
#         if 'poste' in request.data:
#             joueur.poste = request.data['poste']
#         if 'age' in request.data:
#             joueur.age = request.data['age']
#         if 'height' in request.data:
#             joueur.height = request.data['height']
#         if 'weight' in request.data:
#             joueur.weight = request.data['weight']
#         if 'wilaye' in request.data:
#             wilaye_id = request.data['wilaye']
#             joueur.wilaye = get_object_or_404(Wilaye, pk=wilaye_id)
#         if 'moughataa' in request.data:
#             moughataa_id = request.data['moughataa']
#             joueur.moughataa = get_object_or_404(Moughataa, pk=moughataa_id)

#         # Sauvegarder les changements
#         joueur.save()

#         return Response({'message': 'Player updated successfully'}, status=status.HTTP_200_OK)

#     except Joueurs.DoesNotExist:
#         return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         print(e)
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


      

# import os
# from django.core.files.storage import default_storage
# from django.utils.crypto import get_random_string

# @api_view(['POST'])
# def uploadProfileImage(request, player_id):
#     print("Données de la requête:", request.data)
#     print("Fichiers de la requête:", request.FILES)

#     try:
#         player = Joueurs.objects.get(pk=player_id)
#         print("Joueur trouvé:", player)

#         image = request.FILES.get('photo_de_profile')
#         if image:
#             print("Image reçue:", image)
#             player.photo_de_profile = image
#             player.save()
#             print("Image enregistrée:", player.photo_de_profile.url)
#             return Response({'message': 'Image uploaded successfully'}, status=status.HTTP_200_OK)
#         else:
#             print("Erreur : image manquante")
#             return Response({'error': 'No image uploaded'}, status=status.HTTP_400_BAD_REQUEST)
#     except Joueurs.DoesNotExist:
#         print("Erreur : joueur non trouvé")
#         return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         print("Erreur :", e)
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# def client_reservations(request, client_id):
#     client = get_object_or_404(Client, id=client_id)
#     reservations = Reservations.objects.filter(terrain__client=client).select_related('terrain', 'joueur')
#     data = []
#     for reservation in reservations:
#         data.append({
#             'terrain': reservation.terrain.nom,
#             'joueur': f'{reservation.joueur.nom_joueur} {reservation.joueur.prenom_joueur}',
#             'date_reservation': reservation.date_reservation,
#             'heure_debut': reservation.heure_debut,
#             'heure_fin': reservation.heure_fin,
#         })
#     return JsonResponse(data, safe=False)
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from datetime import time  # Importez time depuis datetime
# @method_decorator(csrf_exempt, name='dispatch')
# class AddIndisponibiliteView(View):
#     def post(self, request, *args, **kwargs):
#         try:
#             body_unicode = request.body.decode('utf-8')
#             body = json.loads(body_unicode)
#             heure_indisponible = str(body.get('heure_indisponible')) 
#             date_indisponibilite = str(body.get('date_indisponibilite')) 
#             heure_fin_srt=str(body.get('heure_fin')) 
#              # Convertir en chaîne
#             print("/n /n /n ============================================", heure_indisponible)

#             # Convertir heure_indisponible en objet time
#             heure_debut = time.fromisoformat(heure_indisponible)
#             heure_fin = time.fromisoformat(heure_fin_srt)

#             terrain_id = body.get('terrain')

#             # Exemple de création d'une nouvelle indisponibilité
#             try:
#                 Indisponibilites.objects.get(heure_debut=heure_debut,terrain_id=terrain_id,date_indisponibilite=date_indisponibilite).delete()

#             except:

#                 indisponibilite = Indisponibilites.objects.create(
#                     heure_debut=heure_debut,
#                     heure_fin=heure_fin,  # Exemple : une heure après
#                     terrain_id=terrain_id,
#                     date_indisponibilite=date_indisponibilite
#                 )
#             return JsonResponse({'message': 'Indisponibilité ajoutée avec succès'}, status=201)
#         except ValueError as ve:
#             print("error : =========================== ",ve)

#             return JsonResponse({'error': 'Valeur incorrecte pour heure_indisponible: {}'.format(str(ve))}, status=400)
#         except Exception as e:
#             print("error : =========================== ",e)
#             # Temporairement utiliser raise pour voir l'erreur complète
#             raise
#             # return JsonResponse({'error': str(e)}, status=500)

# @api_view(['POST'])
# def login_joueur(request):
#     data=request.data
#     numero_telephone =  data.get('numero_telephone')
#     password =  data.get('password')
#     print("tel : " ,numero_telephone)
#     print("pwd : " ,password)
    
#     try:
#         joueur = Joueurs.objects.get(numero_telephone=numero_telephone)
#         print("pwd is ",joueur.password)
#         print(check_password(password,joueur.password))
#         if  check_password(password,joueur.password):
#             response_data = {
#                 'id': joueur.id,
#                 'nom_joueur': joueur.nom_joueur,
#                 'prenom_joueur': joueur.prenom_joueur,
#                 'numero_telephone': joueur.numero_telephone,
#                 'poste': joueur.poste,
#                 'age': joueur.age,
#                 'height': joueur.height,
#                 'weight': joueur.weight,
#                 'photo_de_profile': joueur.photo_de_profile.url if joueur.photo_de_profile else None,
#             }
#             return Response(response_data, status=status.HTTP_200_OK)
#         else:
#             print("Invalid password")
#             return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
#     except Joueurs.DoesNotExist:
#         return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)


# @api_view(['POST'])
# def DemandsCount(request):
#     data=request.data
#     client_id = data.get('client')  # Get the 'client' ID from the request
#     print("client is ",client_id)

#     try:
#         # Fetch the client
#         client = Client.objects.get(id=client_id)
        
#         # Get the first terrain for the client
#         terrain = Terrains.objects.filter(client=client).first()

#         if terrain is None:
#             return Response({'count': 0, 'error': 'No terrain found for the specified client'}, status=status.HTTP_404_NOT_FOUND)

#         # Count the number of reservations for the given terrain
#         demands_count = DemandeReservation.objects.filter(terrain=terrain,status='En attente').count()

#         return Response({'count': demands_count}, status=status.HTTP_200_OK)

#     except Client.DoesNotExist:
#         print("client not found===========")

#         return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         print("\n \n Error : ",e)
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST) 




# class WilayeList(generics.ListAPIView):
#     queryset = Wilaye.objects.all()
#     serializer_class = WilayeSerializer

# def get_moughataas(request, code_wilaye):
#     try:
#         moughataas = Moughataa.objects.filter(wilaye__code_wilaye=code_wilaye)
#         moughataa_list = [
#             {
#                 "id": moughataa.id,
#                 "nom_fr": moughataa.nom_fr,
#                 "nom_ar": moughataa.nom_ar,
#                 "wilaye": moughataa.wilaye.code_wilaye
#             }
#             for moughataa in moughataas
#         ]
#         return JsonResponse({"moughataas": moughataa_list}, safe=False)
#     except Moughataa.DoesNotExist:
#         return JsonResponse({"error": "Wilaye not found or no moughataas available"}, status=404)
# # Récupérer la liste des académies
# class AcademieListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Academie.objects.all()
#     serializer_class = AcademieSerializer
    

# @api_view(["PATCH"])
# def update_token(request):
#     try:
#         # Parse the JSON data
#         data = json.loads(request.body)
#         phone_number = data.get('numero_telephone')
#         token = data.get('fcm_token')

#         if not phone_number or not token:
#             return JsonResponse({'error': 'Numéro de téléphone ou token manquant'}, status=400)

#         # Get the client
#         try:
#             client = Client.objects.get(numero_telephone=phone_number)
#         except Client.DoesNotExist:
#             return JsonResponse({'error': 'Client non trouvé'}, status=404)

#         # Update the FCM token
#         client.fcm_token = token
#         client.save()

#         return JsonResponse({'message': 'Token mis à jour avec succès'})

#     except json.JSONDecodeError:
#         return JsonResponse({'error': 'Données JSON invalides'}, status=400)

# def get_firebase_access_token():
#     # Obtenir le chemin absolu de votre fichier JSON
#     service_account_file = os.path.join(os.path.dirname(__file__), './matchinotfications-33aff4839dff.json')

#     try:
#         # Charger les informations d'identification du fichier JSON
#         credentials = service_account.Credentials.from_service_account_file(
#             service_account_file,
#             scopes=['https://www.googleapis.com/auth/firebase.messaging']
#         )

#         # Récupérer un token d'accès
#         request = google.auth.transport.requests.Request()
#         credentials.refresh(request)
#         access_token = credentials.token

#         print(f"Access Token: {access_token}")
#         return access_token

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None

# @api_view(['POST'])
# def create_reservation_request(request):
#     data=request.data
#     joueur_id =  data.get('joueur_id')
#     terrain_id = data.get('terrain_id')
#     date_reservation = data.get('date_reservation')
#     heure_debut = data.get('heure_debut')
#     heure_fin = data.get('heure_fin')

#     try:
#         joueur = Joueurs.objects.get(id=joueur_id)
#         terrain = Terrains.objects.get(id=terrain_id)

#         demande = DemandeReservation(
#             joueur=joueur,
#             terrain=terrain,
#             date_reservation=date_reservation,
#             heure_debut=heure_debut,
#             heure_fin=heure_fin
#         )
#         demande.save()

#         # Envoyer une notification au client après la création de la demande
#         send_notification_to_client(terrain.client.fcm_token, joueur.nom_joueur, terrain.nom_fr)

#         return Response({'message': 'Demande de réservation créée avec succès.'}, status=status.HTTP_201_CREATED)
#     except Joueurs.DoesNotExist:
#         return Response({'error': 'Joueur non trouvé.'}, status=status.HTTP_404_NOT_FOUND)
#     except Terrains.DoesNotExist:
#         return Response({'error': 'Terrain non trouvé.'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# def send_notification_to_client(fcm_token, joueur_name, terrain_name):
#     """
#     Envoie une notification au client via Firebase Cloud Messaging.
#     """
#     if not fcm_token:
#         print("FCM token manquant, notification non envoyée.")
#         return

#     access_token = get_firebase_access_token()
#     headers = {
#         'Authorization': f'Bearer {access_token}',
#         'Content-Type': 'application/json; UTF-8',
#     }

#     # Payload de la notification
#     notification = {
#         "message": {
#             "token": fcm_token,
#             "notification": {
#                 "title": "Nouvelle demande de réservation",
#                 "body": f"Le joueur {joueur_name} a demandé à réserver le terrain {terrain_name}."
#             },
#             "data": {
#                 "type": "reservation",
#                 "joueur_name": joueur_name,
#                 "terrain_name": terrain_name
#             }
#         }
#     }

#     project_id = 'matchinotfications'
#     url = f'https://fcm.googleapis.com/v1/projects/{project_id}/messages:send'

#     # Envoi de la requête
#     response = requests.post(url, headers=headers, json=notification)
#     if response.status_code == 200:
#         print("Notification envoyée avec succès au client.")
#     else:
#         print(f"Échec de l'envoi de la notification: {response.status_code} - {response.text}")
# class DemandeReservationClientView(APIView):
#     def get(self, request, client_id):
#         # Récupérer le client basé sur l'ID fourni
#         client = get_object_or_404(Client, id=client_id)
        
#         # Récupérer toutes les demandes de réservation pour les terrains du client
#         demandes = DemandeReservation.objects.filter(terrain__client=client)
        
#         # Sérialiser les données
#         serializer = DemandeReservationSerializer(demandes, many=True)
        
#         # Retourner les données sérialisées
#         return Response(serializer.data, status=status.HTTP_200_OK)
# @csrf_exempt
# def update_fcm_token_joueur(request, joueur_id):
#     if request.method == 'PATCH':  # Utiliser PATCH au lieu de POST
#         try:
#             data = json.loads(request.body)
#             fcm_token = data.get('fcm_token')  # Récupérer le token FCM dans le corps de la requête

#             # Récupérer le joueur correspondant à l'ID
#             joueur = Joueurs.objects.filter(id=joueur_id).first()

#             if joueur:
#                 # Mettre à jour le token FCM
#                 joueur.fcm_tokenjoueur = fcm_token
#                 joueur.save()

#                 return JsonResponse({'message': 'FCM token updated successfully'}, status=200)
#             else:
#                 return JsonResponse({'error': 'Joueur not found'}, status=404)

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'message': 'Only PATCH requests are allowed'}, status=405)

# @csrf_exempt
# @require_http_methods(["PATCH"])
# def update_reservation_status(request, reservation_id):
#     try:
#         # Récupérer la demande de réservation
#         demande = DemandeReservation.objects.get(id=reservation_id)
#         body_unicode = request.body.decode('utf-8')
#         body_data = json.loads(body_unicode)
#         new_status = body_data.get('status', None)

#         # Vérifier que le statut est valide
#         if new_status in ['En attente', 'Acceptée', 'Refusée']:
#             demande.status = new_status
#             demande.save()

#             # Si le statut est "Acceptée", ajouter une réservation et réduire le crédit du client
#             if new_status == 'Acceptée':
#                 joueur = demande.joueur
#                 terrain = demande.terrain
#                 date_reservation = demande.date_reservation
#                 heure_debut = demande.heure_debut
#                 heure_fin = demande.heure_fin

#                 # Créer une nouvelle réservation
#                 reservation = Reservations(
#                     joueur=joueur,
#                     terrain=terrain,
#                     date_reservation=date_reservation,
#                     heure_debut=heure_debut,
#                     heure_fin=heure_fin
#                 )
#                 reservation.save()

#                 # Réduire le crédit du propriétaire du terrain (client)
#                 client = terrain.client
#                 reduction = terrain.prix_par_heure * 0.10
#                 client.credie -= int(reduction)
#                 client.save()

#             # Envoyer une notification au joueur en fonction du nouveau statut
#             send_notification_to_joueur(demande.joueur.fcm_tokenjoueur, new_status, demande.terrain.nom_fr)

#             return JsonResponse({'message': 'Statut de la demande mis à jour avec succès'}, status=200)
#         else:
#             return JsonResponse({'error': 'Statut invalide'}, status=400)

#     except DemandeReservation.DoesNotExist:
#         return JsonResponse({'error': 'Demande de réservation non trouvée'}, status=404)

# def send_notification_to_joueur(fcm_token, status, terrain_name):
#     """
#     Envoie une notification au joueur via Firebase Cloud Messaging.
#     """
#     if not fcm_token:
#         print("FCM token manquant, notification non envoyée.")
#         return

#     access_token = get_firebase_access_token()
#     headers = {
#         'Authorization': f'Bearer {access_token}',
#         'Content-Type': 'application/json; UTF-8',
#     }

#     # Corps de la notification
#     body_message = f"Votre demande pour le terrain {terrain_name} a été {status.lower()}."
#     notification = {
#         "message": {
#             "token": fcm_token,
#             "notification": {
#                 "title": "Mise à jour de votre réservation",
#                 "body": body_message
#             },
#             "data": {
#                 "type": "reservation_status_update",
#                 "status": status,
#                 "terrain_name": terrain_name
#             }
#         }
#     }

#     project_id = 'matchinotfications'
#     url = f'https://fcm.googleapis.com/v1/projects/{project_id}/messages:send'

#     # Envoi de la requête
#     response = requests.post(url, headers=headers, json=notification)
#     if response.status_code == 200:
#         print("Notification envoyée avec succès au joueur.")
#     else:
#         print(f"Échec de l'envoi de la notification: {response.status_code} - {response.text}")

# def nombre_reservations_confirmees(request, client_id):
#     try:
#         # Récupérer le client
#         client = Client.objects.get(id=client_id)
        
#         # Compter les demandes de réservation confirmées ("Acceptée")
#         demandes_confirmees = DemandeReservation.objects.filter(terrain__client=client, status="Acceptée").count()
        
#         # Retourner la réponse sous forme de JSON
#         return JsonResponse({
#             'client_id': client.id,
#             'client_nom': client.nom,
#             'demandes_confirmees': demandes_confirmees
#         })
    
#     except Client.DoesNotExist:
#         return JsonResponse({'error': 'Client non trouvé'}, status=404)

# @api_view(['GET'])
# def heures_disponibles_for_player(request, terrain_id, date):
#     try:
#         # Convertir la date en objet date
#         date_obj = datetime.strptime(date, '%Y-%m-%d').date()
#         # Récupérer le terrain à partir de l'ID
#         terrain = get_object_or_404(Terrains, pk=terrain_id)

#         heures_disponibles = []
#         current_time = datetime.now().time()
#         heure_ouverture = terrain.heure_ouverture
#         heure_fermeture = terrain.heure_fermeture

#         # Debugging current time, opening, and closing time
#         print(f"Terrain: {terrain.nom_fr}")
#         print(f"Heure d'ouverture: {heure_ouverture}, Heure de fermeture: {heure_fermeture}")
#         print(f"Heure actuelle: {current_time}")

#         # Vérification de la date actuelle et restriction des heures basées sur l'heure actuelle
#         if date_obj == datetime.now().date():
#             # Démarrer à l'heure actuelle si elle est après l'heure d'ouverture
#             start_hour = max(heure_ouverture.hour, current_time.hour + (current_time.minute > 0))
#         else:
#             start_hour = heure_ouverture.hour

#         # Gestion du cas où l'heure de fermeture est après minuit
#         if heure_fermeture.hour < heure_ouverture.hour:
#             print("Closing time is after midnight")
#             hours_before_midnight = set(range(start_hour, 24))  # From opening to midnight
#             hours_after_midnight = set(range(0, heure_fermeture.hour))  # From midnight to closing
#             all_hours = hours_before_midnight.union(hours_after_midnight)
#         else:
#             all_hours = set(range(start_hour, heure_fermeture.hour))

#         # Exclure l'heure actuelle si c'est le jour même
#         if date_obj == datetime.now().date():
#             all_hours.discard(current_time.hour)

#         # Debugging all_hours to check the number of hours
#         print(f"Generated all_hours: {all_hours}")
#         print(f"Number of hours in all_hours: {len(all_hours)}")

#         heures_reservees = set()
#         heures_indisponibles = set()

#         # Récupérer les réservations et les indisponibilités pour le terrain et la date spécifiée
#         reservations = Reservations.objects.filter(terrain=terrain, date_reservation=date_obj)
#         indisponibilites = Indisponibilites.objects.filter(terrain=terrain, date_indisponibilite=date_obj)

#         # Enregistrer les heures réservées
#         for reservation in reservations:
#             heures_reservees.update(range(reservation.heure_debut.hour, reservation.heure_fin.hour))

#         # Enregistrer les heures indisponibles
#         for indisponibilite in indisponibilites:
#             heures_indisponibles.update(range(indisponibilite.heure_debut.hour, indisponibilite.heure_fin.hour))

#         heures_libres2 = []

#         # Vérifier chaque heure pour déterminer son état
#         for hour in all_hours:
#             if hour in heures_reservees:
#                 heures_libres2.append({'heure': hour, 'etat': 'reservé'})
#             elif hour in heures_indisponibles:
#                 heures_libres2.append({'heure': hour, 'etat': 'indisponible'})
#             else:
#                 heures_libres2.append({'heure': hour, 'etat': 'libre'})

#         # Ajouter les résultats à la liste des heures disponibles
#         heures_disponibles.append({
#             'terrain': terrain.id,
#             'heures_libres': heures_libres2
#         })

#         return Response(heures_disponibles, status=status.HTTP_200_OK)

#     except Exception as e:
#         print("Error : ------------- ", e)
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# def get_reservations_par_joueur(request, joueur_id):
#     joueur = get_object_or_404(Joueurs, id=joueur_id)
#     reservations = Reservations.objects.filter(joueur=joueur)
    
#     reservations_data = [
#         {
#             'terrain_Ar': reservation.terrain.nom_ar,
#             'terrain_fr':reservation.terrain.nom_fr,
#              'lieu_Ar':reservation.terrain.lieu_ar,
#              'lieu_fr':reservation.terrain.lieu_fr,
#              'prix':reservation.terrain.prix_par_heure,
#             'date_reservation': reservation.date_reservation,
#             'heure_debut': reservation.heure_debut,
#             'heure_fin': reservation.heure_fin
#         }
#         for reservation in reservations
#     ]
    
#     return JsonResponse({'joueur': joueur.nom_joueur, 'reservations': reservations_data})
  
# class ClientReservationsView(APIView):
#     def get(self, request, client_id):
#         try:
#             client = Client.objects.get(id=client_id)
#             reservations = Reservations.objects.filter(terrain__client=client)
#             serializer = ReservationSerializer_client(reservations, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Client.DoesNotExist:
#             return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)

# class DeletePlayerView(APIView):
#   # Assurez-vous que l'utilisateur est authentifié

#     def delete(self, request, player_id):
#         try:
#             player = Joueurs.objects.get(id=player_id)
#             player.delete()
#             return Response({"message": "Joueur supprimé avec succès."}, status=status.HTTP_204_NO_CONTENT)
#         except Joueurs.DoesNotExist:
#             return Response({"error": "Joueur non trouvé."}, status=status.HTTP_404_NOT_FOUND)

# class DemandeReservationViewSet(viewsets.ViewSet):
#     def list(self, request, joueur_id=None):
#         # Récupérer les demandes de réservation acceptées pour un joueur
#         demandes = DemandeReservation.objects.filter(joueur_id=joueur_id, status='Acceptée').order_by('-date_demande')
        
#         # Créer une liste de dictionnaires pour les demandes
#         demandes_data = []
#         for demande in demandes:
#             demandes_data.append({
#                 'id': demande.id,
#                 'terrain_ar': demande.terrain.nom_ar,
#                 'terrain_fr': demande.terrain.nom_fr,
#                 # ou utilisez d'autres champs que vous souhaitez afficher
#                 'joueur': demande.joueur.id,
#                 'date_reservation': demande.date_reservation.isoformat(),
#                 'heure_debut': demande.heure_debut.strftime('%H:%M'),
#                 'heure_fin': demande.heure_fin.strftime('%H:%M'),
#                 'status': demande.status,
#                 'date_demande': demande.date_demande.isoformat(),
#                 'read': demande.read
#             })

#         return JsonResponse(demandes_data, safe=False)

#     def mark_as_read(self, request, pk=None):
#         # Marquer une demande comme lue
#         try:
#             demande = DemandeReservation.objects.get(pk=pk)
#             demande.read = True
#             demande.save()
#             return JsonResponse({'status': 'Demande marquée comme lue'})
#         except DemandeReservation.DoesNotExist:
#             return JsonResponse({'error': 'Demande non trouvée'}, status=404)


