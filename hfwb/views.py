from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import hashlib
from django.views.decorators.csrf import csrf_exempt
from lxml import etree
from wechat.functions import *
from wechat.config import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from wechat.models import UserInfo,JobInfo,Total
from django.contrib.auth import authenticate,login

@csrf_exempt
def index(request):

    if request.method =="GET":
        signature = request.GET.get("signature",None)
        timestamp = request.GET.get("timestamp",None)
        nonce = request.GET.get("nonce",None)
        echostr = request.GET.get("echostr",None)

        token = "hu1234"
        range_dict = [token,timestamp,nonce]
        range_dict.sort()
        range_str = "%s%s%s" % tuple(range_dict)
        range_str = hashlib.sha1(range_str.encode("utf-8")).hexdigest()
        if range_str == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("111")
    if request.method =="POST":
        str_xml = request.body.decode("utf-8")
        # print(str_xml)
        xml = etree.fromstring(str_xml)
        # print(xml)
        toUserName = xml.find('ToUserName').text
        #print(toUserName)

        fromUserName = xml.find('FromUserName').text
        createTime = xml.find('CreateTime').text
        msgType = xml.find('MsgType').text
        content = xml.find('Content').text  # 获得用户所输入的内容
        msgId = xml.find('MsgId').text
        return render(request, 'reply_text.xml',
                      {'toUserName': fromUserName,
                       'fromUserName': toUserName,
                       'createTime': '1533890692',
                       'msgType': msgType,
                       'content': content,
                       },
                      content_type='application/xml'
                      )

@csrf_exempt
def create_ms(request):
    "在微信公共号中创建菜单，这个请求是要我们主动发起的"
    menu_data = {}
    button1 = {}
    button1["name"] = "掌上微帮"
    button1["type"] = "view"
    button1["url"] = HOME_URL

    menu_data['button'] = [button1]

    post_url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=' + get_access_token()
    post_data = parse_Dict2Json(menu_data)
    resp, content = my_post(post_url, post_data)
    response = parse_Json2Dict(content)
    # print(response)
    return HttpResponse("111")

@login_required(login_url=CREATE_MENU_URL)
def home(request):
    totals = Total.objects.order_by("-time")
    datas = []
    for total in totals:
        comment = total.comment.all()
        reply = total.reply.all()
        try:

            img = total.img.split("**")[1:]
        except:
            img = []


        json1 = {'total':total,'comment':comment,'reply':reply,'img':img}
        datas.append(json1)



    return render(request,'ouxinlixue/index.html',{'datas':datas})


def create(request):
    return render(request,'create.html')


def userinfo(request):
    "获取用户 openid 判定 ID 是否是认证用户来跳转不同的页面"
    # http://www.cnblogs.com/txw1958/p/weixin71-oauth20.html
    code = request.GET.get("code", "")
    state = request.GET.get("state", "")

    if code == '':
        return HttpResponse('非法访问...')

    access_token_url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid='+WEIXIN_APPID+'&secret='+WEIXIN_APPSECRET+'&code='+code+'&grant_type=authorization_code'
    resp,data = my_get(access_token_url)

    # print(parse_Json2Dict(data))
    ACCESS_TOKEN = parse_Json2Dict(data)['access_token']
    OPENID = parse_Json2Dict(data)['openid']
    userinfo_url = 'https://api.weixin.qq.com/sns/userinfo?access_token='+ACCESS_TOKEN+'&openid='+OPENID+'&lang=zh_CN'
    resp2,data2 = my_get(userinfo_url)

    # print(parse_Json2Dict(data2))
    userinfo = parse_Json2Dict(data2)

    try:

        User.objects.get(username=userinfo['openid'])
        us = authenticate(username=userinfo['openid'], password="123456789")
    except:

        User.objects.create_user(username=userinfo['openid'],password="123456789",first_name=userinfo['nickname'])
        user = User.objects.get(username=userinfo['openid'])
        UserInfo.objects.create(user=user,openid=userinfo['openid'],sex=userinfo['sex'],city=userinfo['city'],province=userinfo['province'],headimgurl=userinfo['headimgurl'])
        us = authenticate(username=userinfo['openid'],password="123456789")
    # print("222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222")
    # print('111111111111111',us)
    login(request,us)

    #return HttpResponse("11111")
    return HttpResponseRedirect('/home/')



