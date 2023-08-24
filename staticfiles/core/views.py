from django.shortcuts import render, redirect
from .models import Project, Contact, Skills
from django.contrib import messages
# Create your views here.


def index(request):
    projects = Project.objects.all()
    skills = Skills.objects.all()
    
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['number']
        text = request.POST['text']
        
        new_message = Contact.objects.create(
            name=name,
            email = email,
            phone=phone,
            text=text   
        )
        new_message.save()
        return redirect('index')
                
    context = {
        'projects': projects,
        'skills': skills
    }
    return render(request, "index.html", context)