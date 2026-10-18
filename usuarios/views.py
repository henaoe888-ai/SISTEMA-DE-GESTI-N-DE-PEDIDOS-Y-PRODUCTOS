from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def iniciar_sesion(request):

    if request.method == "POST":

        usuario = authenticate(request,
        username = request.POST["username"],
        password = request.POST["password"]
        )

        if usuario is not None:
            login(request, usuario)
            destino = request.GET.get("next", "/productos/listar/")
            return redirect(destino)

        return render(
            request,
            "usuarios/login.html",
            {"error": "Usuario o contraseña incorrectos"}
        )

    #Redirecciona si el método no es POST
    return render(
        request,
        "usuarios/login.html",
    )

def registro(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:

            return render(
                request,
                "usuarios/registro.html",
                {"error": "Las contraseñas no coinciden"}
            )

        if User.objects.filter(username=username).exists():

            return render(
                request,
                "usuarios/registro.html",
                {"error": "Ese usuario ya existe"}
            )

        usuario = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        login(request, usuario)

        return redirect("/productos/crear/")

    return render(
        request,
        "usuarios/registro.html"
    )

#Cierra sesión
def cerrar_sesion(request):
    logout(request)
    return redirect("/usuarios/login/")

        