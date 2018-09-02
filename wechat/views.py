from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from wechat.config import *
from wechat.functions import *
import json

from wechat.models import *
from wechat.forms import JobInfoForm,House_TradeForm,CarPoolForm,Comments,Reply,User,OldCarForm,OldItemForm,LifeServiceForm,EmergencyHelpForm,LookForHelpForm,ImagesForm
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

# Create your views here.



#求职招聘视图函数
@login_required(login_url=CREATE_MENU_URL)
@csrf_exempt
def job(request,id):
    if request.method == "POST":

        job_info_form = JobInfoForm(request.POST)
        img = ''
        for key in request.FILES:
            file = request.FILES.get(key)
            file_path = os.path.join('static/img/', file.name)

            img = img+'img/'+file.name+'**'
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        if job_info_form.is_valid():
            new_jobinfo = job_info_form.save(commit=False)
            new_jobinfo.type = id
            new_jobinfo.user = request.user
            new_jobinfo.img = img
            new_jobinfo.save()

            Total.objects.create(job=new_jobinfo)
            return HttpResponse("1")
        else:
            return HttpResponse("2")

    else:

        if id =='0':
            name = "求职"
        else:
            name = "招聘"
        job_info_form = JobInfoForm(instance = request.user,initial={'type':id})
        job_tags = JobTag.objects.all()


        return render(request,"wechat/job_info.html",{
            "job_info_form":job_info_form,
            "job_tags":job_tags,
            'name':name,
            'id':id
        })



#房屋租售视图函数
@login_required(login_url=CREATE_MENU_URL)
@csrf_exempt
def house_base(request,id):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        house_trade_form = House_TradeForm(request.POST)
        img = ''
        for key in request.FILES:
            file = request.FILES.get(key)
            file_path = os.path.join('static/img/', file.name)

            img = img+'img/'+file.name+'**'
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        if house_trade_form.is_valid():
            new_house_trade = house_trade_form.save(commit=False)
            new_house_trade.type = id
            new_house_trade.user = request.user
            new_house_trade.img = img
            new_house_trade.save()
            Total.objects.create(house=new_house_trade)
            return HttpResponse("1")
        else:
            return HttpResponse("2")



    else:
        if id =='0':
            name = "房屋出租"
        elif id =="1":
            name = "房屋求租"
        elif id == "2":
            name = "旺铺转让"
        elif id == "3":
            name = "房屋出售"
        else:
            name = "房屋求购"

        house_trade_form = House_TradeForm(instance = request.user,initial=({"type":id}))

        return render(request,"wechat/house_base.html",{"house_trade_form":house_trade_form,'name':name,'id':id})

@login_required(login_url=CREATE_MENU_URL)
@csrf_exempt
def carpool(request,id):
    if request.method =="POST":
        print(request.POST)
        print(request.FILES)
        car_pool_form = CarPoolForm(request.POST)
        img = ''
        for key in request.FILES:
            file = request.FILES.get(key)
            file_path = os.path.join('static/img/', file.name)

            img = img+'img/'+file.name+'**'
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        if car_pool_form.is_valid():
            new_car_pool = car_pool_form.save(commit=False)
            new_car_pool.type = id
            new_car_pool.user = request.user
            new_car_pool.img = img
            new_car_pool.save()
            Total.objects.create(car_pool=new_car_pool)
            return HttpResponse("1")
        else:
            return HttpResponse("2")
    else:
        if id =='0':
            name = '人找车'
        else:
            name = '车找人'
        car_pool_form = CarPoolForm(initial=({"type":id}))
        print(car_pool_form.as_p())
        return render(request,"wechat/carpool.html",{"car_pool_form":car_pool_form,'name':name,'id':id})

