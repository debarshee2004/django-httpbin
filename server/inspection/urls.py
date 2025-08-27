from django.urls import path
from . import views

app_name = "inspection"

urlpatterns = [
    path("headers/", views.HeadersView.as_view(), name="headers"),
    path("ip/", views.IPView.as_view(), name="ip"),
    path("user-agent/", views.UserAgentView.as_view(), name="user-agent"),
    path("uuid/", views.UUIDView.as_view(), name="uuid"),
    path("response-headers/", views.ResponseHeadersView.as_view(), name="response-headers"),
]
