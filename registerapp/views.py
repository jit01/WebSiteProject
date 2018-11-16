from django.shortcuts import render, redirect
from .models import regmodel
from .forms import refrom,loginform
from django.http.response import HttpResponse

def registration(request):
    if request.method=='POST':
        form=refrom(request.POST)
        if form.is_valid():
            form.save()
            # fname=request.POST.get('fname','')
            # lname=request.POST.get('lname','')
            # email=request.POST.get('email','')
            # contact=request.POST.get('contact','')
            #
            # a=regmodel(
            #     fname=fname,
            #     lname=lname,
            #     email=email,
            #     contact=contact
            # )
            # a.save()

            return redirect('./')
        else:
            return HttpResponse('Error while inserting...')


    else:
        form=refrom()
        return render(request,'reg.html',{'form':form})
def Login(request):
    if request.method=='POST':
        form=loginform(request.POST)
        if form.is_valid():
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            dbuser=regmodel.objects.filter(username=username, password=password)
            if dbuser:
                return render(request,'home.html',{'user':username})
            else:
                return HttpResponse("Error To Login")

    else:
        form=loginform()
        return render(request,'login.html',{'form':form})




