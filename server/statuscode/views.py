from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import random
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@method_decorator(csrf_exempt, name="dispatch")
class StatusCodeView(APIView):
    """
    Status Code endpoint - responds with the given HTTP status code
    GET /statuscode/status/{code}/
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        responses={
            "default": openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "code": openapi.Schema(type=openapi.TYPE_INTEGER),
                    "description": openapi.Schema(type=openapi.TYPE_STRING),
                    "headers": openapi.Schema(type=openapi.TYPE_OBJECT),
                    "url": openapi.Schema(type=openapi.TYPE_STRING),
                    "origin": openapi.Schema(type=openapi.TYPE_STRING),
                },
            )
        }
    )
    def get(self, request, code):
        try:
            status_code = int(code)
            if 100 <= status_code <= 599:
                response_data = {
                    "code": status_code,
                    "description": self._get_status_description(status_code),
                    "headers": self._extract_headers(request),
                    "url": request.build_absolute_uri(),
                    "origin": request.META.get('REMOTE_ADDR', '')
                }
                return Response(response_data, status=status_code)
            else:
                return Response(
                    {"error": "Invalid status code. Must be between 100-599."}, 
                    status=400
                )
        except ValueError:
            return Response(
                {"error": "Status code must be a valid integer."}, 
                status=400
            )

    def _get_status_description(self, status_code):
        descriptions = {
            200: "OK",
            201: "Created",
            202: "Accepted",
            204: "No Content",
            301: "Moved Permanently",
            302: "Found",
            304: "Not Modified",
            307: "Temporary Redirect",
            308: "Permanent Redirect",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            405: "Method Not Allowed",
            408: "Request Timeout",
            409: "Conflict",
            429: "Too Many Requests",
            500: "Internal Server Error",
            501: "Not Implemented",
            502: "Bad Gateway",
            503: "Service Unavailable",
            504: "Gateway Timeout"
        }
        return descriptions.get(status_code, "Unknown Status Code")

    def _extract_headers(self, request):
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
class RedirectView(APIView):
    """
    Redirect endpoint - redirects n times
    GET /statuscode/redirect/{n}/
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="count",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description="Internal redirect progress counter"
            )
        ],
        responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)},
    )
    def get(self, request, n):
        try:
            redirect_count = int(n)
            if redirect_count < 0:
                return Response(
                    {"error": "Redirect count must be non-negative."}, 
                    status=400
                )
            current_count = int(request.GET.get('count', 0))
            if current_count >= redirect_count:
                response_data = {
                    "message": f"Redirected {redirect_count} times successfully",
                    "final_url": request.build_absolute_uri(),
                    "total_redirects": redirect_count,
                    "headers": self._extract_headers(request),
                    "origin": request.META.get('REMOTE_ADDR', '')
                }
                return Response(response_data)
            else:
                next_count = current_count + 1
                redirect_url = f"{request.build_absolute_uri()}?count={next_count}"
                return HttpResponseRedirect(redirect_url)
        except ValueError:
            return Response(
                {"error": "Redirect count must be a valid integer."}, 
                status=400
            )

    def _extract_headers(self, request):
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
class RedirectToView(APIView):
    """
    Redirect To endpoint - redirects to a provided URL
    GET /statuscode/redirect-to/
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="url",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="Target URL to redirect to"
            ),
            openapi.Parameter(
                name="status_code",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description="Redirect status code (301,302,303,307,308)"
            ),
        ],
        responses={302: "Redirect"},
    )
    def get(self, request):
        target_url = request.GET.get('url')
        status_code = request.GET.get('status_code', '302')
        if not target_url:
            return Response({"error": "URL parameter is required."}, status=400)
        try:
            status_code_int = int(status_code)
            if status_code_int not in [301, 302, 303, 307, 308]:
                return Response(
                    {"error": "Status code must be a valid redirect code (301, 302, 303, 307, 308)."}, 
                    status=400
                )
        except ValueError:
            return Response({"error": "Status code must be a valid integer."}, status=400)
        return HttpResponseRedirect(target_url)


@method_decorator(csrf_exempt, name="dispatch")
class DenyView(APIView):
    """
    Deny endpoint - returns 403 Forbidden
    GET /statuscode/deny/
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={403: openapi.Schema(type=openapi.TYPE_OBJECT)})
    def get(self, request):
        response_data = {
            "message": "Access Denied",
            "code": 403,
            "description": "Forbidden",
            "headers": self._extract_headers(request),
            "url": request.build_absolute_uri(),
            "origin": request.META.get('REMOTE_ADDR', '')
        }
        return Response(response_data, status=403)

    def _extract_headers(self, request):
        headers = {}
        for key, value in request.META.items():
            if key.startswith("HTTP_"):
                header_name = key[5:].replace("_", "-").title()
                headers[header_name] = value
            elif key in ["CONTENT_TYPE", "CONTENT_LENGTH"]:
                header_name = key.replace("_", "-").title()
                headers[header_name] = value
        return headers
