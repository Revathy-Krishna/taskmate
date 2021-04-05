from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todolist(request):
    context={
        'todo_text':'Welcome to ToDo List'
    }
    return render(request,'todolist.html',context)

def about(request):
    context = {
        'about_text': 'Welcome to About'
    }
    return render(request,'about.html',context)

def contact(request):
    context = {
        'contact_text': 'Welcome to Contact List'
    }
    return render(request,'contact.html',context)
