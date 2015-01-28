#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'g4idrijs'

import requests
r = requests.get('http://www.wjculture.com', timeout=1)
print(r.status_code)  # 返回码
print(r.headers['content-type'])  # 返回头部信息
print(r.encoding)  # 编码信息
# print(r.text)  #内容部分（PS，由于编码问题，建议这里使用r.content）
r.content

import requests
from bs4 import BeautifulSoup
import re

def get_page(url,method="get"):
    # get html page via url
    status_code = 0
    while status_code != 200:
        if method == "get":
            r = requests.get(url)
        elif method == "post":
            r = requests.post(url)
        status_code = r.status_code
    page = r.content
    return page

def parse_csdn_geek(url):
    page = get_page(url)
    soup = BeautifulSoup(page)
    #链接
    href_list = []
    #标题
    title_list = []
    #推荐指数
    recommand_list = []
    #评论数
    comment_list = []
    #获取链接，标题，评论数目等信息
    content_info = soup.find_all("div",{'class':"content_info"})
    for item in content_info:
        href_list.append(item.h4.a['href'])
        title_list.append(item.h4.a.text)
        comment = item.findChildren()[10].text
        #commentNum = re.findall("(\d+)",comment)
        comment_list.append(comment)
    #获取推荐数目
    recommand_info = soup.find_all('div',{'class':'up_down'})
    for item in recommand_info:
        recommand_list.append(item.a.span.text)
    return (href_list,title_list,comment_list,recommand_list,)

if __name__=='__main__':
    url = "http://geek.csdn.net/"
    list1,list2,list3,list4 = parse_csdn_geek(url)
    for i in range(len(list1)):
        print '======================================'
        print u'原文链接:',list1[i],u'标题:',list2[i],u'评论数:',list3[i],u'推荐指数：',list4[i]
