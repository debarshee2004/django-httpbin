from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({"message": "Welcome to the API!"}, status=200)


def health_check(request):
    return JsonResponse({"status": "healthy"}, status=200)
