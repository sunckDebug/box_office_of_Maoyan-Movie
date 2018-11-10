import requests,json
import random
from header import *
# from lxml import etree
import time


def data_analysis(data):
    datetime = data.json()["data"]["updateInfo"]
    date = data.json()["data"]["list"]
    # date = data.json()["data"]["list"][1]


    print(datetime)#当前日期时间
    # print(date)
    # print(date['movieName'])#片名
    # print(date['releaseInfo'],date['sumBoxInfo'])#上映n天票房

    # print(date['boxInfo'])#综合票房
    # print(date['boxRate'])#票房占比
    # print(date['showInfo'])#拍片场次
    # print(date['showRate'])#拍片占比
    # print(date['avgShowView'])#场均人次
    # print(date['avgSeatView'])#上座率

    with open('0723.json','wb') as f:
        data = {'当前时间':datetime}
        times = json.dumps(data,ensure_ascii=False)+"\n"
        f.write(times.encode("utf-8"))
        for i in date:
            print('片名:%s %s:%s 综合票房:%s 票房占比:%s 拍片场次:%s 拍片占比:%s 场均人次:%s 上座率:%s' % \
                (i['movieName'],i['releaseInfo'],i['sumBoxInfo'],i['boxInfo'],i['boxRate'],\
                    i['showInfo'],i['showRate'],i['avgShowView'],i['avgSeatView']))
            print()

            data = {'片名':i['movieName'],i['releaseInfo']:i['sumBoxInfo'],\
                    '综合票房':i['boxInfo'],'票房占比':i['boxRate'],\
                    '拍片场次':i['showInfo'],'拍片占比':i['showRate'],\
                    '场均人次':i['avgShowView'],'上座率':i['avgSeatView']}
            text = json.dumps(data,ensure_ascii=False)+"\n"
            #写到文件中编码设置为utf-8
            f.write(text.encode("utf-8"))
    f.close()


def Query(url):
    print(url) 
    # 主要是获取user-agent，伪装成浏览器，其它的可要，可不要
    h_random = random.choice(header)#header是请求头
    web_data = requests.get(url, headers=h_random, timeout = 1)
    return web_data

data = Query("https://box.maoyan.com/promovie/api/box/second.json")
data_analysis(data)














# def select(data):
    
#     # 初始化 标椎化
#     string = etree.HTML(data)
#     # 提取我们想要的
#     for i in range(1,30):
#         list1 = string.xpath('//*[@id="content"]/div/div[1]/div/table[{}]/tr/td[2]/div[1]/a/@title'.format(i))
#         # list2 = string.xpath('//*[@id="content"]/div/div[1]/div/table[2]/tr/td[2]/div[1]/a/@title')
#         print(list1)
#         time.sleep(0.2)

#     # list1 = string.xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/table/tr[1]/td[1]/div/div[2]/p[1]/text()')
#     print(list1)

# select(data)


# ******************************************************************************************************************


# # coding=utf-8
# from bs4 import BeautifulSoup as bs
# from urllib.error import HTTPError
# from urllib.request import urlopen
# import json
# import pygal
# # 打开网页，获取源码
# def open_page(url):
#     try:
#         netword=urlopen(url)
#     except HTTPError as hp:
#         print(hp)
#     else:
#     # 采用BeautifulSoup来解析，且指定解析器
#         html=bs(netword,'lxml')
#         return html
 
# # 获取网页数据 
# def get_page(url):
#     # 电影名称，上映天数，电影总票房，票房占比，排片场次，排片占比，场均人次，上座率 
#     movieName,releaseInfo,sumBoxInfo,boxInfo,boxRate,showInfo,showRate,avgShowView,avgSeatView=[],[],[],[],[],[],[],[],[]
#     html=open_page(url)
#     print(html)
#     p=html.find('p')
#     text=p.get_text()
#     # 将数据转换为python能够处理的格式
#     jsonObj=json.loads(text)
#     # 获取字典里面特定的键对应的键值
#     data=jsonObj.get('data')
#     # 想要的数据就在字典的键"list"对应的值
#     lists=data.get('list')
#     # print(type(lists)==type([]))判断类型
#     for list in lists:
#         # 获取字典里面特定的键对应的键值,并存储到列表中去
#         movieName.append(list.get('movieName'))
#         releaseInfo.append(list.get('releaseInfo'))
#         sumBoxInfo.append(list.get('sumBoxInfo'))
#         boxInfo.append(list.get('boxInfo'))
#         boxRate.append(list.get('boxRate'))
#         showInfo.append(list.get('showInfo'))
#         showRate.append(list.get('showRate'))
#         avgShowView.append(list.get('avgShowView'))
#         avgSeatView.append(list.get('avgSeatView'))
#     return movieName,releaseInfo,sumBoxInfo,boxInfo,boxRate,showInfo,showRate,avgShowView,avgSeatView
 
# # 利用pygal可视化数据
# # 1-画出数据图.svg
# def creat_BoxInfo(movieName,sumBoxInfo,title):
#     # 设置坐标的旋转角度
#     sum_pl=pygal.Bar(x_label_rotation=45,show_legend=False)
#     sum_pl.title=title+"(万)"
#     sum_pl.x_labels=movieName
#     sum_pl.add('',sumBoxInfo)
#     sum_pl.render_to_file('猫眼电影'+title+'.svg')
 
# # 处理总票房数据
# def  get_piaofang(sumBoxInfos):
#     # 列表存放处理的票房数据
#     sumBoxInfos_piaofang=[]
#     for sumBoxInfo in sumBoxInfos:
#         # 找到票房里面的中文的索引值
#         index_yi=sumBoxInfo.find('亿')
#         index_wan=sumBoxInfo.find('万')
#         if index_yi != -1:
#             # 对数据进行切片，而且字符串数据中存在点(.),不能直接转换为int，先转为float
#             sumBoxInfo=int(float(sumBoxInfo[:index_yi])*10000000)/10000
#             sumBoxInfos_piaofang.append(sumBoxInfo)
#         elif index_wan !=-1:
#             sumBoxInfo=int(float(sumBoxInfo[:index_yi])*10000)/10000
#             sumBoxInfos_piaofang.append(sumBoxInfo)
#     return sumBoxInfos_piaofang
 
# # 处理综合票房数据
# def get_boxInfos_general_piaofang(boxInfos):
#     boxInfos_piaofang=[]
#     for boxInfo in boxInfos:
#         boxInfos_piaofang.append(int(float(boxInfo)*10000)/10000)
#     return boxInfos_piaofang
 
# url='https://box.maoyan.com/promovie/api/box/second.json'
# movieName,releaseInfo,sumBoxInfos,boxInfos,boxRate,showInfo,showRate,avgShowView,avgSeatView=get_page(url)
# sumBoxInfos_piaofang=get_piaofang(sumBoxInfos)
# boxInfos_piaofang=get_boxInfos_general_piaofang(boxInfos)
# creat_BoxInfo(movieName,sumBoxInfos_piaofang,'票房')
# creat_BoxInfo(movieName,boxInfos_piaofang,'综合票房')



# ******************************************************************************************************************
