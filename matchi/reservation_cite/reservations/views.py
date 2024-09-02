from django.views import View
from rest_framework.authtoken.models import Token
from datetime import date, datetime, timedelta
import re
from django.shortcuts import render, redirect, get_object_or_404
from .models import Indisponibilites, Joueurs, Reservations, Wilaye , Moughataa,Client
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView
from .serializers import ReservationSerializer
from django.views.decorators.http import require_POST
import json
import hashlib
from .serializers import WilayeSerializer
from rest_framework import generics
from .models import Wilaye, Moughataa,Academie
from .serializers import WilayeSerializer, MoughataaSerializer,AcademieSerializer

# import re
# from .models import cite as CiteModel  # Renommer l'import pour éviter les conflits de noms

def index(request):
    return render(request, 'index.html')
def ajouter_client(request):
    return render(request, 'pages/ajouter_client.html')
def gestion_client(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        numero_telephone = request.POST.get('numero_telephone')
        modepass_clair = request.POST.get('modepass_chiffre')
        modepass_chiffre = make_password(modepass_clair)
        if not re.match(r'^\d{8}$', numero_telephone):
            return redirect('gestion_client')
        new_client = Client.objects.create(
            nom=nom,
            prenom=prenom,
            numero_telephone=numero_telephone,
            modepass_chiffre=modepass_chiffre
        )
        return redirect('gestion_client')
    clients = Client.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'pages/gestion_client.html', context)
def modifier_client(request):
    client_id = request.POST.get('client_id')
    nom = request.POST.get('nom')
    prenom = request.POST.get('prenom')
    numero_telephone = request.POST.get('numero_telephone')
    modepass_chiffre = request.POST.get('modepass_chiffre', '')
    if not re.match(r'^\d{8}$', numero_telephone):
        return redirect('gestion_client')

    client = Client.objects.get(id=client_id)
    client.nom = nom
    client.prenom = prenom
    client.numero_telephone = numero_telephone
    if modepass_chiffre:
        client.modepass_chiffre = make_password(modepass_chiffre)
    client.save()
    return redirect('gestion_client')
def supprimer_client(request):
    client_id = request.POST.get('client_id')
    client = Client.objects.get(id=client_id)
    client.delete()
    return redirect('gestion_client')
  
