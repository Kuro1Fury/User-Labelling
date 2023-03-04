from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Label
from .forms import CreateNewLabel

# Create your views here.

def index(response, id):
    ls = Label.objects.get(id=id)
 
    if ls in response.user.label.all():
        return render(response, "main/label.html", {"ls":ls})
    return render(response, "main/home.html", {})

def home(response):
	return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewLabel(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Label(name=n)
            t.save()
            response.user.label.add(t)

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewLabel()

    return render(response, "main/create.html", {"form":form})

def view(response):
    return render(response, "main/view.html", {})