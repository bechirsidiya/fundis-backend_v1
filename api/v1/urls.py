from django.urls import path
from .auth import RegisterAPIView
from .projects import urlpatterns as project_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Auth
    path('auth/register/', RegisterAPIView.as_view(), name='register'),

    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += project_urls