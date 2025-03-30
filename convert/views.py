from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Accueil(request):
    if request.method=="POST":
        nombre=request.POST.get("nombre")
        convType=request.POST.get("conv_type")
        if(convType=="bin_to_dec"):
            res=int(nombre,2)
        elif (convType=="dec_to_bin"):
            res=bin(int(nombre))
        else:
            res="Erreur de conversion"
        return render(request,"convert/resultat.html",{"res": res})
    else:
        render(request,"convert/resultat.html")
def resultat(request):
    return render(request,"convert/resultat.html")