from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


def _cookies_dict(request):
    return {k: v for k, v in request.COOKIES.items()}


@method_decorator(csrf_exempt, name="dispatch")
class CookiesView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)})
    def get(self, request):
        return Response({"cookies": _cookies_dict(request)})


@method_decorator(csrf_exempt, name="dispatch")
class SetCookiesView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="name",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description="Cookie key to set"
            ),
            openapi.Parameter(
                name="value",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description="Cookie value to set"
            ),
        ],
        responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)},
    )
    def get(self, request):
        resp = Response({"cookies": _cookies_dict(request), "set": request.GET.dict()})
        for k, v in request.GET.items():
            resp.set_cookie(k, v)
        return resp


@method_decorator(csrf_exempt, name="dispatch")
class DeleteCookiesView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="name",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description="Cookie key to delete"
            ),
        ],
        responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)},
    )
    def get(self, request):
        resp = Response({"cookies": _cookies_dict(request), "deleted": list(request.GET.keys())})
        for k in request.GET.keys():
            resp.delete_cookie(k)
        return resp
