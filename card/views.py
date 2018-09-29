from django.shortcuts import render
from card.models import *
from card.forms import CardInfoForm
from django.http import HttpResponse
# Create your views here.

def creatcard(request):
    if request.method == "POST":
        cardinfoform = CardInfoForm(request.POST,request.FILES)
        if cardinfoform.is_valid():
            try:
                newcard = cardinfoform.save(commit=False)
                newcard.user = request.user
                newcard.save()
                return HttpResponse("fabuchenggong")
            except:
                return HttpResponse("一个人只能发一个名片")
        else:
            return HttpResponse("xinxiyouwu")




    else:
        cardinfoform = CardInfoForm()

        return render(request,'card/createcard.html')


def cardlist(request):
    allcard = CardInfo.objects.all()

    return render(request,'card/cardlist.html',{'allcard':allcard})


def carddetail(request):
    data= request.GET
    id = data['id']
    card = CardInfo.objects.get(id=id)
    return render(request,'card/carddetail.html',{'card':card})




