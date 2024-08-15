from rest_framework import serializers 
from .models import Client, Joueurs, Terrains, Reservations,Moughataa
from django.contrib.auth.hashers import make_password


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'nom', 'prenom', 'numero_telephone', 'modepass_chiffre']
        extra_kwargs = {
            'modepass_chiffre': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['modepass_chiffre'] = make_password(validated_data['modepass_chiffre'])
        return super().create(validated_data)


class TerrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terrains
        fields = '__all__'
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = ['id', 'terrain', 'joueur', 'date_reservation', 'heure_debut', 'heure_fin']
class JoueurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joueurs
        fields = ['nom_joueur', 'prenom_joueur', 'numero_telephone', 'password']

    def create(self, validated_data):
        # Hash the password before saving the user
        validated_data['password'] = make_password(validated_data['password'])
        joueur = Joueurs.objects.create(**validated_data)
        return joueur
from rest_framework import serializers
from .models import Wilaye, Terrains

class WilayeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wilaye
        fields = ['code_wilaye', 'nom_wilaye_Ar', 'nom_wilaye_fr']

class TerrainsSerializer(serializers.ModelSerializer):
    wilaye = WilayeSerializer()

    class Meta:
        model = Terrains
        fields = '__all__'
class MoughataaSerializer(serializers.ModelSerializer):
    wilaye = WilayeSerializer()

    class Meta:
        model = Moughataa
        fields = '__all__'
