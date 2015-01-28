#!/usr/bin/env python
#coding:utf-8
__author__ = 'g4idrijs'
import socket
def udpClient():
    address=('localhost',8080)
    udpClientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #创建socket
    while True:
        data=raw_input('>')
        if not data:
            break
        udpClientSocket.sendto(data,address) #发送数据
        data,addr=udpClientSocket.recvfrom(2048)
        print data
        udpClientSocket.close()

if __name__=='__main__':
    udpClient()