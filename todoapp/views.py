from django.shortcuts import render, redirect

# Create your views here.
from todoapp.models import Tarea
from categorias.models import Categoria


def tareas(request):  # the index view
    mis_tareas = Tarea.objects.all()  # quering all todos with the object manager
    # getting all categories with object manager
    categorias = Categoria.objects.all()

    if request.method == "GET":
        return render(request, "todoapp/index.html", {"tareas": mis_tareas, "categorias": categorias})
    if request.method == "POST":  # revisar si el método de la request es POST
        # verificar si la request es para agregar una tarea (esto está definido en el button)
        if "taskAdd" in request.POST:
            titulo = request.POST["titulo"]  # titulo de la tarea

            # nombre de la categoria
            nombre_categoria = request.POST["selector_categoria"]
            # buscar la categoría en la base de datos
            categoria = Categoria.objects.get(nombre=nombre_categoria)

            contenido = request.POST["contenido"]  # contenido de la tarea

            nueva_tarea = Tarea(titulo=titulo, contenido=contenido,
                                categoria=categoria)  # Crear la tarea
            nueva_tarea.save()  # guardar la tarea en la base de datos.
            print(request.POST)
            return redirect("/tareas")  # recargar la página.
        if "taskDelete" in request.POST:
            ids = request.POST["checkedbox"]
            for id in ids:
                tarea_a_eliminar = Tarea.objects.get(id=id)
                tarea_a_eliminar.delete()
                return redirect("/tareas")
            