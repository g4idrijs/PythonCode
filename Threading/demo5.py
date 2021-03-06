#!/usr/bin/env python
#coding:utf-8
__author__ = 'g4idrijs'

import urllib2
import re
import threading
import time
import random 
rawProxyList = []
checkedProxyList = []
imgurl_list = [] 
#抓取代理网站
portdicts ={'v':"3",'m':"4",'a':"2",'l':"9",'q':"0",'b':"5",'i':"7",'w':"6",'r':"8",'c':"1"}
targets = []
for i in xrange(1,9):
        target = r"http://www.cnproxy.com/proxy%d.html" % i
        targets.append(target)
#print targets 
#抓取代理服务器正则
p = re.compile(r'''<tr><td>(.+?)<SCRIPT type=text/javascript>document.write\(":"\+(.+?)\)</SCRIPT></td><td>(.+?)</td><td>.+?</td><td>(.+?)</td></tr>''') 
#获取代理的类
class ProxyGet(threading.Thread):
        def __init__(self,target):
                threading.Thread.__init__(self)
                self.target = target
        def getProxy(self):
                print "代理服务器目标网站： " + self.target
        req = urllib2.urlopen(self.target)
        result = req.read()
        #print chardet.detect(result)
        matchs = p.findall(result)
        for row in matchs:
            ip=row[0]
            port =row[1]
            port = map(lambda x:portdicts[x],port.split('+'))
            port = ''.join(port)
            agent = row[2]
            addr = row[3].decode("cp936").encode("utf-8")
            proxy = [ip,port,addr]
            #print proxy
            rawProxyList.append(proxy)
            def run(self):
                    self.getProxy() 
#检验代理的类
class ProxyCheck(threading.Thread):
        def __init__(self,proxyList):
                threading.Thread.__init__(self)
                self.proxyList = proxyList
                self.timeout = 5
                self.testUrl = "http://www.baidu.com/"
                self.testStr = "030173"
        def checkProxy(self):
                cookies = urllib2.HTTPCookieProcessor()
        for proxy in self.proxyList:
            proxyHandler = urllib2.ProxyHandler({"http" : r'http://%s:%s' %(proxy[0],proxy[1])})
            #print r'http://%s:%s' %(proxy[0],proxy[1])
            opener = urllib2.build_opener(cookies,proxyHandler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')] 
            #urllib2.install_opener(opener)
            t1 = time.time()
            try:
                #req = urllib2.urlopen("http://www.baidu.com", timeout=self.timeout)
                req = opener.open(self.testUrl, timeout=self.timeout)
                #print "urlopen is ok...."
                result = req.read()
                #print "read html...."
                timeused = time.time() - t1
                pos = result.find(self.testStr)
                #print "pos is %s" %pos 
                if pos > 1:
                    checkedProxyList.append((proxy[0],proxy[1],proxy[2],timeused))
                    #print "ok ip: %s %s %s %s" %(proxy[0],proxy[1],proxy[2],timeused)
                else:
                     continue
            except Exception,e:
                #print e.message
                continue
        def run(self):
                self.checkProxy() 
#获取图片地址函数
def imgurlList(url_home):
    global imgurl_list
    home_page = urllib2.urlopen(url_home)
    url_re = re.compile(r'<li><a href="(.+?)" target="_blank" rel="nofollow">')
    pic_re = re.compile(r'<img src="(.*?\.\w{3,4})"')
    url_list = re.findall(url_re,home_page.read())
    for url in url_list:
        #print url_home+url
        url_page = urllib2.urlopen(url_home+url)
        for imgurlList in re.findall(pic_re,url_page.read()):
            imgurl_list.append(imgurlList) 
#下载图片的类
class getPic(threading.Thread):
    def __init__(self,imgurl_list):
        threading.Thread.__init__(self)
        self.imgurl_list = imgurl_list 
        self.timeout = 5
    def downloadimg(self):
        for imgurl in self.imgurl_list:
            pic_suffix = imgurl.split('.')[-1] #获取图片后缀
            pic_name = str(random.randint(0,10000000000))+'.'+pic_suffix
            cookies = urllib2.HTTPCookieProcessor()
            randomCheckedProxy = random.choice(checkedProxyList) #随机取一组代理服务器
            proxyHandler = urllib2.ProxyHandler({"http" : r'http://%s:%s' %(randomCheckedProxy[0],randomCheckedProxy[1])})
            opener = urllib2.build_opener(cookies,proxyHandler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')]
            urllib2.install_opener(opener)
            try:
                data_img = opener.open(imgurl,timeout=self.timeout)
                f = open (pic_name,'wb')
                f.write(data_img.read())
                f.close()
            except:
                continue
    def run(self):
        self.downloadimg() 
if __name__ == "__main__":
    getThreads = []
    checkThreads = []
    imgurlList('http://www.ivsky.com')
    getPicThreads = [] 
#对每个目标网站开启一个线程负责抓取代理
for i in range(len(targets)):
    t = ProxyGet(targets[i])
    getThreads.append(t)
for i in range(len(getThreads)):
    getThreads[i].start() 
for i in range(len(getThreads)):
    getThreads[i].join()
    print '.'*10+"总共抓取了%s个代理" %len(rawProxyList) +'.'*10 
##开启20个线程负责校验，将抓取到的代理分成20份，每个线程校验一份
for i in range(20):
    t = ProxyCheck(rawProxyList[((len(rawProxyList)+19)/20) * i:((len(rawProxyList)+19)/20) * (i+1)])
    checkThreads.append(t) 
for i in range(len(checkThreads)):
    checkThreads[i].start() 
for i in range(len(checkThreads)):
    checkThreads[i].join()
    print '.'*10+"总共有%s个代理通过校验" %len(checkedProxyList) +'.'*10 
#开启20个线程随机取一个代理下载图片
for i in range(20):
    t = getPic(imgurl_list[((len(imgurl_list)+19)/20) * i:((len(imgurl_list)+19)/20) * (i+1)])
    getPicThreads.append(t) 
for i in range(len(getPicThreads)):
    getPicThreads[i].start() 
for i in range(len(getPicThreads)):
    getPicThreads[i].join()
    print '.'*10+"总共有%s个图片下载" %len(imgurl_list) +'.'*10 
 #代理排序持久化
f= open("proxy_list.txt",'w+')
for proxy in sorted(checkedProxyList,cmp=lambda x,y:cmp(x[3],y[3])):
    #print "checked proxy is: %s:%s\t%s\t%s" %(proxy[0],proxy[1],proxy[2],proxy[3])
    f.write("%s:%s\t%s\t%s\n"%(proxy[0],proxy[1],proxy[2],proxy[3]))
f.close() 
