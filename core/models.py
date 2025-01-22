from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Experience(models.Model):
    TYPE_CHOICES = [
        ('stage', 'Stage'),
        ('emploi', 'Emploi'),
        ('autre', 'Autre'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poste = models.CharField(max_length=255, null=True, blank=True)
    entreprise = models.CharField(max_length=255, null=True, blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    duree = models.CharField(max_length=100, null=True, blank=True)
    ville = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    active = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.date_debut and self.date_fin:
            # Calcul de la durée
            duree = self.date_fin - self.date_debut

            # Obtenez la durée en jours
            nombre_de_jours = duree.days

            # Calcul de la durée en années, mois et jours
            annees = nombre_de_jours // 365
            mois = (nombre_de_jours % 365) // 30
            jours = (nombre_de_jours % 365) % 30

            # Créez une liste pour stocker les composantes non nulles de la durée
            composantes_non_nulles = []

            # Vérifiez chaque composante et ajoutez-la à la liste si elle n'est pas nulle
            if annees > 0:
                composantes_non_nulles.append(f"{annees} an{'s' if annees > 1 else ''}")
            if mois > 0:
                composantes_non_nulles.append(f"{mois} mois")
            if jours > 0:
                composantes_non_nulles.append(f"{jours} jour{'s' if jours > 1 else ''}")

            # Formatage de la durée
            if composantes_non_nulles:
                duree_formatee = ', '.join(composantes_non_nulles)
            else:
                duree_formatee = "0 jours"  # Si toutes les composantes sont nulles

            # Mettez à jour le champ 'duree' avec la durée calculée
            self.duree = duree_formatee

    def __str__(self):
        return f"{self.poste} à {self.entreprise} ({self.type})"
    
class Formation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    intitule = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.intitule} - {self.institution}"
    
class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    intitule = models.CharField(max_length=255)
    date_obtention = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='certifications/', null=True, blank=True)
    valide = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.intitule} ({'Valide' if self.valide else 'Non valide'})"

class Competence(models.Model):
    TYPE_CHOICES = [
        ('technique', 'Technique'),
        ('professionnelle', 'Professionnelle'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES,null=True, blank=True)
    libelle = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.libelle} ({self.type})"
    
class Details(models.Model):
    TYPE_CHOICES = [
        ('qualite', 'Qualité'),
        ('centre_interet', 'Centre d\'intérêt'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    libelle = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.libelle} ({self.type})"
    
class Realisation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    lien_site = models.URLField(null=True, blank=True)
    lien_github = models.URLField(null=True, blank=True)
    ordre = models.PositiveIntegerField(default=0)
    date = models.DateField(null=True, blank=True)

    active = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

class DetailRealisation(models.Model):
    realisation = models.ForeignKey(Realisation, on_delete=models.CASCADE)
    capture = models.ImageField(upload_to='realisations/', null=True, blank=True)
    ordre = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

class Mouchard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mouchards')
    action = models.CharField(max_length=255,blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mouchard {self.action0} - {self.description[:20]}"
