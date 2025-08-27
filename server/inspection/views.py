from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import uuid as uuid_lib
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


def _extract_headers(request):
    headers = {}
    for key, value in request.META.items():
        if key.startswith("HTTP_"):
            header_name = key[5:].replace("_", "-").title()
            headers[header_name] = value
        elif key in ["CONTENT_TYPE", "CONTENT_LENGTH"]:
            header_name = key.replace("_", "-").title()
            headers[header_name] = value
    return headers


@method_decorator(csrf_exempt, name="dispatch")
class HeadersView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)})
    def get(self, request):
        return Response({"headers": _extract_headers(request)})


@method_decorator(csrf_exempt, name="dispatch")
class IPView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)})
    def get(self, request):
        return Response({"origin": request.META.get("REMOTE_ADDR", "")})


@method_decorator(csrf_exempt, name="dispatch")
class UserAgentView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)})
    def get(self, request):
        ua = request.META.get("HTTP_USER_AGENT", "")
        return Response({"user-agent": ua})


@method_decorator(csrf_exempt, name="dispatch")
class UUIDView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)})
    def get(self, request):
        return Response({"uuid": str(uuid_lib.uuid4())})


@method_decorator(csrf_exempt, name="dispatch")
class ResponseHeadersView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="key",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description="Any query params will be echoed as response headers",
            )
        ],
        responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)},
    )
    def get(self, request):
        resp = Response({"args": request.GET.dict()})
        for k, v in request.GET.items():
            resp[k] = v
        return resp
