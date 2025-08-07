from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(["GET"])
def home(request):
    return Response({"message": "Welcome to the API!"}, status=200)


@api_view(["GET"])
def health_check(request):
    return Response({"status": "healthy"}, status=200)
