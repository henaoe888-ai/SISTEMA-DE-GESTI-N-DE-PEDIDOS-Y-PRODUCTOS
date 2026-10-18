from django.shortcuts import render
from .models import Pedido

# Create your views here.
def crear(request):
    if request.method == "POST":
        pedidos = Pedido(
            nombre = request.POST["nombre"],
            valor = request.POST["valor"],
            estado = request.POST["estado"],
            descripcion = request.POST["descripcion"],
            registro = request.POST["registro"]
        )

        pedidos.save()
    return render(request, "pedidos/formulario.html")

def listar(request):
    pedidos = Pedido.objects.all()
    return render(
        request,
        "pedidos/listar.html",
        {"pedidos": pedidos}
    )

def detalle(request,id):
    pedidos = Pedido.objects.get(id=id)
    return render(
        request,
        "pedidos/detalle.html",
        {"pedidos":pedidos}
    )

def editar(request,id):
    pedidos = Pedido.objects.get(id=id)
    
    if request.method == "POST":
        pedidos.nombre = request.POST["nombre"]
        pedidos.valor = request.POST["valor"]
        pedidos.estado = request.POST["estado"]
        pedidos.descripcion = request.POST["descripcion"]
        pedidos.registro = request.POST["registro"] == "True"

        pedidos.save()
        return render(
            request,
            "pedidos/detalle.html",
            {"pedidos":pedidos}
        )

    return render(
        request,
        "pedidos/formulario.html",
        {"pedidos":pedidos}
    )

def eliminar(request,id):
    pedidos = Pedido.objects.get(id=id)
    pedidos.delete()
    return render(
        request,
        "pedidos/detalle.html",
        {"pedidos":pedidos}
    )



        

    #crear(ya)
    #listar(ya)
    #detalle(ya)
    #editar(ya)
    #eliminar

