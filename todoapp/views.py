from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import TodoItem

@csrf_protect
def create_todo(request):
    todos = TodoItem.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Create a new TodoItem object
        todo_item = TodoItem(title=title, description=description)

        # Save the TodoItem to the database
        todo_item.save()

        # Retrieve all todo items from the database
        todos = TodoItem.objects.all()

    return render(request, 'createtodo.html', {'todos': todos})
