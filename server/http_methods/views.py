from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


@method_decorator(csrf_exempt, name="dispatch")
class GetView(APIView):
    """
    GET method endpoint - returns request data for GET requests
    GET /http_methods/get/
    """
    permission_classes = [AllowAny]

    def get(self, request):
        response_data = {
            "args": dict(request.GET),
            "headers": self._extract_headers(request),
            "origin": request.META.get('REMOTE_ADDR', ''),
            "url": request.build_absolute_uri(),
            "method": "GET"
        }
        return Response(response_data)

    def _extract_headers(self, request):
        """Extract all headers from request"""
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
class PostView(APIView):
    """
    POST method endpoint - returns posted data for POST requests
    POST /http_methods/post/
    """
    permission_classes = [AllowAny]

    def post(self, request):
        response_data = {
            "args": dict(request.GET),
            "data": request.data,
            "files": dict(request.FILES),
            "form": dict(request.POST),
            "headers": self._extract_headers(request),
            "json": request.data if request.content_type == 'application/json' else None,
            "origin": request.META.get('REMOTE_ADDR', ''),
            "url": request.build_absolute_uri(),
            "method": "POST"
        }
        return Response(response_data)

    def _extract_headers(self, request):
        """Extract all headers from request"""
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
class PutView(APIView):
    """
    PUT method endpoint - returns PUT data for PUT requests
    PUT /http_methods/put/
    """
    permission_classes = [AllowAny]

    def put(self, request):
        response_data = {
            "args": dict(request.GET),
            "data": request.data,
            "files": dict(request.FILES),
            "form": dict(request.POST),
            "headers": self._extract_headers(request),
            "json": request.data if request.content_type == 'application/json' else None,
            "origin": request.META.get('REMOTE_ADDR', ''),
            "url": request.build_absolute_uri(),
            "method": "PUT"
        }
        return Response(response_data)

    def _extract_headers(self, request):
        """Extract all headers from request"""
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
class PatchView(APIView):
    """
    PATCH method endpoint - returns PATCH data for PATCH requests
    PATCH /http_methods/patch/
    """
    permission_classes = [AllowAny]

    def patch(self, request):
        response_data = {
            "args": dict(request.GET),
            "data": request.data,
            "files": dict(request.FILES),
            "form": dict(request.POST),
            "headers": self._extract_headers(request),
            "json": request.data if request.content_type == 'application/json' else None,
            "origin": request.META.get('REMOTE_ADDR', ''),
            "url": request.build_absolute_uri(),
            "method": "PATCH"
        }
        return Response(response_data)

    def _extract_headers(self, request):
        """Extract all headers from request"""
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
class DeleteView(APIView):
    """
    DELETE method endpoint - returns request data for DELETE requests
    DELETE /http_methods/delete/
    """
    permission_classes = [AllowAny]

    def delete(self, request):
        response_data = {
            "args": dict(request.GET),
            "headers": self._extract_headers(request),
            "origin": request.META.get('REMOTE_ADDR', ''),
            "url": request.build_absolute_uri(),
            "method": "DELETE"
        }
        return Response(response_data)

    def _extract_headers(self, request):
        """Extract all headers from request"""
        headers = {}
        for key, value in request.META.items():
            if key.startswith("HTTP_"):
                header_name = key[5:].replace("_", "-").title()
                headers[header_name] = value
            elif key in ["CONTENT_TYPE", "CONTENT_LENGTH"]:
                header_name = key.replace("_", "-").title()
                headers[header_name] = value
        return headers



