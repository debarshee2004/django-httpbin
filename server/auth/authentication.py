import base64
from rest_framework import authentication, exceptions


class HTTPBinBasicAuthentication(authentication.BaseAuthentication):
    """
    Custom Basic Authentication for HTTPBin endpoints
    """

    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header or not auth_header.startswith("Basic "):
            return None

        try:
            credentials = base64.b64decode(auth_header[6:]).decode("utf-8")
            username, password = credentials.split(":", 1)
            return (username, password), None
        except (ValueError, UnicodeDecodeError):
            raise exceptions.AuthenticationFailed("Invalid basic auth credentials")


class HTTPBinBearerAuthentication(authentication.BaseAuthentication):
    """
    Custom Bearer Token Authentication for HTTPBin endpoints
    """

    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header or not auth_header.startswith("Bearer "):
            return None

        token = auth_header[7:]
        return ("bearer_user", token), None


class HTTPBinDigestAuthentication(authentication.BaseAuthentication):
    """
    Custom Digest Authentication for HTTPBin endpoints
    """

    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header or not auth_header.startswith("Digest "):
            return None

        # Parse digest auth header
        auth_dict = {}
        auth_header = auth_header[7:]  # Remove 'Digest '

        for item in auth_header.split(", "):
            key, value = item.split("=", 1)
            auth_dict[key] = value.strip('"')

        return (auth_dict.get("username"), auth_dict), None
