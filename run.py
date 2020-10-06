#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020-10-04 13:17
# @Author   :wangqinghua
# @File     : run.py
# @Software : PyCharm


# from Actual_practice.case_one.http_request_01 import HttpRequest
# from Actual_practice.case_one.du_excel import Doexcel
#
# # 第一个表单 验证登录
# def run(test_data):  # 两种方法 1.索引 2.嵌套
#     # for item in test_data:
#     #     print("正在测试的用例是:{}".format(item['title']))
#     #     res = HttpRequest().http_request(item['url'], eval(item['data']), item['http_method'])
#     #     print("请求的结果是:{}".format(res.json()))
#     #     Doexcel().write_back(r"E:\tmp\jichuke\Actual_practice\case_one\test.xlsx","login",item["case_id"]+1,str(res.json()))
#     for i in range(len(test_data)):
#         print("正在测试的用例是:{}".format(test_data[i]['title']))
#         res = HttpRequest().http_request(test_data[i]['url'], eval(test_data[i]['data']), test_data[i]['http_method'])
#         print("请求的结果是:{}".format(res.json()))
#         Doexcel().write_back(r"E:\tmp\jichuke\Actual_practice\case_one\test.xlsx","login",i+2,str(res.json()))  # 第一个表单
#

# # test_data = [{"url":"http://localhost:8066/api/mgr/loginReq",
# #               "data":{"username": "auto", "password": "sdfsdfsdf"},"title":"正常登录","http_method":"post"},
# #         {"url": "http://localhost:8066/api/mgr/loginReq",
# #          "data": {"username": "auto", "password": "sdfssdf"},"title": "登录密码错误", "http_method": "post"},
# #         {"url": "http://localhost:8066/api/mgr/loginReq",
# #          "data": {"username": "auto", "password": ""},"title": "登录密码为空", "http_method": "post"},
# #         {"url": "http://localhost:8066/api/mgr/loginReq",
# #          "data": {"username": "auo", "password": "sdfsdfsdf"},"title": "登录账号错误", "http_method": "post"}]
#
# test_data = Doexcel().get_data(r"E:\tmp\jichuke\Actual_practice\case_one\test.xlsx","login")

# run(test_data)







from Actual_practice.case_one.http_request_01 import HttpRequest
from Actual_practice.case_one.du_excel import Doexcel

# 第二个表单 验证创建课程
COOKIE=None
def run(test_data,sheet_name):  # 两种方法 1.索引 2.嵌套
    global COOKIE
    for i in range(len(test_data)):
        print("正在测试的用例是:{}".format(test_data[i]['title']))

        res = HttpRequest().http_request(test_data[i]['url'], eval(test_data[i]['data']), test_data[i]['http_method'],COOKIE)
        if res.cookies:
            COOKIE=res.cookies
        print("请求的结果是:{}".format(res.json()))
        Doexcel().write_back(r"E:\tmp\jichuke\Actual_practice\case_one\test.xlsx",sheet_name,i+2,str(res.json()))  # 第一个表单




test_data = Doexcel().get_data(r"E:\tmp\jichuke\Actual_practice\case_one\test.xlsx","add")

run(test_data,"add")







