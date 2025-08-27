from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import uuid as uuid_lib


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

    def get(self, request):
        return Response({"headers": _extract_headers(request)})


@method_decorator(csrf_exempt, name="dispatch")
class IPView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"origin": request.META.get("REMOTE_ADDR", "")})


@method_decorator(csrf_exempt, name="dispatch")
class UserAgentView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        ua = request.META.get("HTTP_USER_AGENT", "")
        return Response({"user-agent": ua})


@method_decorator(csrf_exempt, name="dispatch")
class UUIDView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"uuid": str(uuid_lib.uuid4())})


@method_decorator(csrf_exempt, name="dispatch")
class ResponseHeadersView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Echo back query params as response headers
        resp = Response({"args": request.GET.dict()})
        for k, v in request.GET.items():
            resp[k] = v
        return resp
