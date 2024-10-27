
from django.views import View
from rest_framework.authtoken.models import Token
from datetime import date, datetime, time, timedelta
from django.db.models import Count
import re
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from .models import Indisponibilites, Joueurs, Reservations, Wilaye , Moughataa,Client,Academie,Inscription
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.http import HttpResponse
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

from .models import Wilaye, Moughataa,Academie,Terrains
from .serializers import WilayeSerializer, MoughataaSerializer,AcademieSerializer

from .models import Wilaye, Moughataa
from .serializers import WilayeSerializer, MoughataaSerializer,IndisponibiliteSerializer
from django.views.decorators.http import require_http_methods


# import re
# from .models import cite as CiteModel  # Renommer l'import pour éviter les conflits de noms

def index(request):
    return render(request, 'index.html')

def inscription(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        mot_de_passe = request.POST.get('pwd')
        confPwd = request.POST.get('confPwd')
        if mot_de_passe == confPwd:
            hashed_password = make_password(mot_de_passe)
            inscription = Inscription(login=login, mot_de_passe=hashed_password, confPwd=hashed_password)
            inscription.save()
            return redirect('login')
        else:
            pass
    return render(request, 'pages/signup.html')

def login(request):
    if request.method == 'POST':
        login_value = request.POST.get('login')
        mot_de_passe = request.POST.get('pwd')
        
        try:
            inscription = Inscription.objects.get(login=login_value)
            if check_password(mot_de_passe, inscription.mot_de_passe):
                return redirect('page_acceuil')
            else:
                error_message = "Login or password is incorrect."
                return render(request, 'pages/login.html', {'error_message': error_message})
        
        except Inscription.DoesNotExist:
            error_message = "Login or password is incorrect."
            return render(request, 'pages/login.html', {'error_message': error_message})
    return render(request, 'pages/login.html')


def ajouter_client(request):
    return render(request, 'pages/ajouter_client.html')

def gestion_client(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        credie = request.POST.get('credie')
        numero_telephone = request.POST.get('numero_telephone')
        modepass_clair = request.POST.get('modepass_chiffre')
        modepass_chiffre = make_password(modepass_clair)

        if not re.match(r'^\d{8}$', numero_telephone):
            messages.error(request, "Le numéro de téléphone doit comporter 8 chiffres.")
            return redirect('gestion_client')
        
        if Client.objects.filter(numero_telephone=numero_telephone).exists():
            messages.error(request, "Un client avec ce numéro de téléphone existe déjà.")
            return redirect('gestion_client')

        try:
            new_client = Client.objects.create(
                nom=nom,
                prenom=prenom,
                credie=credie,
                numero_telephone=numero_telephone,
                modepass_chiffre=modepass_chiffre
            )
        except Exception as e:
            messages.error(request, f"Erreur lors de l'ajout du client : {e}")
        
        return redirect('gestion_client')
    
    clients = Client.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'pages/gestion_client.html', context)


def modifier_client(request):
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        credie = request.POST.get('credie')
        numero_telephone = request.POST.get('numero_telephone')
        modepass_chiffre = request.POST.get('modepass_chiffre', '')

        # Validation du numéro de téléphone
        if not re.match(r'^\d{8}$', numero_telephone):
            return JsonResponse({'error': 'Le numéro de téléphone doit comporter 8 chiffres.'}, status=400)

        try:
            client = Client.objects.get(id=client_id)
            client.nom = nom
            client.prenom = prenom
            client.credie = credie
            client.numero_telephone = numero_telephone
            
            if modepass_chiffre:
                client.modepass_chiffre = make_password(modepass_chiffre)
            
            client.save()
            return JsonResponse({'success': 'Le client a été modifié avec succès.'}, status=200)
        except Client.DoesNotExist:
            return JsonResponse({'error': 'Le client spécifié n\'existe pas.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Requête invalide'}, status=400)


def supprimer_client(request):
    client_id = request.POST.get('client_id')
    client = Client.objects.get(id=client_id)
    client.delete()
    return redirect('gestion_client')

def modifier_terrain(request, terrain_id):
    terrain_instance = get_object_or_404(Terrains, id=terrain_id)
    
    if request.method == 'POST':
        terrain_instance.nom_fr = request.POST.get('nom_fr')
        terrain_instance.nom_ar = request.POST.get('nom_ar')
        
        terrain_instance.longitude = request.POST.get('longitude')
        terrain_instance.latitude = request.POST.get('latitude')
        client_numero_telephone = request.POST.get('client')

        try:
            client = Client.objects.get(numero_telephone=client_numero_telephone)
            if client != terrain_instance.client:
                if Terrains.objects.filter(client=client).exists():
                    messages.error(request, "Ce client a déjà enregistré un terrain.")
                    return redirect('gestion_terrain')
            terrain_instance.client = client
        except Client.DoesNotExist:
            messages.error(request, " Client avec ce numéro de téléphone n existe pas.")
            return redirect('gestion_terrain')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('gestion_terrain')
        
        terrain_instance.wilaye_id = request.POST.get('Wilaye')
        terrain_instance.moughataa_id = request.POST.get('Moughataa')
        terrain_instance.ballon_disponible = request.POST.get('ballon_disponible') == 'True'
        terrain_instance.gazon_artificiel = request.POST.get('gazon_artificiel') == 'True'
        terrain_instance.parking = request.POST.get('parking') == 'True'
        terrain_instance.siffler = request.POST.get('siffler') == 'True'
        terrain_instance.eau = request.POST.get('eau') == 'True'
        
        terrain_instance.maillot_disponible = request.POST.get('maillot_disponible') == 'True'
        terrain_instance.eclairage_disponible = request.POST.get('eclairage_disponible') == 'True'
        terrain_instance.sonorisation_disponible = request.POST.get('sonorisation_disponible') == 'True'
        terrain_instance.lieu_fr = request.POST.get('lieu_fr')
        terrain_instance.lieu_ar = request.POST.get('lieu_ar')
        
        terrain_instance.nombre_joueur = request.POST.get('nombre_joueur')
        terrain_instance.prix_par_heure = request.POST.get('prix_par_heure')
        
        try:
            # Validation du format de l'heure
            if 'heure_ouverture' in request.POST and request.POST['heure_ouverture']:
                terrain_instance.heure_ouverture = time.fromisoformat(request.POST['heure_ouverture'])
            
            if 'heure_fermeture' in request.POST and request.POST['heure_fermeture']:
                terrain_instance.heure_fermeture = time.fromisoformat(request.POST['heure_fermeture'])
            
        except ValueError:
            messages.error(request, "Le format de l'heure est incorrect. Utilisez HH:MM.")
            return redirect('modifier_terrain', terrain_id=terrain_id)

        if 'photo1' in request.FILES:
            terrain_instance.photo1 = request.FILES['photo1']
        if 'photo2' in request.FILES:
            terrain_instance.photo2 = request.FILES['photo2']
        if 'photo3' in request.FILES:
            terrain_instance.photo3 = request.FILES['photo3']
        
        try:
            terrain_instance.save()
        except Exception as e:
            messages.error(request, str(e))
            return redirect('gestion_terrain')
        
        return redirect('gestion_terrain')

    return render(request, 'pages/modifier_terrain.html', {
        'terrain': terrain_instance,
        'wilayes': Wilaye.objects.all(),
        'moughataa': Moughataa.objects.all(),
    })


def supprimer_terrain(request, terrain_id):
    terrain_instance = get_object_or_404(Terrains, id=terrain_id)
    if request.method == 'POST':
        terrain_instance.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def page_acceuil(request):
    nombre_clients = Client.objects.count()
    nombre_jouers = Joueurs.objects.count()
    nombre_terrains = Terrains.objects.count()
    nombre_de_reservation_par_client=Reservations.objects.values(
        'terrain__client__numero_telephone'
    ).annotate(nombre=Count('id'))
    # Group by client and date_reservation
    Reservations_par_Client = Reservations.objects.values(
        'terrain__client__numero_telephone', 'date_reservation'
    ).annotate(nombre=Count('id'))

    Reservations_par_Client_list = list(Reservations_par_Client)

    # Convert date_reservation to string
    for reservation in Reservations_par_Client_list:
        reservation['date_reservation'] = reservation['date_reservation'].strftime('%Y-%m-%d')

    Reservations_par_Client_json = json.dumps(Reservations_par_Client_list)

    terrains_par_wilaya = list(Terrains.objects.values('wilaye').annotate(nombre=Count('id')))
    
    # Convert to JSON
    terrains_par_wilaya_json = json.dumps(terrains_par_wilaya)
    
    return render(request, 'pages/page_acceuil.html', {
        'nombre_clients': nombre_clients,
        'nombre_jouers': nombre_jouers,
        'nombre_de_reservation_par_client':nombre_de_reservation_par_client,
        'nombre_terrains': nombre_terrains,
        'terrains_par_wilaya_json': terrains_par_wilaya_json,
        'Reservations_par_Client_json': Reservations_par_Client_json
    })
def ajouter_terrain(request):
    return render(request, 'pages/ajouter_terrain.html')

def gestion_terrain(request):
    clients = Client.objects.all()
    wilayes = Wilaye.objects.all()
    moughataa = Moughataa.objects.all()
    terrains = Terrains.objects.all()
    context = {
        'clients': clients,
        'wilayes': wilayes,
        'moughataa': moughataa,
        'terrains': terrains,
    }
    
    if request.method == 'POST':
        nom_fr = request.POST.get('nom_fr')
        nom_ar = request.POST.get('nom_ar')
        lieu_ar = request.POST.get(' lieu_ar')
        lieu_fr = request.POST.get('lieu_fr')
        
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        nombre_joueur = request.POST.get('nombre_joueur')
        prix_par_heure = request.POST.get('prix_par_heure')
        photo1 = request.FILES.get('photo1')
        photo2 = request.FILES.get('photo2')
        photo3 = request.FILES.get('photo3')
        client_telephone = request.POST.get('client')
        heure_ouverture = request.POST.get('heure_ouverture')
        heure_fermeture = request.POST.get('heure_fermeture')
        wilaye_id = request.POST.get('Wilaye')
        moughataa_id = request.POST.get('Moughataa')
        ballon_disponible = request.POST.get('ballon_disponible') == 'True'
        maillot_disponible = request.POST.get('maillot_disponible') == 'True'
        eclairage_disponible = request.POST.get('eclairage_disponible') == 'True'
        eau = request.POST.get('eau') == 'True'
        gazon_artificiel = request.POST.get('gazon_artificiel') == 'True'
        parking = request.POST.get('parking') == 'True'
        siffler = request.POST.get('siffler') == 'True'
        
        # Validation des coordonnées
        try:
            longitude = float(longitude)
            latitude = float(latitude)
        except ValueError:
            messages.error(request, "Les coordonnées doivent être des nombres valides.")
            return redirect('gestion_terrain')
        
        # Validation du nombre de joueurs et du prix par heure
        try:
            nombre_joueur = int(nombre_joueur)
            prix_par_heure = int(prix_par_heure)
        except ValueError:
            messages.error(request, "Le nombre de joueurs et le prix par heure doivent être des nombres valides.")
            return redirect('gestion_terrain')
        
        try:
            client = Client.objects.get(numero_telephone=client_telephone)
        except Client.DoesNotExist:
            messages.error(request, "Client avec ce numéro de téléphone n'existe pas.")
            return redirect('gestion_terrain')
        
        # Vérification si le client a déjà enregistré un terrain
        if Terrains.objects.filter(client=client).exists():
            messages.error(request, "Ce client a déjà enregistré un terrain.")
            return redirect('gestion_terrain')
        
        try:
            nouveau_terrain = Terrains.objects.create(
                nom_fr=nom_fr,
                nom_ar=nom_ar,
                lieu_fr=lieu_fr,
                lieu_ar=lieu_ar,
                longitude=longitude,
                latitude=latitude,
                nombre_joueur=nombre_joueur,
                prix_par_heure=prix_par_heure,
                moughataa_id=moughataa_id,
                wilaye_id=wilaye_id,
                client=client,
                photo1=photo1,
                photo2=photo2,
                photo3=photo3,
                ballon_disponible=ballon_disponible,
                maillot_disponible=maillot_disponible,
                eclairage_disponible=eclairage_disponible,
                eau=eau,
                gazon_artificiel=gazon_artificiel,
                parking=parking,
                siffler=siffler,
                heure_ouverture=heure_ouverture,
                heure_fermeture=heure_fermeture,
            )
            messages.success(request, "Terrain ajouté avec succès.")
            return redirect('gestion_terrain')
        except IntegrityError:
            messages.error(request, "Erreur d'intégrité : le terrain ne peut pas être ajouté.")
            return redirect('gestion_terrain')
    
    return render(request, 'pages/gestion_terrain.html', context)

def headerGestion_terrain(request):
    return render(request, 'pages/headerGestion_terrain.html')

def listes_joueurs(request):
    joueurs = Joueurs.objects.all()
    return render(request, 'pages/listes_joueurs.html',{'joueurs': joueurs})

def supprimer_joueur(request, joueur_id):
    joueur = get_object_or_404(Joueurs, id=joueur_id)
    joueur.delete()
    return redirect(listes_joueurs)
def academie(request):
    wilayes = Wilaye.objects.all()
    moughataa = Moughataa.objects.all() 
    academies=Academie.objects.all()

    if request.method == 'POST':
        nom_fr = request.POST['nom_fr']
        nom_ar = request.POST['nom_ar']
        lieu_fr = request.POST['lieu_fr']
        lieu_ar = request.POST['lieu_ar']
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']
        wilaye_id = request.POST['Wilaye']  # Utilisez le bon ID
        moughataa_id = request.POST['Moughataa']  # Utilisez le bon ID
        age_group = request.POST['age_group']

        # Gérer l'upload de la photo
        photo = None
        if request.FILES.get('photo'):
            photo = request.FILES['photo']

        # Créer une nouvelle académie
        academie = Academie(
            name_fr=nom_fr,
            name_ar=nom_ar,
            location_fr=lieu_fr,
            location_ar=lieu_ar,
            longitude=float(longitude),  # Conversion explicite
            latitude=float(latitude),  # Conversion explicite
            wilaye_id=wilaye_id,  # Assurez-vous que vous utilisez l'ID ici
            moughataa_id=moughataa_id,  # Assurez-vous que vous utilisez l'ID ici
            age_group=age_group,
            photo=photo
        )
        academie.save()

        # Rediriger vers une autre page ou afficher un message de succès
        messages.success(request, "Académie ajoutée avec succès.")
        return redirect('academie')  # Remplacez par le bon nom de route

    # Contexte à passer à la page
    context = {
        'wilayes': wilayes,
        'moughataa': moughataa, 
        'academies':academies# Assurez-vous que c'est moughataas
    }
    return render(request, 'pages/academie.html',context)

def ajouter_academie(request):
    return render(request, 'pages/ajouter_academie.html')
def modifier_academie(request, academie_id):
    academie_instance = get_object_or_404(Academie, id=academie_id)

    if request.method == 'POST':
        academie_instance.name_fr = request.POST.get('name_fr')
        academie_instance.name_ar = request.POST.get('name_ar')
        
        academie_instance.longitude = request.POST.get('longitude')
        academie_instance.latitude = request.POST.get('latitude')
        academie_instance.wilaye_id = request.POST.get('Wilaye')
        academie_instance.moughataa_id = request.POST.get('Moughataa')
        academie_instance.age_group = request.POST.get('age_group')
        academie_instance.location_fr = request.POST.get('location_fr')
        academie_instance.location_ar = request.POST.get('location_ar')
        
        if 'photo' in request.FILES:
            academie_instance.photo = request.FILES['photo']

        try:
            academie_instance.save()
        except Exception as e:
            messages.error(request, str(e))
            return redirect('academie')
        
        return redirect('academie')

    return render(request, 'pages/modifier_academie.html', {
        'academie': academie_instance,
        'wilayes': Wilaye.objects.all(),
        'moughataa': Moughataa.objects.all(),
    })


def supprimer_academie(request, academie_id):
    academie_instance = get_object_or_404(Academie, id=academie_id)
    if request.method == 'POST':
        academie_instance.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


































