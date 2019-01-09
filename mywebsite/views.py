from django.shortcuts import render

def index(request):
    context = {
        "Judul":"Home Page",
        "Content":"Ini adalah Home page dari website"
    }
    return render(request,"index.html",context)