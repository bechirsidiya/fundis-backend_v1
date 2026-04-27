from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from services.auth_service import register_user


class RegisterAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        username = request.data.get("username")
        password = request.data.get("password")

        user = register_user(email, username, password)

        return Response({
            "id": user.id,
            "email": user.email
        }, status=status.HTTP_201_CREATED)