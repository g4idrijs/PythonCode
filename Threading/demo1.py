#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
 
import threading
import Queue
import sys
import urllib2
import re
import MySQLdb
 
#
# 数据库变量设置
#
DB_HOST = '127.0.0.1'
DB_USER = "XXXX"
DB_PASSWD = "XXXXXXXX"
DB_NAME = "xxxx"
 
#
# 变量设置
#
THREAD_LIMIT = 3
jobs = Queue.Queue(5)
singlelock = threading.Lock()
info = Queue.Queue()
 
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
    singlelock.acquire()        # Acquire the lock so we can print
    print "Waiting for threads to finish."
    singlelock.release()        # Release the lock
    jobs.join()              # This command waits for all threads to finish.
    # while not jobs.empty():
    #   print jobs.get()
 
def getTitle(url,time=10):
    response = urllib2.urlopen(url,timeout=time)
    html = response.read()
    response.close()
    reg = r'<title>(.*?)</title>'
    title = re.compile(reg).findall(html)
    # title = title[0].decode('gb2312','replace').encode('utf-8')
    title = title[0]
    return title
 
class spider(threading.Thread):
    def run(self):
        while 1:
            try:
                job = jobs.get(True,1)
                singlelock.acquire()
                title = getTitle(job[1])
                info.put([job[0],title], block=True, timeout=5)
                # print 'This {0} is {1}'.format(job[1],title)
                singlelock.release()
                jobs.task_done()
            except:
                break;
 
if __name__ == '__main__':
    con = None
    urls = []
    try:
        con = MySQLdb.connect(DB_HOST,DB_USER,DB_PASSWD,DB_NAME)
        cur = con.cursor()
        cur.execute('SELECT id,url FROM `table_name` WHERE `status`=0 LIMIT 10')
        rows = cur.fetchall()
        for row in rows:
            # print row
            urls.append([row[0],row[1]])
        workerbee(urls)
        while not info.empty():
            print info.get()
    finally:
        if con:
            con.close()