@login_required(login_url=CREATE_MENU_URL)
@csrf_exempt
def oldcar(request):
    if request.method == "POST":
        old_car_form = OldCarForm(request.POST)
        img = ''
        for key in request.FILES:
            file = request.FILES.get(key)
            file_path = os.path.join('static/img/', file.name)

            img = img+'img/'+file.name+'**'
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        if old_car_form.is_valid():
            new_old_car = old_car_form.save(commit=False)
            new_old_car.user =request.user
            new_old_car.img = img
            new_old_car.save()
            Total.objects.create(old_car=new_old_car)
            return HttpResponse("1")
        else:
            return HttpResponse("2")

    else:
        old_car_form = OldCarForm()
        print(old_car_form.as_p())
        return render(request,"wechat/oldcar.html",{"old_car_form":old_car_form})

@login_required(login_url=CREATE_MENU_URL)
@csrf_exempt
def olditem(request):
    if request.method == "POST":
        old_item_form = OldItemForm(request.POST)
        img = ''
        for key in request.FILES:
            file = request.FILES.get(key)
            file_path = os.path.join('static/img/', file.name)

            img = img+'img/'+file.name+'**'
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        if old_item_form.is_valid():
            new_item = old_item_form.save(commit=False)
            new_item.user = request.user
            new_item.img = img
            new_item.save()
            Total.objects.create(old_item=new_item)
            return HttpResponse("1")
        else:
            return HttpResponse("2")

    else:
        old_item_form = OldItemForm()

        return render(request, "wechat/olditem.html", {"old_item_form": old_item_form})

@login_required(login_url=CREATE_MENU_URL)
@csrf_exempt
def emergencyhelp(request):
    if request.method == "POST":
        emer_help_form = EmergencyHelpForm(request.POST)
        img = ''
        for key in request.FILES:
            file = request.FILES.get(key)
            file_path = os.path.join('static/img/', file.name)

            img = img+'img/'+file.name+'**'
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        if emer_help_form.is_valid():
            new_help = emer_help_form.save(commit=False)
            new_help.user = request.user
            new_help.img = img
            new_help.save()
            Total.objects.create(eme_help=new_help)
            return HttpResponse("1")
        else:
            return HttpResponse("2")
    else:
        emer_help_form = EmergencyHelpForm()

        return render(request,"wechat/emergencyhelp.html",{"emer_help_form":emer_help_form})

@login_required(login_url=CREATE_MENU_URL)
@csrf_exempt
def lookforhelp(request):
    if request.method == "POST":
        look_help_form = LookForHelpForm(request.POST)
        img = ''


        for key in request.FILES:
            file = request.FILES.get(key)
            file_path = os.path.join('static/img/', file.name)

            img = img+'img/'+file.name+'**'
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        if look_help_form.is_valid():
            new_help = look_help_form.save(commit=False)
            new_help.user = request.user
            new_help.img = img
            new_help.save()
            Total.objects.create(look_help=new_help)
            return HttpResponse("1")

        else:
            return HttpResponse("2")

    else:
        look_help_form = LookForHelpForm()


        return render(request,"wechat/lookforhelp.html",{"look_help_form":look_help_form})



@login_required(login_url=CREATE_MENU_URL)
@csrf_exempt
def lifeservice(request,id):
    if request.method =="POST":

        life_service_form = LifeServiceForm(request.POST)
        img = ''
        for key in request.FILES:
            file = request.FILES.get(key)
            file_path = os.path.join('static/img/', file.name)

            img = img+'img/'+file.name+'**'
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        if life_service_form.is_valid():
            new_lifeservice = life_service_form.save(commit=False)
            new_lifeservice.type = id
            new_lifeservice.user = request.user
            new_lifeservice.img = img
            new_lifeservice.save()
            Total.objects.create(life_ser=new_lifeservice)
            return HttpResponse("1")
        else:
            return HttpResponse("2")

    else:
        if id =='0':
            name = "求购"
        elif id =='1':
            name = "求租"
        elif id == '2':
            name = "出租"
        else:
            name = "出售"
        life_service_form = LifeServiceForm()
        return render(request,"wechat/lifeservice.html",{"name":name,"life_service_form":life_service_form,'id':id})







