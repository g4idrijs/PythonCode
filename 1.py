#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__ = 'g4idrijs'
#1#####################################################################################################################
#i = 5;
#print(i);
#s = 'This is a string. \
#This continues the string.'
#print(s);
#2#####################################################################################################################
#import os,sys
#base = 'C:/'
#i = 1
#for j in range(2):
#    file_name = base+str(i)
#    os.mkdir(file_name)
#    i=i+1
#3#####################################################################################################################
#!/usr/bin/python
#for letter in 'Python':     # First Example
#    if letter == 'h':
#        break
#    print 'Current Letter :', letter
#
#var = 10                    # Second Example
#while var > 0:
#    print 'Current variable value :', var
#    var = var -1
#    if var == 5:
#        break
#print "Good bye!"
#4#######################################################################################################################
#import math
#dir(math)
#help(math)

#import random
#print random.uniform(10,20)
#print random.randint(10,20)
#print random.randrange(10,100,5)
#print random.choice([1,2,3,4])
#print random.choice('hello')
#a=[1,2,3,4,5]
#print random.shuffle(a)
#print random.sample(a,3)
#from decimal import Decimal
#from decimal import getcontext
#getcontext().prec = 4
#print Decimal('0.1') / Decimal('0.3')
#from fractions import Fraction
#print Fraction(16, -10)
#print  Fraction(123)
#print Fraction('3/7')
#print Fraction('-.125')
#print Fraction(2.25)
#print Fraction(Decimal('1.1'))
#print Fraction(1,2)+Fraction(1,3)
#if not (3>=2 and 3<=2):
#    print 'haha'
#else:
#    print 3>=2 or 3<=2
#print 'I\'m learning\nPython.'
#print '''line1
#... line2
#... line3'''
#5######################################################################################################################
#def printme( str ):
#    print str
#    return
#printme('hello')
#printme( str = "My string");
#
#def changeme( mylist ):
#    mylist.append([1,2,3,4]);
#    print mylist
#    return
#mylist = [10,20,30];
#changeme( mylist )
#
#def printinfo( name, age ):
#    print "Name:", name;
#    print "Age:", age;
#    return;
#printinfo( age=50, name="miki" );
#
#def printinfo( arg1, *vartuple ):
#    print arg1
#    for var in vartuple:
#        print var
#    return;
#printinfo( 10 );
#printinfo( 70, 60, 50 );
#
#sum = lambda arg1, arg2: arg1 + arg2;
#print "Value of total : ", sum( 10, 20 )
#print "Value of total : ", sum( 20, 20 )
#
#def sum( arg1, arg2 ):
#    total = arg1 + arg2
#    print "Inside the function : ", total
#    return total;
#total1 = sum( 10, 20 );
#print "Outside the function : ", total1
#
#total = 0;
#def sum( arg1, arg2 ):
#    total = arg1 + arg2;
#    print "Inside the function local total : ", total
#    return total;
#sum( 10, 20 );
#print "Outside the function global total : ", total
#6######################################################################################################################
#for letter in 'Python':     # First Example
# if letter == 'h':
#    break
#print 'Current Letter :', letter
#var = 10                    # Second Example
#while var > 0:
#    print 'Current variable value :', var
#    var = var -1
#    if var == 5:
#        break
#print "Good bye!"
#7######################################################################################################################
##########change data format##########
####way 1
#a="2013-10-10 23:40:00"
#import time
#timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
#timeStamp = int(time.mktime(timeArray))
#print timeStamp == 1381419600
#otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
#print otherStyleTime
####way 2
#import datetime
#timeStamp = 1381419600
#dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
#otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
#print otherStyleTime

##########get now time##########
####way 1
#import time
#now = int(time.time())
#timeArray = time.localtime(now)
#nowTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
#print nowTime
####way 2
#import datetime
#now = datetime.datetime.now()
#nowTime = now.strftime("%Y-%m-%d %H:%M:%S")
#print nowTime
###way 3 (2 format)
#import time
#print (time.strftime("%H:%M:%S"))
## 12 hour format #
#print (time.strftime("%I:%M:%S"))

#import time
#print (time.strftime("%d/%m/%Y"))
####get time using datatime
#import datetime
#i = datetime.datetime.now()
#print i
#print i.year
#print i.month
#print i.day
#print i.hour
#print i.minute
#print i.second
##########get time of 3 days ago##########
#import time
#import datetime
#threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 3))
#timeStamp = int(time.mktime(threeDayAgo.timetuple()))
#timeOfThatDay = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
#print timeOfThatDay

##########caculate the time before based on given timestamp
#timeStamp = 1381419600
#import datetime
#import time
#dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
#threeDayAgo = dateArray - datetime.timedelta(days = 3)
#print threeDayAgo
#8######################################################################################################################
##########use of help##########
#help('dir')
#help('sys')
#help('str')
#a = [1,2,3]
#help(a)
#help(a.append)
#9######################################################################################################################
##########use of pass##########
#for letter in 'Python':
#    if letter == 'h':
#        pass
#        #print 'This is pass block'
#    print 'Current Letter :', letter
#print "Good bye!"
#10#####################################################################################################################
##########luo han tan##########
#times = 0
#def test(num,a,b,c):
#    global times
#    if num==1:
#        print (a,b)
#        times+=1
#    else:
#        test(num-1,a,c,b)
#        test(1,a,b,c)
#        test(num-1,c,b,a)
#
#test(122,"a","b","c")
#print times
#11#####################################################################################################################
##########return multi value##########
#def __init__(self, cells):
#    self.cells, self.comments = self._parse(cells)
#def _parse(self, row):
#    data = []
#    comments = []
#    for cell in row:
#        cell = self._collapse_whitespace(cell)
#        if cell.startswith('#') and not comments:
#            comments.append(cell[1:])
#        elif comments:
#            comments.append(cell)
#        else:
#            data.append(cell)
#    return self._purge_empty_cells(data), self._purge_empty_cells(comments)
#12#####################################################################################################################
##########get website chaining##########
#import socket
#import htmllib,formatter
#def open_socket(host,servname):
#    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#    port=socket.getservbyname(servname)
#    s.connect((host,port))
#    return s
#host=''
#host=input('please input website\n')
#mysocket=open_socket(host,'http')
#message='GET http://%s/\n\n'%(host,)
#mysocket.send(message)
#file=mysocket.makefile()
#htmldata=file.read()
#file.close()
#parser=htmllib.HTMLParser(formatter.NullFormatter())
#parser.feed(htmldata)
#print '\n'.join(parser.anchorlist)
#parser.close()
#13#####################################################################################################################
#http://www.jb51.net/article/47208.htm
##########get content of website##########
#import socket
#def open_tcp_socket(remotehost,servicename):
#    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#    portnumber=socket.getservbyname(servicename,'tcp')
#    s.connect((remotehost,portnumber))
#    return s
#mysocket=open_tcp_socket('www.taobao.com','http')
#mysocket.send('usb')
#while(1):
#    data=mysocket.recv(1024)
#    if(data):
#        print data.decode('gbk').encode('utf-8')
#    else:
#        break
#mysocket.close()
#14#####################################################################################################################
#http://www.jb51.net/article/47108.htm
##########caculate lines of file##########
#import time
#def block(file,size=65536):
#    while True:
#        nb = file.read(size)
#        if not nb:
#            break
#        yield nb
#def getLineCount(filename):
#    with open(filename,"r",encoding="utf-8") as f:
#        return sum(line.count("\n") for line in block(f))
#if __name__ == "__main__":
#    import sys
#    import os
#    if len(sys.argv) != 2:
#        print("error imput argument")
#        sys.exit(-1)
#    if not os.path.isfile(sys.argv[1]) :
#        print(sys.argv + " is not a file")
#        sys.exit(-1)
#    start_time = time.time()
#    print(getLineCount(sys.argv[1]))
#    print(time.time() - start_time ,"seconds")
#15#####################################################################################################################
#http://www.jb51.net/article/47001.htm
##########login and post state in renren using python##########
#from sgmllib import SGMLParser
#import sys, urllib2, urllib, cookielib
#import datetime, time
#class spider(SGMLParser):

#    def __init__(self, email, password):
#        SGMLParser.__init__(self)

#        self.email = email
#        self.password = password
#        self.domain = 'renren.com'

