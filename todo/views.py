<<<<<<< HEAD
from django.shortcuts import render, redirect
from .models import Item

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')
=======
from django.shortcuts import render

# Create your views here.
def get_todo_list(request):
    return render(request, 'todo/todo_list.html')
>>>>>>> dcd57c3c14521a21b06f0666fe572aa84a7c56ab
