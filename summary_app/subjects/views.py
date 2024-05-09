from django.http import HttpResponse
from django.shortcuts import redirect, render



# Create your views here.
def subject_ai(request):
    
    if request.method=="POST":
        if request.user.is_authenticated :
            subject_title=request.POST.get("subject_title")
            title=request.POST.get("title")
            text=request.POST.get("text")
          
            
            return redirect('makenotes',subject_title=subject_title, title =title,  text=text)
        return HttpResponse("login first")
    return render(request,"subjects/ai.html",{})



def subject_cc(request):
    if request.method=="POST":
        if request.user.is_authenticated :
            subject_title=request.POST.get("subject_title")
            title=request.POST.get("title")
            text=request.POST.get("text")
            return redirect('makenotes',subject_title=subject_title, title =title,  text=text)
        return HttpResponse("login first")   
    return render(request,"subjects/cc.html",{})

def subject_cn(request):
    if request.method=="POST":
        if request.user.is_authenticated :
            subject_title=request.POST.get("subject_title")
            title=request.POST.get("title")
            text=request.POST.get("text")
            return redirect('makenotes',subject_title=subject_title, title =title,  text=text)
        return HttpResponse("login first")
    return render(request,"subjects/cn.html",{})


def subject_daa(request):
    if request.method=="POST":
        if request.user.is_authenticated :
            subject_title=request.POST.get("subject_title")
            title=request.POST.get("title")
            text=request.POST.get("text")       
            return redirect('makenotes',subject_title=subject_title, title =title,  text=text)
        return HttpResponse("login first")
    return render(request,"subjects/daa.html",{})


def subject_dbs(request):
    if request.method=="POST":
        if request.user.is_authenticated :
            subject_title=request.POST.get("subject_title")
            title=request.POST.get("title")
            text=request.POST.get("text")
            return redirect('makenotes',subject_title=subject_title, title =title,  text=text)
        return HttpResponse("login first")
    return render(request,"subjects/dbs.html",{})


def subject_se(request):
    if request.method=="POST":
        if request.user.is_authenticated :
            subject_title=request.POST.get("subject_title")
            title=request.POST.get("title")
            text=request.POST.get("text")                     
            return redirect('makenotes',subject_title=subject_title, title =title,  text=text)
        return HttpResponse("login first")
    return render(request,"subjects/se.html",{})

def subject_oops(request):
    if request.method=="POST":
        if request.user.is_authenticated :
            subject_title=request.POST.get("subject_title")
            title=request.POST.get("title")
            text=request.POST.get("text")                    
            return redirect('makenotes',subject_title=subject_title, title =title,  text=text)
        return HttpResponse("login first")
    return render(request,"subjects/oops.html",{})

def subject_ml(request):
    if request.method=="POST":
        if request.user.is_authenticated :
            subject_title=request.POST.get("subject_title")
            title=request.POST.get("title")
            text=request.POST.get("text")                      
            return redirect('makenotes',subject_title=subject_title, title =title,  text=text)
        return HttpResponse("login first")
    return render(request,"subjects/ml.html",{})

def subject_os(request):
    if request.method=="POST":
        if request.user.is_authenticated :
            subject_title=request.POST.get("subject_title")
            title=request.POST.get("title")
            text=request.POST.get("text")                   
            return redirect('makenotes',subject_title=subject_title, title =title,  text=text)
        return HttpResponse("login first")
    return render(request,"subjects/os.html",{})


def subject_dsa(request):
    if request.method=="POST":
        if request.user.is_authenticated :
            subject_title=request.POST.get("subject_title")
            title=request.POST.get("title")
            text=request.POST.get("text")           
            return redirect('makenotes',subject_title=subject_title, title =title,  text=text)
        return HttpResponse("login first")
    return render(request,"subjects/dsa.html",{})    
