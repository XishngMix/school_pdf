# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pdfkit, os, forms
# from SchoolSpider.spiders import SchoolSpider
# from scrapy import Spider






class SchoolspiderPipeline(object):
    def __init__(self):
        self.pdf_power = ''


    def process_item(self, item, spider):
        if not os.path.isdir('html'):
            os.mkdir('html')
        if not os.path.isdir('pdf'):
            os.mkdir('pdf')
        if self.pdf_power.strip() == '':
            # pdf = input('需要转为多个PDF吗？（是或否）\n')
            pdf = forms.CHECKED
            self.pdf_power = pdf
        if self.pdf_power == '是':
            print('#########################获取CONTENT#########################')
            TITLE = item['TITLE']
            CONTENT = item['CONTENT']
            IMG_CONT = str.replace(CONTENT,'img','img height=1000,width=1000,')
            h1 = ('<h1 style="text-align:center">' + TITLE + '</h1>')
            all = h1 + IMG_CONT
            with open('html/{}.html'.format(TITLE), 'w', encoding='utf-8') as f:
                f.write(all)
            options = {
                'page-size': 'Letter',
                'encoding': "UTF-8",
                'custom-header': [
                    ('Accept-Encoding', 'gzip')
                ]
            }
            pdfkit.from_file('html/{}.html'.format(TITLE), 'pdf/{}.pdf'.format(TITLE), options=options)
        if self.pdf_power == '否':
            TITLE = item['TITLE']
            CONTENT = item['CONTENT']
            IMG_CONT = str.replace(CONTENT,'img','img height=350,width=400,')
            h1 = ('<h1 style="text-align:center">' + TITLE + '</h1>')
            all = h1 + IMG_CONT
            with open('html/all.html', 'a+', encoding='utf-8') as f:
                f.write(all)



    def close_spider(self,spider):
        if self.pdf_power == '否':
            print('因文件过大，请稍等')
            options = {
                'page-size': 'Letter',
                'encoding': "UTF-8",
                'custom-header': [
                    ('Accept-Encoding', 'gzip')
                ]
            }
            pdfkit.from_file('html/all.html', 'pdf/all.pdf', options=options)
            print('转换完成')
        # else:
        #     a= input("是否需要继续?（是/否）\n")
        #     if a == '是':
        #         SchoolSpider(Spider)