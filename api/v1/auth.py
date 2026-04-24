from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.serializers import RegisterSerializer, UserSerializer
from apps.users.services import create_user

from rest_framework_simplejwt.tokens import RefreshToken


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = create_user(**serializer.validated_data)

        refresh = RefreshToken.for_user(user)

        return Response({
            "user": UserSerializer(user).data,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }, status=status.HTTP_201_CREATED)