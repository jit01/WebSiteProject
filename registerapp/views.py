
# Ajit Edited BY cloning This Projet into the Pycharm
from django.shortcuts import render, redirect
from .models import regmodel
from .forms import refrom,loginform
from django.http.response import HttpResponse




def registration(request):
    if request.method=='POST':
        form=refrom(request.POST)
        if form.is_valid():
            form.save()
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
            raise ("Please Check the credintiality ")

    else:
        form=loginform()
        return render(request,'login.html',{'form':form})

def result(request):
    num = request.POST.get('btn')
    num1 = request.POST.get('invite')
    row = request.POST.getlist('checks')

    if num == 'single':
        return render(request,'singlethankyou.html')
    if num == 'group':
        return HttpResponse("Grp Calling successful")
    if num == 'Invite':
        data = regmodel.objects.all()
        return render(request, 'invite.html',{'data':data})
    if num1 == 'invite':
        # return HttpResponse("Invited")
        a=[]
        req_to_user = request.POST.getlist('checks[]')
        if req_to_user:
            # all_user = regmodel.objects.filter(username=req_to_user)
            #       # return HttpResponse(all_user)
            # data1 = regmodel.objects.all()
            # data2 = regmodel.objects.filter(username=req_to_user)
            # if data1 == data2:
            a.append(req_to_user)
            # return HttpResponse(a)


        else:
            return HttpResponse("Please choose The user")
    else:
        return HttpResponse("No operation")