@api_view(['GET'])
def get_user_info(request):
    client_id = request.query_params.get('client_id')
    if client_id is None:
        return Response({'error': 'Client ID non fourni'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        client = Client.objects.get(id=client_id)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Client.DoesNotExist:
        return Response({'error': 'Client non trouvé'}, status=status.HTTP_404_NOT_FOUND)
# def modifier_cite(request, cite_id):
#     cite_instance = get_object_or_404(cite, id=cite_id)

#     if request.method == 'POST':
#         cite_instance.nom = request.POST.get('nom')
#         cite_instance.longitude = request.POST.get('longitude')
#         cite_instance.latitude = request.POST.get('latitude')
#         cite_instance.client_id = request.POST.get('client')
#         cite_instance.wilaye_id = request.POST.get('Wilaye')
#         cite_instance.moughataa_id = request.POST.get('Moughataa')
#         cite_instance.ballon_disponible = request.POST.get('ballon_disponible') == 'True'
#         cite_instance.maillot_disponible = request.POST.get('maillot_disponible') == 'True'
#         cite_instance.eclairage_disponible = request.POST.get('eclairage_disponible') == 'True'
#         cite_instance.sonorisation_disponible = request.POST.get('sonorisation_disponible') == 'True'
#         cite_instance.lieu = request.POST.get('lieu')
#         cite_instance.nombre_joueur = request.POST.get('nombre_joueur')
#         cite_instance.prix_par_heure = request.POST.get('prix_par_heure')
#         if 'photo1' in request.FILES:
#              cite_instance.photo1 = request.FILES['photo1']

#         if 'photo2' in request.FILES:
#             cite_instance.photo2 = request.FILES['photo2']

#         if 'photo3' in request.FILES:
#             cite_instance.photo3 = request.FILES['photo3']

#         cite_instance.save()
#         return redirect('gestion_cite')
#     return render(request, 'modifier_cite.html', {'cite': cite_instance})



# def supprimer_cite(request, cite_id):
#     cite_instance = get_object_or_404(cite, id=cite_id)
#     if request.method == 'POST':
#         cite_instance.delete()
#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False})

# def page_acceuil(request):
#     return render(request, 'pages/page_acceuil.html')

# def ajouter_cite(request):
#     return render(request, 'pages/ajouter_cite.html')

# def gestion_cite(request):
#     clients = Client.objects.all()
#     wilayes = Wilaye.objects.all()
#     moughataa=Moughataa.objects.all()
#     cites=cite.objects.all()
#     context = {
#         'clients': clients,
#         'wilayes': wilayes,
#         'moughataa':moughataa,
#         'cites':cites,
#     }
#     if request.method == 'POST':
#         # Récupérer les données du formulaire
#         nom = request.POST.get('nom')
#         longitude = request.POST.get('longitude')
#         latitude = request.POST.get('latitude')
#         nombre_joueur = request.POST.get('nombre_joueur')
#         lieu = request.POST.get('lieu')
#         prix_par_heure = request.POST.get('prix_par_heure')
#         photo1 = request.FILES.get('photo1')
#         photo2 = request.FILES.get('photo2')
#         photo3 = request.FILES.get('photo3')
#         client_id = request.POST.get('client')
#         wilaye_id = request.POST.get('Wilaye')
#         moughataa_id = request.POST.get('Moughataa') 
#         ballon_disponible = request.POST.get('ballon_disponible')
#         maillot_disponible = request.POST.get('maillot_disponible')
#         eclairage_disponible = request.POST.get('eclairage_disponible')
#         sonorisation_disponible = request.POST.get('sonorisation_disponible')# Assurez-vous d'ajouter ce champ dans le formulaire si nécessaire
#         nouvelle_cite = cite.objects.create(
#             nom=nom,
#             longitude=longitude,
#             latitude=latitude,
#             nombre_joueur=nombre_joueur,
#             lieu=lieu,
#             prix_par_heure=prix_par_heure,
#             moughataa_id=moughataa_id,
#             wilaye_id=wilaye_id,
#             client_id=client_id,
#             photo1=photo1,
#             photo2=photo2,
#             photo3=photo3,
#             ballon_disponible=ballon_disponible,
#             maillot_disponible=maillot_disponible,
#             eclairage_disponible=eclairage_disponible,
#             sonorisation_disponible=sonorisation_disponible,
#         )
#         return redirect('/gestion_cite')
#     return render(request, 'pages/gestion_cite.html', context)

# def headerGestion_cite(request):
#     return render(request, 'pages/headerGestion_cite.html')
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Client, Terrains
from .serializers import ClientSerializer, JoueurSerializer, TerrainSerializer,ReservationSerializer
from django.contrib.auth.hashers import check_password
from rest_framework import generics

@api_view(['POST'])
def register_client(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_client(request):
    numero_telephone = request.data.get('numero_telephone')
    modepass_chiffre = request.data.get('modepass_chiffre')
    try:
        client = Client.objects.get(numero_telephone=numero_telephone)
        if check_password(modepass_chiffre, client.modepass_chiffre):
            return Response({'message': 'Login successful', 'client_id': client.id}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    except Client.DoesNotExist:
        return Response({'error': 'Client does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_player(request):
    numero_telephone = request.data.get('numero_telephone')
    password = request.data.get('password')
    nom_joueur = request.data.get('nom')
    prenom_joueur = request.data.get('prenom')
    #hashed_password = hashlib.md5(password.encode()).hexdigest()

    try:
        joueur = Joueurs.objects.create(
    nom_joueur=nom_joueur,
    prenom_joueur=prenom_joueur,
    password=password,
    numero_telephone=numero_telephone
)
        return Response({"message":"Done!"},status=201)
        # if check_password(modepass_chiffre, client.modepass_chiffre):
        #     return Response({'message': 'Login successful', 'client_id': client.id}, status=status.HTTP_200_OK)
        # else:
        #     return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    except Client.DoesNotExist:
        return Response({'error': 'Client does not exist'}, status=status.HTTP_400_BAD_REQUEST)








class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class TerrainsCreateView(generics.CreateAPIView):
    queryset = Terrains.objects.all()
    serializer_class = TerrainSerializer
class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
@api_view(['GET'])
def get_terrain_info(request, client_id):
    try:
        terrain = Terrains.objects.filter(client_id=client_id).first()
        if not terrain:
            return Response({'error': 'Terrain non trouvé'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TerrainSerializer(terrain)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['GET'])
def get_all_terrains(request):
    try:
        # Récupérer tous les terrains avec les objets liés
        terrains = Terrains.objects.all().select_related('wilaye', 'moughataa')
        terrain_list = []
        
        # Parcourir chaque terrain et construire la réponse
        for terrain in terrains:
            terrain_data = {
                'nom_fr': terrain.nom_fr,
                'nom_ar': terrain.nom_ar,
                'longitude': terrain.longitude,
                'latitude': terrain.latitude,
                'nombre_joueur': terrain.nombre_joueur,
                'lieu_fr': terrain.lieu_fr,
                'lieu_ar': terrain.lieu_ar,
                'photo1': request.build_absolute_uri(terrain.photo1.url) if terrain.photo1 else None,
                'photo2': request.build_absolute_uri(terrain.photo2.url) if terrain.photo2 else None,
                'photo3': request.build_absolute_uri(terrain.photo3.url) if terrain.photo3 else None,
                'prix_par_heure': terrain.prix_par_heure,
                'client': terrain.client.nom,  # Utiliser le nom du client au lieu de l'ID
                'wilaye_nom_fr': terrain.wilaye.nom_wilaye_fr if terrain.wilaye else None,
                'wilaye_nom_ar': terrain.wilaye.nom_wilaye_Ar if terrain.wilaye else None,
                'moughataa_nom_fr': terrain.moughataa.nom_fr if terrain.moughataa else None,
                'moughataa_nom_ar': terrain.moughataa.nom_ar if terrain.moughataa else None,
                'heure_ouverture': terrain.heure_ouverture,
                'heure_fermeture': terrain.heure_fermeture,
                'ballon_disponible': terrain.ballon_disponible,
                'maillot_disponible': terrain.maillot_disponible,
                'eclairage_disponible': terrain.eclairage_disponible,
                'siffler': terrain.siffler,
                'parking': terrain.parking,
                'eau': terrain.eau,
                'gazon_artificiel': terrain.gazon_artificiel
            }
            terrain_list.append(terrain_data)
        
        return Response(terrain_list, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class TerrainViewSet(viewsets.ModelViewSet):
    queryset = Terrains.objects.all()
    serializer_class = TerrainSerializer
@api_view(['GET'])
def heures_disponibles(request, client_id):
    try:
        client = get_object_or_404(Client, pk=client_id)
        terrains = Terrains.objects.filter(client=client)
        
        heures_disponibles = []
        
        for terrain in terrains:
            date_today = datetime.now().date()
            date_ouverture = datetime.combine(date_today, terrain.heure_ouverture)
            date_fermeture = datetime.combine(date_today, terrain.heure_fermeture)
            
            # Récupérer toutes les réservations pour ce terrain
            reservations = Reservations.objects.filter(terrain=terrain, date_reservation=date_today)
            
            # Récupérer toutes les indisponibilités pour ce terrain
            indisponibilites = Indisponibilites.objects.filter(terrain=terrain, date_indisponibilite=date_today)
            
            # Liste des heures disponibles pour ce terrain aujourd'hui
            heures_reservees = set()
            heures_indisponibles = set()
            
            for reservation in reservations:
                heures_reservees.update(range(reservation.heure_debut.hour, reservation.heure_fin.hour))
            
            for indisponibilite in indisponibilites:
                heures_indisponibles.update(range(indisponibilite.heure_debut.hour, indisponibilite.heure_fin.hour))
            
            heures_libres = sorted(list(set(range(date_ouverture.time().hour, date_fermeture.time().hour)) - heures_reservees - heures_indisponibles))
            
            heures_disponibles.append({
                'terrain': terrain.id,
                'heures_libres': heures_libres
            })
        
        return Response(heures_disponibles, status=status.HTTP_200_OK)
    
    except Client.DoesNotExist:
        return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
      
class TerrainsListView(APIView):
    def get(self, request):
        terrains = Terrains.objects.all()
        serializer = TerrainSerializer(terrains, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
@api_view(['GET'])
def terrain_heures_disponibles(request, terrain_id):
    try:
        terrain = Terrains.objects.get(pk=terrain_id)
        
        date_today = datetime.now().date()
        date_ouverture = datetime.combine(date_today, terrain.heure_ouverture)
        date_fermeture = datetime.combine(date_today, terrain.heure_fermeture)
        
        # Récupérer toutes les réservations pour ce terrain aujourd'hui
        reservations = Reservations.objects.filter(terrain=terrain, date_reservation=date_today)
        
        # Récupérer toutes les indisponibilités pour ce terrain aujourd'hui
        indisponibilites = Indisponibilites.objects.filter(terrain=terrain, date_indisponibilite=date_today)
        
        # Liste des heures réservées et indisponibles pour ce terrain aujourd'hui
        heures_reservees = set()
        heures_indisponibles = set()
        
        for reservation in reservations:
            heures_reservees.update(range(reservation.heure_debut.hour, reservation.heure_fin.hour))
        
        for indisponibilite in indisponibilites:
            heures_indisponibles.update(range(indisponibilite.heure_debut.hour, indisponibilite.heure_fin.hour))
        
        # Calcul des heures disponibles pour ce terrain aujourd'hui
        heures_libres = sorted(list(set(range(date_ouverture.time().hour, date_fermeture.time().hour)) - heures_reservees - heures_indisponibles))
        
        return Response({'terrain_id': terrain.id, 'heures_libres': heures_libres}, status=status.HTTP_200_OK)
    
    except Terrains.DoesNotExist:
        return Response({'error': 'Terrain not found'}, status=status.HTTP_404_NOT_FOUND)
      
class JoueurCreateView(APIView):
    def post(self, request):
        serializer = JoueurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class JoueursListView(generics.ListCreateAPIView):
    queryset = Joueurs.objects.filter(visible=True)

    serializer_class = JoueurSerializer

def joueur_detail(request, joueur_id):
    joueur = get_object_or_404(Joueurs, id=joueur_id)
    
    # Sérialiser les objets Wilaye et Moughataa
    wilaye_data = WilayeSerializer(joueur.wilaye).data if joueur.wilaye else None
    moughataa_data = MoughataaSerializer(joueur.moughataa).data if joueur.moughataa else None
    
    joueur_data = {
        'id': joueur.id,
        'nom_joueur': joueur.nom_joueur,
        'prenom_joueur': joueur.prenom_joueur,
        'numero_telephone': joueur.numero_telephone,
        'poste': joueur.poste,
        'age': joueur.age,
        'photo_de_profile': joueur.photo_de_profile.url if joueur.photo_de_profile else None,
        'height': joueur.height, 
        'weight': joueur.weight,
        'visible': joueur.visible,
        'wilaye': wilaye_data,  # Utiliser les données sérialisées'moughataa': moughataa_data,  # Utiliser les données sérialisées
    }

    return JsonResponse(joueur_data)
  
@api_view(['POST'])
def faire_reservation(request):
    joueur_id = request.data.get('joueur_id')
    terrain_id = request.data.get('terrain_id')
    date_reservation_str = request.data.get('date_reservation')
    heure_debut_str = request.data.get('heure_debut')
    heure_fin_str = request.data.get('heure_fin')

    joueur = get_object_or_404(Joueurs, pk=joueur_id)
    terrain = get_object_or_404(Terrains, pk=terrain_id)

    try:
        date_reservation = datetime.fromisoformat(date_reservation_str)
        heure_debut = datetime.strptime(heure_debut_str, '%H:%M:%S').time()
        heure_fin = datetime.strptime(heure_fin_str, '%H:%M:%S').time()
    except ValueError:
        return Response({'error': 'Invalid date or time format. Must be in ISO 8601 and HH:MM:SS format respectively.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create a new reservation instance
    reservation = Reservations(
        joueur=joueur,
        terrain=terrain,
        date_reservation=date_reservation.date(),
        heure_debut=heure_debut,
        heure_fin=heure_fin
    )
    reservation.save()

    return Response({'message': 'Reservation successful'}, status=status.HTTP_201_CREATED)
@api_view(['POST'])
def annuler_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservations, pk=reservation_id)
    reservation.delete()
    return Response({'success': 'Réservation annulée avec succès'}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET'])
def get_reservations(request, joueur_id):
    reservations = Reservations.objects.filter(joueur_id=joueur_id).select_related('terrain')
    data = []
    for reservation in reservations:
        data.append({
            'terrain_name': reservation.terrain.nom,
            'location': reservation.terrain.lieu,
            'date_reservation': reservation.date_reservation.isoformat(),
            'heure_debut': reservation.heure_debut.strftime('%H:%M'),
            'heure_fin': reservation.heure_fin.strftime('%H:%M'),
            'price': reservation.terrain.prix_par_heure,
            'payment_method': 'amanty',
        })
    return JsonResponse(data, safe=False)
  
class ReservationsJoueurView(APIView):

    def get(self, request, joueur_id):
        joueur = get_object_or_404(Joueurs, id=joueur_id)  # Récupérer le joueur par son ID
        
        reservations = Reservations.objects.filter(joueur=joueur)

        serializer = ReservationSerializer(reservations, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
      
@api_view(['GET'])
def joueur_reservations(request, joueur_id):
    try:
        # Récupérer les réservations pour le joueur spécifié
        reservations = Reservations.objects.filter(joueur_id=joueur_id)
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
    except Reservations.DoesNotExist:
        return Response({'error': 'Aucune réservation trouvée pour ce joueur.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      

@api_view(['POST'])
def ActiveDesactive(request, joueur_id):
    try:
        # Récupérer le joueur spécifié par son ID
        joueur = Joueurs.objects.get(id=joueur_id)  # Use 'id' if it's the primary key
        value = request.data.get('visible', joueur.visible)  # Get 'visible' from the request, default to current value
        
        # Mettre à jour la visibilité du joueur
        joueur.visible = value
        joueur.save()  # Save the changes to the database
        
        return Response({"message": "ok", "visible": joueur.visible}, status=status.HTTP_200_OK)
    
    except Joueurs.DoesNotExist:
        return Response({"error": "Player not found"}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      


@api_view(['GET'])
def list_reservations(request):
    try:
        reservations = Reservations.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['PATCH'])
def update_player(request, player_id):
    # print(request.data)
    try:
        joueur = get_object_or_404(Joueurs, pk=player_id)
        # print(request.data)
        # Utilisation de request.data pour récupérer les données JSON
        serializer = JoueurSerializer(instance=joueur, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Player updated successfully'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except Joueurs.DoesNotExist:
        return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
      

import os
from django.core.files.storage import default_storage
from django.utils.crypto import get_random_string

@api_view(['POST'])
def uploadProfileImage(request, player_id):
    try:
        # Retrieve the player instance by ID
        player = Joueurs.objects.get(pk=player_id)
        old_url = player.photo_de_profile.path

        # Delete the old image file from the server if it exists
        if os.path.exists(old_url):
            os.remove(old_url)

        # Access the uploaded file
        image = request.FILES.get('image')

        if not image:
            return Response({'error': 'No image uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate a new filename using player_id and a random string
        extension = os.path.splitext(image.name)[1]  # Get the file extension
        new_filename = f"{player_id}_{get_random_string(8)}{extension}"

        # Save the file with the new name
        image.name = new_filename
        player.photo_de_profile = image
        # player.image=new_filename
        player.save()

        return Response({'message': 'Image uploaded successfully', 'filename': new_filename}, status=status.HTTP_200_OK)
    except Joueurs.DoesNotExist:
        return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


def client_reservations(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    reservations = Reservations.objects.filter(terrain__client=client).select_related('terrain', 'joueur')
    data = []
    for reservation in reservations:
        data.append({
            'terrain': reservation.terrain.nom,
            'joueur': f'{reservation.joueur.nom_joueur} {reservation.joueur.prenom_joueur}',
            'date_reservation': reservation.date_reservation,
            'heure_debut': reservation.heure_debut,
            'heure_fin': reservation.heure_fin,
        })
    return JsonResponse(data, safe=False)
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import time  # Importez time depuis datetime
@method_decorator(csrf_exempt, name='dispatch')
class AddIndisponibiliteView(View):
    def post(self, request, *args, **kwargs):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            heure_indisponible = str(body.get('heure_indisponible'))  # Convertir en chaîne

            # Convertir heure_indisponible en objet time
            heure_debut = time.fromisoformat(heure_indisponible)

            terrain_id = body.get('terrain')

            # Exemple de création d'une nouvelle indisponibilité
            indisponibilite = Indisponibilites.objects.create(
                heure_debut=heure_debut,
                heure_fin=(heure_debut.hour + 1) % 24,  # Exemple : une heure après
                terrain_id=terrain_id
            )
            return JsonResponse({'message': 'Indisponibilité ajoutée avec succès'}, status=201)
        except ValueError as ve:
            return JsonResponse({'error': 'Valeur incorrecte pour heure_indisponible: {}'.format(str(ve))}, status=400)
        except Exception as e:
            # Temporairement utiliser raise pour voir l'erreur complète
            raise
            # return JsonResponse({'error': str(e)}, status=500)

@api_view(['POST'])
def login_joueur(request):
    numero_telephone = request.data.get('numero_telephone')
    password = request.data.get('password')
    print("tel : " ,numero_telephone)
    print("pwd : " ,password)
    
    try:
        joueur = Joueurs.objects.get(numero_telephone=numero_telephone)
        if check_password(password, joueur.password):
            response_data = {
                'id': joueur.id,
                'nom_joueur': joueur.nom_joueur,
                'prenom_joueur': joueur.prenom_joueur,
                'numero_telephone': joueur.numero_telephone,
                'poste': joueur.poste,
                'age': joueur.age,
                'height': joueur.height,
                'weight': joueur.weight,
                'photo_de_profile': joueur.photo_de_profile.url if joueur.photo_de_profile else None,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
    except Joueurs.DoesNotExist:
        return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)


class WilayeList(generics.ListAPIView):
    queryset = Wilaye.objects.all()
    serializer_class = WilayeSerializer

def get_moughataas(request, code_wilaye):
    try:
        moughataas = Moughataa.objects.filter(wilaye__code_wilaye=code_wilaye)
        moughataa_list = [
            {
                "id": moughataa.id,
                "nom_fr": moughataa.nom_fr,
                "nom_ar": moughataa.nom_ar,
                "wilaye": moughataa.wilaye.code_wilaye
            }
            for moughataa in moughataas
        ]
        return JsonResponse({"moughataas": moughataa_list}, safe=False)
    except Moughataa.DoesNotExist:
        return JsonResponse({"error": "Wilaye not found or no moughataas available"}, status=404)
# Récupérer la liste des académies
class AcademieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Academie.objects.all()
    serializer_class = AcademieSerializer


