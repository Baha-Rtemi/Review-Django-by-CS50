from django.urls import path
from . import views

urlpatterns = [
    # path ( ||  Three Arguments  || )
    # path(  A string representing the URL path
    #        this string pass it to views.py,
    #        A function from views.py that we wish to call when that URL is visited,
    #        A name for that path
    #     )
    path("", views.index, name="index"),
    path("Baha/", views.Baha, name="Baha"),
    path("Ali/", views.Ali, name="Ali"),
    path("<str:name>", views.greet, name="greet"),
    path("<str:name>/", views.greet, name="greet")
]