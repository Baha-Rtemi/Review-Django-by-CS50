from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # render( request: HttpRequest,
    #         template_name: "str",
    #         context: value pass it to templates)
    return render(request, "hello/index.html")

def Baha(request):
    return HttpResponse("Hello, Baha")

def Ali(request):
    return HttpResponse("Hello, Ali")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    }) 