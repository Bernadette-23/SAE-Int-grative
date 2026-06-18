from django.shortcuts import render
from .models import Capteur

# Create your views here.

def modifier_capteur(request, id):

    capteur = Capteur.objects.get(id=id)

    if request.method == "POST":

        capteur.nom_capteur = request.POST["nom_capteur"]
        capteur.emplacement = request.POST["emplacement"]
        capteur.save()

        return redirect("/")

    return render(
        request,
        "capteurs/modifier_capteur.html",
        {"capteur": capteur}
    )
