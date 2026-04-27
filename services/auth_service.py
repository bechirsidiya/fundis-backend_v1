from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()


def register_user(email, username, password):
    user = User.objects.create_user(
        email=email,
        username=username,
        password=password
    )
    return user


def login_user(email, password):
    user = authenticate(email=email, password=password)
    if not user:
        return None
    return user