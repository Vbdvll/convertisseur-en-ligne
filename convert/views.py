from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Accueil(request):
    if request.method=="POST":
        nombre=request.POST.get("nombre")
        convType=request.POST.get("conv_type")
        if nombre is None or convType is None:
            return render(request,"convert/resultat.html",{"error": "Nombre ou le type de conversion ne peut pas etre nulle"})
        try :
            if(convType=="bin_to_dec"):
                res=int(nombre,2)
            elif (convType=="dec_to_bin"):
                res=bin(int(nombre))[2:]
        except  ValueError:
            return render(request,"convert/resultat.html",{"error ":"Erreur de conversion"})
        return render(request,"convert/resultat.html",{"res":res})
    return render(request,"convert/index.html")
def resultat(request):
    return render(request,"convert/resultat.html")