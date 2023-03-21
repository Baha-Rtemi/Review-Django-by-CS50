from django.shortcuts import render
# Django Forms
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here. ( This before use sessions)
# tasks = [ "foo", "boo", "baz" ]

def index(request):
    # Check if there already exists a "tasks" key in our session
    if "tasks" not in request.session:
        # If not, create a new list
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

# Django Forms
class NewTaskForm(forms.Form):
    # class NewTaskForm(our new form inherits=> from a class called >>Form<<):
    # we see that we have (forms.Form) 
    # This is because our new form inherits from a class called (Form) 
    # that is included in the forms module.
    task = forms.CharField(label="New Task") # LIKE <input type="text">

# add new task
def add(request):
    # Check if method is POST
    if request.method == "POST":
        #  Take in the data the user submitted and save it as form
        form = NewTaskForm(request.POST)
        # NewTaskForm() ==> creates a blank form.
        # you can also populate that form with some data.
        # if I populate it with request.post ( NewTaskForm(request.POST))
        # resuest.POST : contains all of the data that
        # the user submitted when they submitted the form.

        # Check if form data is valid ( server-side )
        if form.is_valid():
            # Isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data["task"]

            # Add the new task to our list of tasks
            # tasks.append(task)  (befor using session)
            request.session["tasks"] += [task]

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            # If the is invalid, re-render the page with existing information.
            return render (request, "task/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })


# There are several advantages to using the forms module rather than manually writing an HTML form:

# * If we want to add new fields to the form, we can simply add them in views.py without typing additional HTML.
# * Django automatically performs client-side validation, or validation local to the user’s machine. meaning it will not allow a user to submit their form if it is incomplete.
# * Django provides simple server-side validation, or validation that occurs once form data has reached the server.
# * we’ll begin using models to store information, and Django makes it very simple to create a form based on a model.