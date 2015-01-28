#!/usr/bin/python
#coding:utf-8
__author__ = 'g4idrijs'

from sgmllib import SGMLParser
import urllib
import urllib2
import datetime
import json
import os
from time import sleep

class cityObject(object):
	def __init__(self, abbr_pinyin="", full_pinyin="",chinaname="",shortCode=""):
		self.abbr_pinyin = abbr_pinyin
		self.full_piyin = full_pinyin
		self.chinaname = chinaname
		self.shortCode = shortCode

class trainObject(object):
	def __init__(self, tid="", code="", start_city="", start_time="", end_city="", end_time="", full_time=""):
		self.tid = tid
		self.code = code
		self.start_city = start_city
		self.start_time = start_time
		self.end_city = end_city
		self.end_time = end_time
		self.full_time = full_time

	def get_writestr(self):
		# return ("%s,%s,%s,%s,%s,%s,%s") % (self.tid, self.code, self.start_city.encode('utf-8'), self.start_time, self.end_city.encode('utf-8'), self.end_time, self.full_time)
		str_return = self.tid + ",";
		str_return += self.code + ",";
		str_return += self.start_city + ",";
		str_return += self.start_time + ",";
		str_return += self.end_city + ",";
		str_return += self.end_time + ",";
		str_return += self.full_time;
		return str_return

class trainModel(list):
	def isExist(self, train):
		for sub_train in self:
			if sub_train.code == train.code:
				return True

		return False

	def save(self):
		train = self[-1]
		with open(("%s.txt") % (train.code), "w") as wf:
			print train.get_writestr()
			wf.write(train.get_writestr().encode('utf-8'))


def parserCitys(data):
	parser_citys = []
	for original_city in data:
		if original_city and len(original_city) > 1:
			split_city = original_city.split('|')
			parser_city = cityObject(split_city[0])
			parser_citys.append(parser_city)

	print len(parser_citys)

	return parser_citys


def getBookingTrainListUrl(start_code, end_code, day):
	strUrl =  ("http://dynamic.12306.cn/otsquery/query/queryRemanentTicketAction.do?method=queryLeftTicket&")

	strUrl += ("orderRequest.train_date=%s&") % (day)
	strUrl += ("orderRequest.from_station_telecode=%s&") % (start_code)
	strUrl += ("orderRequest.to_station_telecode=%s&") % (end_code)
	strUrl += ("orderRequest.train_no=&trainPassType=QB&trainClass=QB%23D%23Z%23T%23K%23QT%23&includeStudent=00&seatTypeAndNum=&orderRequest.start_time_str=00%3A00--24%3A00")

	return strUrl

trains = trainModel()


def parser_booking_str(str_booking):
	json_book = json.loads(str_booking)
	datas = json_book['datas']
	if datas and len(datas) > 1:
		# print datas.replace("&nbsp;","")
		trainlist = datas.replace("&nbsp;","").split("\\n")
		for train_str in trainlist:
			train_str_list = train_str.split(',')

			if len(train_str_list) == 17:
				str_id_and_code = train_str_list[1]
				str_start_city_and_time = train_str_list[2]
				str_end_city_and_time = train_str_list[3]
				str_full_time = train_str_list[4]

				# print str_id_and_code
				str_id = str_id_and_code[13:25]
				str_code = str_id_and_code[131:-7]
				# print str_start_city_and_time
				if len(str_start_city_and_time) > 50:
					str_start_city = str_start_city_and_time[43:-9]
				else :
					str_start_city = str_start_city_and_time[0:-9]

				str_start_time = str_start_city_and_time[-5:]
				# print str_end_city_and_time
				if len(str_end_city_and_time) > 50:
					str_end_city = str_end_city_and_time[42:-9]
				else:
					str_end_city = str_end_city_and_time[0:-9]
				str_end_time = str_end_city_and_time[-5:]

			tobj = trainObject(str_id, str_code, str_start_city, str_start_time, str_end_city, str_end_time, str_full_time)

			if trains.isExist(tobj) == False:
				trains.append(tobj)
				trains.save()



u = urllib2.urlopen("http://dynamic.12306.cn/otsquery/js/common/station_name.js?version=1.40")
buffer = u .read()
u.close()


buffer = buffer[20:-3]
unformatter_citys = buffer.split('@')


parser_citys = parserCitys(unformatter_citys)

city_length = len(parser_citys)

today = datetime.date.today()
torrow = datetime.timedelta(days=1)
today = today + torrow

day_str = ("%s-%02d-%02d") % (today.year, int(today.month), int(today.day))

print (day_str)

strPath = os.getcwd()
os.chdir("%s/" % strPath)


for i in range(1, city_length):
	for j in range(0 , len(parser_citys) - i):
		try:
			print ("[%d %d]" % (i , j))
			sleep(0.09)
			strurl = getBookingTrainListUrl(parser_citys[i].shortCode, parser_citys[j].shortCode, day_str)

			url_add_header = urllib2.Request(strurl)
			url_add_header.add_header('X-Requested-With', "XMLHttpRequest")
			url_add_header.add_header('Referer', "http://dynamic.12306.cn/otsquery/query/queryRemanentTicketAction.do?method=init")
			url_add_header.add_header('Content-Type', 'application/x-www-form-urlencoded')
			url_add_header.add_header('Connection', 'keep-alive')

			resp = urllib2.urlopen(url_add_header)
			urlread = resp.read()
			resp.close()

			parser_booking_str(urlread)

		except urllib2.HTTPError as err:
			print ("error : [%s] url=[%s]") % (err, strurl)
			exit(1)

os.chdir(strPath)
print len(trains)