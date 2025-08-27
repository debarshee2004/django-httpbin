from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


def _cookies_dict(request):
    return {k: v for k, v in request.COOKIES.items()}


@method_decorator(csrf_exempt, name="dispatch")
class CookiesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"cookies": _cookies_dict(request)})


@method_decorator(csrf_exempt, name="dispatch")
class SetCookiesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        resp = Response({"cookies": _cookies_dict(request), "set": request.GET.dict()})
        for k, v in request.GET.items():
            resp.set_cookie(k, v)
        return resp


@method_decorator(csrf_exempt, name="dispatch")
class DeleteCookiesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        resp = Response({"cookies": _cookies_dict(request), "deleted": list(request.GET.keys())})
        for k in request.GET.keys():
            resp.delete_cookie(k)
        return resp
