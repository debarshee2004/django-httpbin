from django.urls import path

from .views import home, health_check, json_view, xml_view, html_view, utf8_view, bytes_view, drip_view, delay_view, stream_view, range_view, gzip_view, deflate_view, base64_view, links_view, cache_view, forms_post_view, robots_txt

urlpatterns = [
    path("", home, name="home"),
    path("health/", health_check, name="health_check"),
    path("json/", json_view, name="json"),
    path("xml/", xml_view, name="xml"),
    path("html/", html_view, name="html"),
    path("encoding/utf8/", utf8_view, name="utf8"),
    path("bytes/<int:n>/", bytes_view, name="bytes"),
    path("drip/", drip_view, name="drip"),
    path("delay/<int:seconds>/", delay_view, name="delay"),
    path("stream/<int:lines>/", stream_view, name="stream"),
    path("range/<int:num>/", range_view, name="range"),
    path("gzip/", gzip_view, name="gzip"),
    path("deflate/", deflate_view, name="deflate"),
    path("base64/<str:value>/", base64_view, name="base64"),
    path("links/<int:n>/", links_view, name="links"),
    path("cache/", cache_view, name="cache"),
    path("forms/post/", forms_post_view, name="forms-post"),
    path("robots.txt/", robots_txt, name="robots-txt"),
]
