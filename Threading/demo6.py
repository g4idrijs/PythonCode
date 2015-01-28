#!/usr/bin/env python
#coding:utf-8
__author__ = 'g4idrijs'
from time import ctime,sleep
def music():
    for i in range(5):
        print "listening to music. %s" %ctime()
        sleep(2)
def move():
     for i in range(5):
        print "at the movies! %s" %ctime()
        sleep(10) 
if __name__ == '__main__':
    music()
    move()
    print "all over %s" %ctime()
 
