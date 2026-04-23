from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Users app is working"})