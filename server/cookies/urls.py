from django.urls import path
from . import views

app_name = "cookies"

urlpatterns = [
    path("", views.CookiesView.as_view(), name="cookies"),
    path("set/", views.SetCookiesView.as_view(), name="cookies-set"),
    path("delete/", views.DeleteCookiesView.as_view(), name="cookies-delete"),
]
