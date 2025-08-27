from django.urls import path
from . import views

app_name = "statuscode"

urlpatterns = [
    path("status/<int:code>/", views.StatusCodeView.as_view(), name="status"),
    path("redirect/<int:n>/", views.RedirectView.as_view(), name="redirect"),
    path("redirect-to/", views.RedirectToView.as_view(), name="redirect-to"),
    path("deny/", views.DenyView.as_view(), name="deny"),
]
