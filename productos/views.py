from django.shortcuts import render
from .models import Producto

# Create your views here.
def crear(request):
    if request.method == "POST":
        productos = Producto(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            precio = request.POST["precio"],
            stock = request.POST["stock"],
            registro = request.POST["registro"]
        )

        productos.save()
    return render(request, "productos/formulario.html")

def listar(request):
    productos = Producto.objects.all()
    return render(
        request,
        "productos/listar.html",
        {"productos":productos}
    )

def detalle(request,id):
    productos = Producto.objects.get(id=id)
    return render(
        request,
        "productos/detalle.html",
        {"productos":productos}
    )

def editar(request,id):
    productos = Producto.objects.get(id=id)
    
    if request.method == "POST":
        productos.nombre = request.POST["nombre"]
        productos.descripcion = request.POST["descripcion"]
        productos.precio = request.POST["precio"]
        productos.stock = request.POST["stock"]
        productos.registro = request.POST["registro"] == "True"

        productos.save()
        return render(
            request,
            "productos/detalle.html",
            {"productos":productos}
        )

    return render(
        request,
        "productos/formulario.html",
        {"productos":productos}
    )

def eliminar(request,id):
    productos = Producto.objects.get(id=id)
    productos.delete()
    return render(
        request,
        "productos/detalle.html",
        {"productos":productos}
    )



        

    #crear(ya)
    #listar(ya)
    #detalle(ya)
    #editar(ya)
    #eliminar

