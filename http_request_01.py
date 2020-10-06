#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020-09-27 22:47
# @Author   :wangqinghua
# @File     : http_request.py
# @Software : PyCharm

import requests

class HttpRequest:

    def http_request(self,url,data,method,cookie=None):
        try:
            if method.lower()=='get':  #小写
                res = requests.get(url, data, cookies=cookie,verify=False)
            else:
                res = requests.post(url, data, cookies=cookie,verify=False)
            return res #消息实体：包含响应头 状态码 响应报文 sessid cookis信息(响应结果的响应实体)
        except Exception as e:
            print("请求报错了：{}".format(e))
            raise e

if __name__=='__main__':
    #登录
    url_login = "http://localhost:8066/api/mgr/loginReq"
    data = {"username": "auto", "password": "sdfsdfsdf"}
    res = HttpRequest().http_request(url_login,data,"post")
    print("登录的结果是:",res.json())


    #创建课程
    add_course = "http://localhost:8066/api/mgr/sq_mgr/"
    payload ={'action':'add_course',
              'data':'''{"name":"初中数学",
              "desc":"初中数学课程",
              "display_idx":4}'''}

    ress = HttpRequest().http_request(add_course,payload,'post',res.cookies)
    print("创建的课程是:",ress.json())



payload ={'action':'add_course', 'data':'''{"name":"初中数学","desc":"初中数学课程","display_idx":4}'''}