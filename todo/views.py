from django.shortcuts import render, redirect
from .models import Task

def todo_list(request):
    if request.method == "POST":
        title = request.POST.get("title")  # Get task title from the form
        if title:
            Task.objects.create(title=title)  # Save task in the database
        return redirect("todo_list")  # Redirect to the same page after saving

    tasks = Task.objects.all()  # Retrieve all tasks
    return render(request, "todo/todo_list.html", {"tasks": tasks})