#评论和回复视图函数
@login_required(login_url=CREATE_MENU_URL)
@csrf_exempt
def comment(request):
    if request.method == "POST":
        print(request.POST)
        try:
            total_id = request.POST['total_id']
            words = request.POST['words']
            total = Total.objects.get(id=total_id)
            print(total,words)
            Comments.objects.create(belong_article=total,belong_user=request.user,words=words)
            return HttpResponse("1")
        except:
            return HttpResponse("2")



@login_required(login_url=CREATE_MENU_URL)
@csrf_exempt
def reply(request):
    if request.method == "POST":
        print(request.POST)
        try:
            total_id = request.POST['total_id']
            words = request.POST['words']
            to_user = User.objects.get(first_name=request.POST['to_user'])
            total = Total.objects.get(id=total_id)

            Reply.objects.create(belong_article=total,belong_user=request.user,to_user=to_user,words=words)
            return HttpResponse("1")

        except:
            return HttpResponse("2")


#文章详情页页的视图函数
@login_required(login_url=CREATE_MENU_URL)
@csrf_exempt
def detail(request):
    data = request.GET
    name = data['name']
    userimg = data['img']
    title = data['title']
    id = request.GET['id']
    total = Total.objects.get(id = id)
    comment = total.comment.all()
    reply = total.reply.all()
    try:

        img = total.img.split("**")[0:-1]
    except:
        img = []

    return render(request,'wechat/detail.html',{'total':total,'img':img,'comment':comment,'reply':reply,'name':name,'userimg':userimg,'title':title})

#个人中心
@login_required(login_url=CREATE_MENU_URL)
@csrf_exempt
def myself(request):
    user = request.user
    return render(request,'ouxinlixue/my.html',{'user':user})



# @login_required(login_url=CREATE_MENU_URL)
# @csrf_exempt
# def ajax(request):
#     if request.method == "POST":
#         id = request.POST['id']
#         if id=='0':
#             totals = Total.objects.order_by("-time")
#         elif id =='1':
#             t = JobInfo.objects.order_by("-created")
#             totals = [t[i].total for i in range(len(t))]
#         elif id == '2':
#             t = CarPool.objects.order_by("-created")
#             totals = [t[i].total for i in range(len(t))]
#         elif id == '3':
#             t = OldCar.objects.order_by("-created")
#             totals = [t[i].total for i in range(len(t))]
#         elif id=='4':
#             t = House_Trade.objects.order_by("-created")
#             totals = [t[i].total for i in range(len(t))]
#         elif id=='5':
#             t = LifeService.objects.order_by("-created")
#             totals = [t[i].total for i in range(len(t))]
#         elif id=='6':
#             t = EmergencyHelp.objects.order_by("-created")
#             totals = [t[i].total for i in range(len(t))]
#         elif id=='7':
#             t = LookForHelp.objects.order_by("-created")
#             totals = [t[i].total for i in range(len(t))]
#
#
#         data1 = []
#         for total in totals:
#             comment = total.comment.all()
#             reply = total.reply.all()
#             try:
#
#                 img = total.img.split("**")[0:-1]
#             except:
#                 img = []
#
#             json1 = {'total': total, 'comment': comment, 'reply': reply, 'img': img}
#             data1.append(json1)
#
#         print(data1)
#
#
#
#
#
#
#         return HttpResponse({'data1':data1})











#测试代码
@csrf_exempt
def ceshi(request):
    if request.method == "POST":
        print(request.FILES)
        for key in request.FILES:
            file = request.FILES.get(key)
            file_path = os.path.join('static/img/', file.name)
            print(file_path)
            print('111111111111111111111111111')
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)



        return HttpResponse('1')

    else:
        return render(request,'ceshi.html')