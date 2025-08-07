from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .authentication import (
    HTTPBinBasicAuthentication,
    HTTPBinBearerAuthentication,
    HTTPBinDigestAuthentication,
)
from .serializers import (
    AuthResponseSerializer,
    TokenValidationSerializer,
    TokenValidationResponseSerializer,
)
from .utils import (
    generate_digest_challenge,
    validate_digest_response,
    extract_request_headers,
)


@method_decorator(csrf_exempt, name="dispatch")
class BasicAuthView(APIView):
    """
    Basic Authentication endpoint
    GET /auth/basic-auth/{username}/{password}
    """

    authentication_classes = [HTTPBinBasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, username, password):
        auth_result = HTTPBinBasicAuthentication().authenticate(request)

        if not auth_result:
            response = HttpResponse("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)
            response["WWW-Authenticate"] = 'Basic realm="HTTPBin"'
            return response

        auth_username, auth_password = auth_result[0]

        if auth_username != username or auth_password != password:
            response = HttpResponse("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)
            response["WWW-Authenticate"] = 'Basic realm="HTTPBin"'
            return response

        response_data = {
            "authenticated": True,
            "user": username,
            "token": None,
            "method": "basic",
            "headers": extract_request_headers(request),
            "url": request.build_absolute_uri(),
        }

        serializer = AuthResponseSerializer(response_data)
        return Response(serializer.data)


@method_decorator(csrf_exempt, name="dispatch")
class BearerAuthView(APIView):
    """
    Bearer Token Authentication endpoint
    GET /auth/bearer
    """

    authentication_classes = [HTTPBinBearerAuthentication]
    permission_classes = [AllowAny]

    def get(self, request):
        auth_result = HTTPBinBearerAuthentication().authenticate(request)

        if not auth_result:
            return Response(
                {"error": "Bearer token required"}, status=status.HTTP_401_UNAUTHORIZED
            )

        user, token = auth_result[0]

        response_data = {
            "authenticated": True,
            "user": user,
            "token": token,
            "method": "bearer",
            "headers": extract_request_headers(request),
            "url": request.build_absolute_uri(),
        }

        serializer = AuthResponseSerializer(response_data)
        return Response(serializer.data)


@method_decorator(csrf_exempt, name="dispatch")
class HiddenBasicAuthView(APIView):
    """
    Hidden Basic Authentication endpoint (returns 404 instead of 401)
    GET /auth/hidden-basic-auth/{username}/{password}
    """

    authentication_classes = [HTTPBinBasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, username, password):
        auth_result = HTTPBinBasicAuthentication().authenticate(request)

        if not auth_result:
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        auth_username, auth_password = auth_result[0]

        if auth_username != username or auth_password != password:
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        response_data = {
            "authenticated": True,
            "user": username,
            "token": None,
            "method": "hidden-basic",
            "headers": extract_request_headers(request),
            "url": request.build_absolute_uri(),
        }

        serializer = AuthResponseSerializer(response_data)
        return Response(serializer.data)


@method_decorator(csrf_exempt, name="dispatch")
class DigestAuthView(APIView):
    """
    Digest Authentication endpoint
    GET /auth/digest-auth/{qop}/{username}/{password}
    """

    authentication_classes = [HTTPBinDigestAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, qop, username, password):
        auth_result = HTTPBinDigestAuthentication().authenticate(request)

        if not auth_result:
            challenge, nonce, opaque = generate_digest_challenge(qop=qop)
            response = HttpResponse("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)
            response["WWW-Authenticate"] = f"Digest {challenge}"
            return response

        auth_username, auth_dict = auth_result[0]

        # Validate digest response
        if not validate_digest_response(
            username, password, request.method, request.get_full_path(), auth_dict
        ):
            challenge, nonce, opaque = generate_digest_challenge(qop=qop)
            response = HttpResponse("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)
            response["WWW-Authenticate"] = f"Digest {challenge}"
            return response

        response_data = {
            "authenticated": True,
            "user": username,
            "token": None,
            "method": "digest",
            "headers": extract_request_headers(request),
            "url": request.build_absolute_uri(),
        }

        serializer = AuthResponseSerializer(response_data)
        return Response(serializer.data)


@method_decorator(csrf_exempt, name="dispatch")
class TokenValidationView(APIView):
    """
    Token Validation endpoint
    POST /auth/validate-token
    """

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = TokenValidationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = getattr(serializer, "validated_data", None)
        token = (
            validated_data.get("token")
            if validated_data and hasattr(validated_data, "get")
            else None
        )
        if token is None:
            return Response(
                {"error": "Token is required."}, status=status.HTTP_400_BAD_REQUEST
            )

        # Check if token is in Authorization header
        auth_header = request.META.get("HTTP_AUTHORIZATION", "")
        header_token = None
        auth_method = "body"

        if auth_header.startswith("Bearer "):
            header_token = auth_header[7:]
            auth_method = "bearer"
        elif auth_header.startswith("Basic "):
            header_token = auth_header[6:]
            auth_method = "basic"

        # Use header token if available, otherwise use body token
        final_token = header_token if header_token else token

        # Simple validation - in real app, you'd validate against your token system
        is_valid = len(final_token) > 10  # Simple length check

        details = {
            "length": len(final_token),
            "source": "header" if header_token else "body",
            "auth_method": auth_method,
            "headers": extract_request_headers(request),
        }

        response_data = {
            "valid": is_valid,
            "token": final_token[:20] + "..." if len(final_token) > 20 else final_token,
            "method": auth_method,
            "details": details,
        }

        response_serializer = TokenValidationResponseSerializer(response_data)
        return Response(response_serializer.data)
