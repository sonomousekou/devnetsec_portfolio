from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'experiences', views.ExperienceViewSet)
router.register(r'formations', views.FormationViewSet)
router.register(r'certifications', views.CertificationViewSet)
router.register(r'competences', views.CompetenceViewSet)
router.register(r'details', views.DetailsViewSet)
router.register(r'realisations', views.RealisationViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
    path('', include(router.urls)),
]
