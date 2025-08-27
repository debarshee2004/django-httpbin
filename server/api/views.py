from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, StreamingHttpResponse
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
import base64 as b64
import json
import time
import zlib
import gzip as gz
import io
import os
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.


@swagger_auto_schema(method='get', responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)})
@api_view(["GET"])
def home(request):
    return Response({"message": "Welcome to the API!"}, status=status.HTTP_200_OK)


@swagger_auto_schema(method='get', responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)})
@api_view(["GET"])
def health_check(request):
    return Response({"status": "healthy"}, status=status.HTTP_200_OK)


@swagger_auto_schema(method='get', responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)})
@api_view(["GET"])
def json_view(request):
    data = {"slideshow": {"title": "Sample Slide Show", "slides": [{"title": "Slide 1"}]}}
    return Response(data)


@swagger_auto_schema(method='get', responses={200: 'XML'})
@api_view(["GET"])
def xml_view(request):
    xml = """<?xml version='1.0' encoding='us-ascii'?>\n<slideshow title='Sample Slide Show'><slide title='Slide 1' /></slideshow>"""
    return HttpResponse(xml, content_type="application/xml")


@swagger_auto_schema(method='get', responses={200: 'HTML'})
@api_view(["GET"])
def html_view(request):
    html = """<html><head><title>Sample</title></head><body><h1>Sample HTML</h1></body></html>"""
    return HttpResponse(html, content_type="text/html; charset=utf-8")


@swagger_auto_schema(method='get', responses={200: 'UTF-8 text'})
@api_view(["GET"])
def utf8_view(request):
    content = "÷ Samples: Café – 東京 — emojis 😀"
    return HttpResponse(content, content_type="text/plain; charset=utf-8")


@swagger_auto_schema(method='get', responses={200: 'binary'})
@api_view(["GET"])
def bytes_view(request, n: int):
    rng = os.urandom(n)
    return HttpResponse(rng, content_type="application/octet-stream")


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('duration', openapi.IN_QUERY, type=openapi.TYPE_NUMBER, required=False),
        openapi.Parameter('numbytes', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=False),
    ],
    responses={200: 'stream'}
)
@api_view(["GET"])
def drip_view(request):
    duration = float(request.GET.get("duration", "1"))
    numbytes = int(request.GET.get("numbytes", "10"))
    interval = duration / max(numbytes, 1)

    def generator():
        for _ in range(numbytes):
            time.sleep(interval)
            yield b"*"

    return StreamingHttpResponse(generator(), content_type="application/octet-stream")


@swagger_auto_schema(method='get', responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)})
@api_view(["GET"])
def delay_view(request, seconds: int):
    time.sleep(seconds)
    return Response({"delay": seconds, "status": "done"})


@swagger_auto_schema(method='get', responses={200: 'stream'})
@api_view(["GET"])
def stream_view(request, lines: int):
    def generator():
        for i in range(lines):
            yield json.dumps({"line": i}) + "\n"
            time.sleep(0.05)

    return StreamingHttpResponse(generator(), content_type="application/json")


@swagger_auto_schema(method='get', responses={200: 'binary'})
@api_view(["GET"])
def range_view(request, num: int):
    data = bytes(range(0, num % 256)) * (num // 256) + bytes(range(0, num % 256))[: num % 256]
    return HttpResponse(data, content_type="application/octet-stream")


@swagger_auto_schema(method='get', responses={200: 'gzip'})
@api_view(["GET"])
def gzip_view(request):
    buf = io.BytesIO()
    with gz.GzipFile(fileobj=buf, mode="wb") as f:
        f.write(b"hello world")
    return HttpResponse(buf.getvalue(), content_type="application/gzip")


@swagger_auto_schema(method='get', responses={200: 'deflate'})
@api_view(["GET"])
def deflate_view(request):
    compressed = zlib.compress(b"hello world")
    return HttpResponse(compressed, content_type="application/zlib")


@swagger_auto_schema(method='get', responses={200: 'binary or error 400'})
@api_view(["GET"])
def base64_view(request, value: str):
    try:
        decoded = b64.b64decode(value)
        return HttpResponse(decoded, content_type="application/octet-stream")
    except Exception:
        return Response({"error": "invalid base64"}, status=400)


@swagger_auto_schema(method='get', responses={200: 'HTML'})
@api_view(["GET"])
def links_view(request, n: int):
    links = "".join([f"<a href='/api/links/{i}/'>{i}</a><br/>" for i in range(n)])
    return HttpResponse(links, content_type="text/html; charset=utf-8")


@swagger_auto_schema(method='get', responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)})
@api_view(["GET"])
def cache_view(request):
    resp = Response({"cached": True})
    resp["Cache-Control"] = "public, max-age=3600"
    return resp


@swagger_auto_schema(method='post', responses={200: openapi.Schema(type=openapi.TYPE_OBJECT)})
@api_view(["POST"])
def forms_post_view(request):
    return Response({"form": request.POST.dict(), "files": {k: f.name for k, f in request.FILES.items()}})


@swagger_auto_schema(method='get', responses={200: 'text/plain'})
@api_view(["GET"])
def robots_txt(request):
    content = "User-agent: *\nDisallow: /deny\n"
    return HttpResponse(content, content_type="text/plain")
