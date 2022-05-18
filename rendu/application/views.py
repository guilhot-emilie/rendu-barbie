from django.shortcuts import render

# Create your views here.

def firstform(request):
    return render(request,"application/firstform.html")

def traitement(request):
    nom = request.GET["nom"]
    return render(request,"application/traitement.html")