from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring
from xml.etree.ElementTree import dump
from datetime import datetime
from lxml import etree
import httplib2
import time
import random
import string
import hashlib
import json
import os
from glob import glob
from PIL import Image

def compress(img_list):

    for img in img_list:
        imgsize = os.path.getsize(img)
        if imgsize >=1024*1024:

            with Image.open(img) as im:
                width,height = im.size
                new_width = int(width/3)
                new_height = int(height/3)
                resized_im = im.resize((new_width,new_height))
                resized_im.save(img)




import wechat.config

def my_get(url):
	h = httplib2.Http()
	resp, content = h.request(url, 'GET')
	return resp, content


def my_post(url, data):
	h = httplib2.Http()
	resp, content = h.request(url, 'POST', data.encode("utf-8"))
	return resp, content

# json样式的str ==> dict
def parse_Json2Dict(my_json):
	my_dict = json.loads(my_json)
	return my_dict

# dict ==> json样式的str
def parse_Dict2Json(my_dict):
	my_json = json.dumps(my_dict, ensure_ascii=False)
	return my_json



def get_access_token():
    # 获取 access_token 存入 WEIXIN_ACCESS_TOKEN
    if wechat.config.WEIXIN_ACCESS_TOKEN_LASTTIME == 0 or (int(
            time.time()) - wechat.config.WEIXIN_ACCESS_TOKEN_LASTTIME > wechat.config.WEIXIN_ACCESS_TOKEN_EXPIRES_IN - 300):

        resp, result = my_get(wechat.config.WEIXIN_ACCESS_TOKEN_URL)
        print(wechat.config.WEIXIN_ACCESS_TOKEN_URL)
        decodejson = parse_Json2Dict(result)
        print(decodejson)
        wechat.config.WEIXIN_ACCESS_TOKEN = str(decodejson[u'access_token'])
        wechat.config.WEIXIN_ACCESS_TOKEN_LASTTIME = int(time.time())
        wechat.config.WEIXIN_ACCESS_TOKEN_EXPIRES_IN = decodejson['expires_in']

        print("new access_token ->> " + wechat.config.WEIXIN_ACCESS_TOKEN + "---" + str(
            wechat.config.WEIXIN_ACCESS_TOKEN_LASTTIME) + "---" + str(wechat.config.WEIXIN_ACCESS_TOKEN_EXPIRES_IN))
        return wechat.config.WEIXIN_ACCESS_TOKEN
    else:
        print("old access_token ->> " + wechat.config.WEIXIN_ACCESS_TOKEN + "---" + str(
            wechat.config.WEIXIN_ACCESS_TOKEN_LASTTIME) + "---" + str(wechat.config.WEIXIN_ACCESS_TOKEN_EXPIRES_IN))
        return wechat.config.WEIXIN_ACCESS_TOKEN



def get_jsapi_ticket():
    access = get_access_token()
    url = 'https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token='+access+'&type=jsapi'

    if wechat.config.WEIXIN_LASTTIME == 0 or (int(
            time.time()) - wechat.config.WEIXIN_LASTTIME > wechat.config.WEIXIN_EXPIRES_IN - 300):

        resp, result = my_get(url)
        decodejson = parse_Json2Dict(result)

        wechat.config.WEIXIN_JSAPI_TICKET = str(decodejson[u'ticket'])
        wechat.config.WEIXIN_LASTTIME = int(time.time())
        wechat.config.WEIXIN_EXPIRES_IN = decodejson['expires_in']

        print("new jsapi ->> " + wechat.config.WEIXIN_JSAPI_TICKET + "---" + str(
            wechat.config.WEIXIN_LASTTIME) + "---" + str(wechat.config.WEIXIN_EXPIRES_IN))
        return wechat.config.WEIXIN_JSAPI_TICKET
    else:
        print("old jsapi ->> " + wechat.config.WEIXIN_JSAPI_TICKET + "---" + str(
            wechat.config.WEIXIN_LASTTIME) + "---" + str(wechat.config.WEIXIN_EXPIRES_IN))
        return wechat.config.WEIXIN_JSAPI_TICKET






class Sign:
    def __init__(self, jsapi_ticket, url):
        self.ret = {
            'nonceStr': self.__create_nonce_str(),
            'jsapi_ticket': jsapi_ticket,
            'timestamp': self.__create_timestamp(),
            'url': url
        }

    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    def __create_timestamp(self):
        return int(time.time())

    def sign(self):
        string = '&'.join(['%s=%s' % (key.lower(), self.ret[key]) for key in sorted(self.ret)])
        print (string)
        self.ret['signature'] = hashlib.sha1(string.encode("utf-8")).hexdigest()
        return self.ret

