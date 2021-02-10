from __future__ import (absolute_import,division,print_function,unicode_literals)

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
import json
import requests
import pygal
import webbrowser
import math 
from itertools import groupby

json_url='https://iamcsy.top/btc_close_2017.json'
response=urlopen(json_url)
req=response.read()
with open('btc_close_2017_urllib.json','wb') as f:
    f.write(req)
file_urllib=json.loads(req)
print(file_urllib)



json_url='https://iamcsy.top/btc_close_2017.json'
req=requests.get(json_url)
with open('btc_close_2017_urllib.json','wb') as f:
    # print(req.text)
    f.write(bytes(req.text,'utf-8'))
file_requests=req.json()



filename='btc_close_2017_urllib.json'
with open(filename) as f:
    btc_data=json.load(f)
for btc_dict in btc_data:
    date=btc_dict['date']
    month=int(btc_dict['month'])
    week=int(btc_dict['week'])
    weekday=btc_dict['weekday']
    close=int(float(btc_dict['close']))
    print("{} is month {} week {} ,{} , the close price is {} RMB".format(date,month,week,weekday,close))



filename='btc_close_2017_urllib.json'
with open(filename) as f:
    btc_data=json.load(f)
dates=[]
months=[]
weeks=[]
weekdays=[]
close=[]
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
line_chart=pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title='收盘价'
line_chart.x_labels=dates
N=20
line_chart.x_labels_major=dates[::N]
line_chart.add('收盘价',close)
line_chart.render_to_file('收盘价折线图.svg')
webbrowser.open("收盘价折线图.svg")



line_chart2=pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart2.title='log收盘价'
line_chart2.x_labels=dates
N=20
close_log=[math.log10(_) for _ in close]
line_chart2.add('log收盘价',close_log)
line_chart2.render_to_file('log收盘价折线图.svg')
webbrowser.open("log收盘价折线图.svg")



def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):  # 2
        y_list = [v for _, v in y]
        xy_map.append([str(x), sum(y_list) / len(y_list)])  # 3
    x_unique, y_mean = [*zip(*xy_map)]  # 4
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')
    webbrowser.open(title+".svg")
    return line_chart


idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(
    months[:idx_month], close[:idx_month], '收盘价月日均值','月日均值')
line_chart_month



idx_week = dates.index('2017-12-01')
line_chart_week = draw_line(
    weeks[1:idx_week], close[1:idx_week], '收盘价周日均值','周日均值')
line_chart_week



idx_week2 = dates.index('2017-12-11')
wd=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdays_int =[wd.index(w)+1 for w in weekdays[1:idx_week2]]
line_chart_week2 = draw_line(
    weekdays_int, close[1:idx_week2], '收盘价星期均值','星期均值')
line_chart_week2.x_labels = ['周一','周二','周三','周四','周五','周六','周日']



with open('收盘价Dashboard.html','w',encoding='utf8') as html_file:
    html_file.write('<html><head><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><title></title><link rel="stylesheet" href=""></head><body>\n')
    for svg in ['收盘价折线图.svg','log收盘价折线图.svg','收盘价月日均值.svg','收盘价周日均值.svg','收盘价星期均值.svg']:
        html_file.write('<object type="image/svg+xml" data="{0}" height="500"></object>\n<br \>'.format(svg))
    html_file.write('</body></html>')
webbrowser.open('收盘价Dashboard.html')