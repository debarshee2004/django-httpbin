from django.urls import path
from . import views

app_name = "http_methods"

urlpatterns = [
    path("get/", views.GetView.as_view(), name="get"),
    path("post/", views.PostView.as_view(), name="post"),
    path("put/", views.PutView.as_view(), name="put"),
    path("patch/", views.PatchView.as_view(), name="patch"),
    path("delete/", views.DeleteView.as_view(), name="delete"),
]
