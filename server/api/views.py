from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(["GET"])
def home(request):
    return Response({"message": "Welcome to the API!"}, status=status.HTTP_200_OK)


@api_view(["GET"])
def health_check(request):
    return Response({"status": "healthy"}, status=status.HTTP_200_OK)
