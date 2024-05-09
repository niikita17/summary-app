

from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from django.contrib.auth import logout
# Create your views here.
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def makenotes(request,  subject_title, title, text):
   
    note=Note.objects.create(title=title,text=text, subject_title=subject_title, user=request.user)
    
    return redirect('allnotes')  
        
    

def list(request):
    if request.user.is_authenticated :
        mynotes=Note.objects.filter(user=request.user)
        return render(request,'notesApp/notes_list.html',{'notes':mynotes})
    else:
        return render(request,"notesApp/login.html",{})

def detail(request,pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request,'notesApp/notes_details.html',{'note':note})

