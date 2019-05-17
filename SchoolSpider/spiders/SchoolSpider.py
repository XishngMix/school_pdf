from scrapy import Spider
import requests, time, sys, json, os.path
from scrapy import Request
from SchoolSpider.items import SchoolspiderItem
from selenium import webdriver
from hello import *
from login import *

class SchoolSpider(Spider):
    name = 'SchoolSpider'
    start_urls = ['http://authserver.hnuahe.edu.cn/authserver/login?service=http%3A%2F%2Fehall.hnuahe.edu.cn%2Flogin%3Fservice%3Dhttp%3A%2F%2Fehall.hnuahe.edu.cn%2Fnew%2Findex.html%3Fbrowser%3Dno']


    def __init__(self):
        self.login_cookies = {}
        self.wid = []
        self.titles = []


    def check_cookietime(self):
        if os.path.exists('cookies.json') == True:
            xiugai = os.stat("cookies.json").st_mtime
            tii = time.localtime(xiugai)
            dt_niew = time.strftime("%Y%m%d%H%M%S", tii)
            dt_now = time.time()
            local_now = time.localtime(dt_now)
            dt_now = time.strftime("%Y%m%d%H%M%S", local_now)
            print(dt_niew)
            print(dt_now)
            day = int(dt_now) - int(dt_niew)
            if day > 10000:
                QMessageBox.warning(self,'警告','请重新登录')
                return Ui_Form
            else:
                print('OK')
                with open('cookies.json','r') as r:
                    str = r.read()
                    date = json.loads(str)
                    self.login_cookies = date
                    print(date)
        else:
            return Ui_Form


    def wid_list(self):
        title = forms.KEY
        data_start = forms.DATA_STAR
        data_end = forms.DATA_END

        # 部门的字典
        dep = {
            '': '',
            '1': '1000',
            '2': '6101%2C',
            '3': '6102%2C',
            '4': '6103%2C',
            '5': '6104%2C',
            '6': '6105%2C',
            '7': '6106%2C',
            '8': '6107%2C',
            '9': '6108%2C',
            '10': '6109%2C',
            '11': '6110%2C',
            '12': '6111%2C',
            '13': '6112%2C',
            '14': '6113%2C',
            '15': '6201%2C',
            '16': '6202%2C',
            '17': '6204%2C',
            '18': '6205%2C',
            '19': '6206%2C',
            '20': '6207%2C',
            '21': '6208%2C',
            '22': '6209%2C',
            '23': '6210%2C',
            '24': '6211%2C',
            '25': '6212%2C',
            '26': '6213%2C',
            '27': '6301%2C',
            '28': '6302%2C',
            '29': '6304%2C',
            '30': '6305%2C',
            '31': '6306%2C',
            '32': '6307%2C',
            '33': '6309%2C',
            '34': '6310%2C',
            '35': '6311%2C',
            '36': '6312%2C',
            '37': '6313%2C',
            '38': '6314%2C',
            '39': '6315%2C',
            '40': '6316%2C',
            '41': '6317%2C',
            '42': '6318%2C',
            '43': '6319%2C',
            '44': '6320%2C',
            '45': '6321%2C',
            '46': '6322%2C',
            '47': '6323%2C',
            '48': '6325%2C',
            '49': '6327%2C',
            '50': '6329%2C',
            '51': '6335%2C',
            '52': '6401%2C',
            '53': '6402%2C',
            '54': '6403%2C',
            '55': '6404%2C',
            '56': '6406%2C',
            '57': '6407%2C',
            '58': '6408%2C',
            '59': '6410%2C',
            '60': '6414%2C',
            '61': '6801%2C'
        }

        department = forms.DEPARTMENT
        # 栏目分类的字典
        columns = {
            '': '',
            '1': '1d55d7f3770e432fa9156992f7f5488b%2C',
            '2': 'f668f73d8eab423a80e9739ec94139fc%2C',
            '3': '05accc68d8fe4036a31ac42bcd5e6b62%2C',
        }
        column = forms.COLUNM

        # 将筛选用的网站转为python的json格式   同时为了使一页可以显示完毕，将单页面的信息改为了10000
        jsons = requests.get(
            'http://ehall.hnuahe.edu.cn/publicapp/sys/bulletin/bulletin/getAllBulletin.do?pageNum=1&pageSize=10000&title=' + title + '&columnId=' +
            columns[column] + '&deptId=' + dep[department] + '&startTime=' + data_start + '&endTime=' + data_end + '&',
            cookies=self.login_cookies).json()
        print(jsons)

        # 到达json中的aList 下
        dic = jsons.get('aList')

        # 将aList下得WID 遍历
        for WID in dic:
            wid = WID['WID']
            self.wid.append(wid)

    def start_requests(self):
        self.check_cookietime()
        self.wid_list()
        urls = []
        print('\n=\n===================\n=\n', self.login_cookies, '\n=\n===================\n=\n', self.wid, '\n=\n===================\n=\n')
        # 开始访问登录后的内容
        for wid in self.wid:
            c_url = 'http://ehall.hnuahe.edu.cn/publicapp/sys/bulletin/bulletin/getBulletinById.do?WID='+wid
            urls.append(c_url)
            # 进入XHR的页面将数据转为py json
        for url in urls:
            print(url)
            yield Request(url,cookies=self.login_cookies,callback=self.parse)



    def parse(self, response):
        jsonBody = json.loads(response.body)
        item = SchoolspiderItem()
        item['TITLE'] = jsonBody['TITLE']
        item['CONTENT'] = jsonBody['CONTENT']
        yield item
