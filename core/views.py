from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from .models import Mouchard, Experience, Formation, Certification, Competence, Details, Realisation
from .serializers import (
    ExperienceSerializer, FormationSerializer, CertificationSerializer,
    CompetenceSerializer, DetailsSerializer, RealisationSerializer
)

def log_action(user, description):
    """
    Fonction pour enregistrer une action dans le modèle Mouchard.
    """
    Mouchard.objects.create(user=user, description=description)

    """Fonction pour loguer les actions des utilisateurs."""
    # Vous pouvez loguer l'action dans un fichier ou une base de données
    # Exemple : Loguer dans un fichier
    with open('action_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now()} - {user.username}: {description}\n")

# Base commune pour les ViewSets
class BaseLoggingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Associer l'utilisateur authentifié à l'objet lors de la création
        serializer.save(user=self.request.user)
        instance = serializer.instance
        log_action(self.request.user, f"Créé {instance}.")

    def perform_update(self, serializer):
        instance = serializer.save()
        log_action(self.request.user, f"Mis à jour {instance}.")

    def perform_destroy(self, instance):
        log_action(self.request.user, f"Supprimé {instance}.")
        instance.delete()

    # Filtrer les objets par l'utilisateur authentifié
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

class ExperienceViewSet(BaseLoggingViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class FormationViewSet(BaseLoggingViewSet):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer

class CertificationViewSet(BaseLoggingViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class CompetenceViewSet(BaseLoggingViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer

class DetailsViewSet(BaseLoggingViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer

class RealisationViewSet(BaseLoggingViewSet):
    queryset = Realisation.objects.all()
    serializer_class = RealisationSerializer