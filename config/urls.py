from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth + users
    path('api/users/', include('apps.users.urls')),

    # Projects

    # JWT (simplejwt default endpoints)
    path('api/token/', include('rest_framework_simplejwt.urls')),
]