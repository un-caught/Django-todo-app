from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import TodoForm
from .models import Todo

def index(request):

    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    context = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'index.html', context)


def delete(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')


def detail(request, item_id):
    item = get_object_or_404(Todo, id=item_id)
    context = {
        "item": item,
        "title": "Item Details",
    }
    return render(request, 'details.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(Todo, id=item_id)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('todo') 
    else:
        form = TodoForm(instance=item) 

    context = {
        'form': form,
        'item': item,
        'title': 'Edit Task',
    }
    return render(request, 'edit.html', context)
