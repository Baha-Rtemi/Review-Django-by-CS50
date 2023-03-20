from django.shortcuts import render

# Create your views here.
tasks = [ "foo", "boo", "baz" ]
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })