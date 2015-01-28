#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'g4idrijs'
 
import threading,Queue,sys,urllib2,re
#
# 变量设置
#
THREAD_LIMIT = 1        #设置线程数
jobs = Queue.Queue(5)      #设置队列长度
singlelock = threading.Lock()    #设置一个线程锁,避免重复调用
 
urls = ['http://games.sina.com.cn/w/n/2013-04-28/1634703505.shtml',
        'http://games.sina.com.cn/w/n/2013-04-28/1246703487.shtml',
        'http://games.sina.com.cn/w/n/2013-04-28/1028703471.shtml',
        'http://games.sina.com.cn/w/n/2013-04-27/1015703426.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1554703373.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1512703346.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1453703334.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1451703333.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1445703329.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1434703322.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1433703321.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1433703320.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1429703318.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1429703317.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1409703297.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1406703296.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1402703292.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1353703286.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1348703284.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1327703275.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1239703265.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1238703264.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1231703262.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1229703261.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1228703260.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1223703259.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1218703258.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1202703254.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1159703251.shtml',
        'http://games.sina.com.cn/w/n/2013-04-26/1139703233.shtml']

def workerbee(inputlist):
  for x in xrange(THREAD_LIMIT):
    print 'Thead {0} started.'.format(x)
    t = spider()
    t.start()
  for i in inputlist:
    try:
      jobs.put(i, block=True, timeout=5)
    except:
      singlelock.acquire()
      print "The queue is full !"
      singlelock.release()
 
  # Wait for the threads to finish
  singlelock.acquire()    # Acquire the lock so we can print
  print "Waiting for threads to finish."
  singlelock.release()    # Release the lock
  jobs.join()       # This command waits for all threads to finish.
  # while not jobs.empty():
  #  print jobs.get()
 
def getTitle(url,time=10):
  response = urllib2.urlopen(url,timeout=time)
  html = response.read()
  response.close()
  reg = r'<title>(.*?)</title>'
  title = re.compile(reg).findall(html)
  title = title[0].decode('gb2312','replace').encode('utf-8')
  return title
 
class spider(threading.Thread):
  def run(self):
    while 1:
      try:
        job = jobs.get(True,1)
        singlelock.acquire()
        title = getTitle(job)
        print 'This {0} is {1}'.format(job,title)
        singlelock.release()
        jobs.task_done()
      except:
        break;
 
if __name__ == '__main__':
  workerbee(urls)
