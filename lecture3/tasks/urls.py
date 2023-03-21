from django.urls import path

from . import views

# we create name for this app to not have 
# namespace collision (same name for two or more url app) when we call it in our index.html
app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]