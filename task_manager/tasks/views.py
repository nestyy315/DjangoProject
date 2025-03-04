from django.shortcuts import render, redirect
from .models import Task
from datetime import date



def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']

        # Determine status based on due date
        status = 'pending'
        if date.today() > date.fromisoformat(due_date):
            status = 'overdue'  
        elif date.today() <= date.fromisoformat(due_date):
            status = 'pending'  

        task = Task.objects.create(
            title=title,
            description=description,
            status=status,
            due_date=due_date
        )

        return redirect('task_list')
    return render(request, 'task_form.html')



def task_update(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']

        # Convert due_date to a date object
        task.due_date = date.fromisoformat(task.due_date)

        # Determine status based on due date
        if date.today() > task.due_date:
            task.status = 'Overdue'
        else:
            task.status = 'Pending' 

        if request.POST.get('completed') == 'on':
            task.status = 'completed'  # If the 'completed' checkbox is checked, mark the task as completed

        task.save()

        return redirect('task_list')
    return render(request, 'task_form.html', {'task': task})



def task_delete(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'task_confirm_delete.html', {'task': task})




# search bar function
def task_list(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameters
    tasks = Task.objects.all()  # Default to all tasks if no query is provided
    
    if query:
        # Filter tasks based on the search query in the title or description
        tasks = tasks.filter(title__icontains=query) | tasks.filter(description__icontains=query)
    
    return render(request, 'task_list.html', {'tasks': tasks, 'query': query})