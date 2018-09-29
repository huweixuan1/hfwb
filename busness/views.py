from django.shortcuts import render,redirect
from busness.forms import *
from django.http import HttpResponse
import os

# Create your views here.

def createbusness(request):
    if request.method =='POST':
        busness_form = BusnessForm(request.POST)
        if busness_form.is_valid():
            new_busness = busness_form.save(commit=False)
            new_busness.user = request.user
            new_busness.save()
            return redirect("busness/showbusness")
        else:
            return HttpResponse("bbbbbbbbbbbb")
    else:


        return render(request,'busness/createbusness.html')


def showbusness(request):
    allbusness = BusnessInfo.objects.all()
    return render(request,'busness/showbusness.html',{'allbusness':allbusness})

def detail(request):
    data = request.GET
    id = data['id']
    busness = BusnessInfo.objects.get(id=id)
    try:
        busimg = busness.busimg.split("**")[1:]
    except:
        busimg = []
    busdetail = busness.detail

    return render(request,'busness/detail.html',{'busness':busness,'busimg':busimg,'busdetail':busdetail})


def post_img(request):
    file_obj = request.FILES.get('avatar')
    file_path = os.path.join('static/img/', file_obj.name)

    with open(file_path, 'wb') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    return HttpResponse(file_path)

