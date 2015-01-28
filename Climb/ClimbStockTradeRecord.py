

#!/usr/bin/python
__author__ = 'g4idrijs'
#coding:utf-8

import sys
import urllib
import datetime

def download_date(src_url,dest_file):
    download=urllib.FancyURLopener();
    download_page=download.open(src_url);
    savefile=file(dest_file,'wb+');
    while True:
        arr = download_page.read();
        if len(arr)==0:
            break;
        savefile.write(arr);
    savefile.flush();
    savefile.close();
    return

stock_code=sys.argv[1]
str_0='''http://stock.gtimg.cn/data/index.php?appn=detail&action=download&c='''
str_0=str_0 + stock_code + '&d='
date_start=datetime.datetime.strptime(sys.argv[2],'%Y-%m-%d')
if len(sys.argv)>3:
    date_end=datetime.datetime.strptime(sys.argv[3],'%Y-%m-%d')
else:
    date_end=date_start+datetime.timedelta(days=1)

while date_start<date_end: str_date="date_start.strftime('%Y%02m%02d')"
    str_url="str_0+str_date"
    str_file="stock_code" +="" &#39;_&#39;="" date_start.strftime(&#39;%y-%02m-%02d&#39;)="" &#39;.txt&#39;="" download_date(str_url,str_file)="" print="" date_start="date_start+datetime.timedelta(days=1)</pre"><br></date_end:>