#        try:
#            cookie = cookielib.CookieJar()
#            # a class to handle HTTP cookies
#            cookieProc = urllib2.HTTPCookieProcessor(cookie)
#        except:
#            raise
#        else:
#            opener = urllib2.build_opener(cookieProc)
#            urllib2.install_opener(opener)
#    def login(self):
#        print 'begin login'
#        url = 'http://www.renren.com/PLogin.do'
#        #url = 'http://www.renren.com/SysHome.do'
#        postdata = {
#            'email': self.email,
#            'password': self.password,
#            'domain': self.domain
#        }
#        req = urllib2.Request(
#            url,
#            urllib.urlencode(postdata)
#        )

#        self.file = urllib2.urlopen(req).read()
#        print self.file

#        idPos = self.file.index("'id':'")
#        self.id = self.file[idPos+6:idPos+15]

#        tokPos = self.file.index("get_check:'")
#        self.tok = self.file[tokPos+11:tokPos+21]

#        rtkPos = self.file.index("get_check_x:'")
#        self.rtk = self.file[rtkPos+13:rtkPos+21]

#    def publish(self, content):
#        url1 = 'http://shell.renren.com/' +self.id+ '/status'
#        print 'self.id = ' , self.id
#        postdata = {
#            'content': content,
#            'hostid': self.id,
#            'requestToken': self.tok,
#            '_rtk': self.rtk,
#            'channel': 'renren',
#            }
#        req1 = urllib2.Request(
#            url1,
#            urllib.urlencode(postdata)
#        )
#        self.file1 = urllib2.urlopen(req1).read()

#        print datetime.datetime.now()
#        print 'account %sposted a state' % self.email
#        print 'the content is: %s' % postdata.get('content', '')
#renrenspider = spider('g4idrijs@sina.com', 'Goooidrijs')
#renrenspider.login()
#contents = raw_input('please the content to be post:')
#contents =["1","2"]
#renrenspider.publish(content)
#content = "12"
#renrenspider.publish(content)
#renrenspider.publish(content.decode('gb2312').encode('utf-8'))
#for content in contents:
#    renrenspider.publish(content)
#16#####################################################################################################################
#http://www.jb51.net/article/46835.htm
##########seek for prim##########
#def is_sushu(num):
#    res=True
#    for x in range(2,num-1):
#        if num%x==0:
#            res=False
#            return res
#    return res
#print ([x for x in range(1000) if is_sushu(x)])
#17#####################################################################################################################
#http://www.jb51.net/article/46804.htm
##########count down##########
#import time
#count = 0
#a = input('time:')
#while (count < a):
#    ncount = a - count
#    print ncount
#    time.sleep(1)
#    count += 1
#print 'done'
#18#####################################################################################################################
#http://www.jb51.net/article/46803.htm
##########realize of order##########
#def insertion_sort(n):
#    if len(n) == 1:
#        return n
#    b = insertion_sort(n[1:])
#    m = len(b)
#    for i in range(m):
#        if n[0] <= b[i]:
#            return b[:i]+[n[0]]+b[i:]
#    return b + [n[0]]
#l = [1,3,4,2,6,7,9,7,12,11,789,345,456]
#print insertion_sort(l)
#print insertion_sort(l)
#d = input('l=')
#19#####################################################################################################################
#http://www.jb51.net/article/46343.htm
##########use of sys.argv in commend line
#import sys
#if len(sys.argv) <> 3:
#    print "Usage: " + sys.argv[0] + "file1 file2"
#    sys.exit(-1)
#file1 = sys.argv[1]
#file2 = sys.argv[2]
#list1 = {}
#for line in open(file1):
#    list1[line.split()[0]] = 1
#for line in open(file2):
#    key = line.split()[0]
#    if key not in list1:
#        sys.stdout.write(line)
#20#####################################################################################################################
#http://www.jb51.net/article/46499.htm
#########usege to realize get cookie##########
import Cookie
import datetime
import random

expiration = datetime.datetime.now() + datetime.timedelta(days=30)
cookie = Cookie.SimpleCookie()
cookie["session"] = random.randint(1,1000000000)
cookie["session"]["domain"] = ".baidu.com"
cookie["session"]["path"] = "/"
cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")

print "Content-type: text/plain"
print cookie.output()
print
print "Cookie set with: " + cookie.output()
#21#####################################################################################################################


