from django.http import HttpResponse
from django.shortcuts import render
from .forms import *


# Create your views here.
def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print('yoh')


    form = ContactForm()
    return render(request,"form.html", {'form':form})

def snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid:
           
            print("saved to database!")
            form.save()

    form = SnippetForm()
    return render(request,"form.html", {'form':form})
