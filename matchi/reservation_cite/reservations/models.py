from django.db import models
from django.contrib.auth.hashers import make_password

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numero_telephone = models.IntegerField()
    modepass_chiffre = models.CharField(max_length=128)

class Wilaye(models.Model):
    code_wilaye = models.IntegerField(primary_key=True)
    nom_wilaye_Ar = models.CharField(max_length=255, blank=True, null=True)
    nom_wilaye_fr = models.CharField(max_length=255, blank=True, null=True)

class Moughataa(models.Model):
    nom_fr = models.CharField(max_length=255)
    nom_ar = models.CharField(max_length=255)
    wilaye = models.ForeignKey(Wilaye, on_delete=models.CASCADE)

class Terrains(models.Model):
    nom_fr = models.CharField(max_length=255)  # Remplacement de nom par nom_fr
    nom_ar = models.CharField(max_length=255)  # Ajout du champ nom_ar
    longitude = models.DecimalField(max_digits=10, decimal_places=3)
    latitude = models.DecimalField(max_digits=10, decimal_places=3)
    nombre_joueur = models.IntegerField()
    lieu_fr = models.CharField(max_length=255)  # Remplacement de lieu par lieu_fr
    lieu_ar = models.CharField(max_length=255)  # Ajout du champ lieu_ar
    photo1 = models.ImageField(upload_to='images', blank=True)
    photo2 = models.ImageField(upload_to='images', blank=True)
    photo3 = models.ImageField(upload_to='images', blank=True)
    prix_par_heure = models.IntegerField()
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    wilaye = models.ForeignKey('Wilaye', on_delete=models.CASCADE)
    moughataa = models.ForeignKey(Moughataa, on_delete=models.CASCADE, default=None)
    heure_ouverture = models.TimeField()
    heure_fermeture = models.TimeField()
    ballon_disponible = models.BooleanField(default=False)
    maillot_disponible = models.BooleanField(default=False)
    eclairage_disponible = models.BooleanField(default=False)
    siffler = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    eau = models.BooleanField(default=False)
    gazon_artificiel = models.BooleanField(default=True)



    



class Joueurs(models.Model):
    nom_joueur = models.CharField(max_length=100)
    prenom_joueur = models.CharField(max_length=100)
    numero_telephone = models.CharField(max_length=20)
    password = models.CharField(max_length=128, null=True, blank=True)
    poste = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # image = models.CharField(max_length=100)

    photo_de_profile = models.ImageField(upload_to='images/', blank=True, null=True)
    wilaye = models.ForeignKey('Wilaye', on_delete=models.CASCADE ,null=True)
    moughataa = models.ForeignKey(Moughataa, on_delete=models.CASCADE, default=None, null=True)

    def save(self, *args, **kwargs):
        if self.password and not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Reservations(models.Model):
    terrain = models.ForeignKey(Terrains, on_delete=models.CASCADE)
    joueur = models.ForeignKey(Joueurs, on_delete=models.CASCADE)
    date_reservation = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

class Indisponibilites(models.Model):
    terrain = models.ForeignKey(Terrains, on_delete=models.CASCADE)
    date_indisponibilite = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

class Notification(models.Model):
    contenu = models.TextField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    est_lue = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class Evaluation(models.Model):
    evaluateur = models.ForeignKey(Joueurs, related_name='evaluations_done', on_delete=models.CASCADE)
    evalue = models.ForeignKey(Joueurs, related_name='evaluations_received', on_delete=models.CASCADE)
    note = models.IntegerField()  # Note sur 5 étoiles
    commentaire = models.TextField(null=True, blank=True)
    date_evaluation = models.DateTimeField(auto_now_add=True)
    