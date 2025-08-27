from django.urls import path
from . import views

app_name = "auth"

urlpatterns = [
    path(
        "basic-auth/<str:username>/<str:password>/",
        views.BasicAuthView.as_view(),
        name="basic-auth",
    ),
    path("bearer/", views.BearerAuthView.as_view(), name="bearer"),
    path(
        "hidden-basic-auth/<str:username>/<str:password>/",
        views.HiddenBasicAuthView.as_view(),
        name="hidden-basic-auth",
    ),
    path(
        "digest-auth/<str:qop>/<str:username>/<str:password>/"
        "<str:algo>/<str:stale_after>/",
        views.DigestAuthView.as_view(),
        name="digest-auth",
    ),
    path("validate-token/", views.TokenValidationView.as_view(), name="validate-token"),
]
