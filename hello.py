from PyQt5 import QtCore, QtGui, QtWidgets
from scrapy import cmdline
import forms, re


class hello_mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(hello_mainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 280)

        # 关键字名称
        self.KEY_line = QtWidgets.QLineEdit(Form)
        self.KEY_line.setEnabled(False)
        self.KEY_line.setGeometry(QtCore.QRect(40, 20, 61, 20))
        self.KEY_line.setFrame(False)
        self.KEY_line.setObjectName("KEY_line")

        # 关键字输入
        self.key_input = QtWidgets.QLineEdit(Form)
        self.key_input.setGeometry(QtCore.QRect(90, 20, 165, 20))
        self.key_input.setObjectName("key_input")

        #开始时间名称
        self.stardate_line = QtWidgets.QLineEdit(Form)
        self.stardate_line.setEnabled(False)
        self.stardate_line.setGeometry(QtCore.QRect(30, 60, 71, 20))
        self.stardate_line.setFrame(False)
        self.stardate_line.setObjectName("stardate_line")

        # 开始时间输入
        self.dateEdit_start = QtWidgets.QDateEdit(Form)
        self.dateEdit_start.setGeometry(QtCore.QRect(90, 60, 165, 22))
        self.dateEdit_start.setObjectName("dateEdit_start")

        # 结束时间名称
        self.enddate_line = QtWidgets.QLineEdit(Form)
        self.enddate_line.setEnabled(False)
        self.enddate_line.setGeometry(QtCore.QRect(30, 100, 71, 20))
        self.enddate_line.setFrame(False)
        self.enddate_line.setObjectName("enddate_line")

        # 结束时间输入
        self.dateEdit_end = QtWidgets.QDateEdit(Form)
        self.dateEdit_end.setGeometry(QtCore.QRect(90, 100, 165, 22))
        self.dateEdit_end.setObjectName("dateEdit_end")

        # 部门选择名称
        self.department_line = QtWidgets.QLineEdit(Form)
        self.department_line.setEnabled(False)
        self.department_line.setGeometry(QtCore.QRect(30, 140, 71, 20))
        self.department_line.setFrame(False)
        self.department_line.setObjectName("department_line")

        # 部门选择输入
        self.comboBox_department = QtWidgets.QComboBox(Form)
        self.comboBox_department.setGeometry(QtCore.QRect(90, 140, 165, 22))
        self.comboBox_department.setObjectName("comboBox_department")

        department = ['1.党政办公室','2.党政办公室','3.组织部','4.宣传部','5.统战部','6.纪委','7.学工部','8.离退职工工作处','9.团委',
                           '10.工会','11.党委机关工委','12.党群党总支','13.行政党总支','14.科教党总支','15.人事处',
                           '16.财务处','17.教务处','18.招生就业处','19.发展规划处','20.科研处','21.保卫处',
                           '22.后勤处','23.国有资产管理处','24.实验室管理处','25.基建处','26.国际交流合作处','27.动物科技学院',
                           '28.动物医学院','29.工商管理学院','30.会计学院','31.金融学院','32.制药工程学院','33.包装与印刷工程学院',
                           '34.农林经济管理学院','35.物流与电商学院','36.工程管理学院','37.智能制造与自动化学院','38.能源与动力工程学院',
                           '39.经济贸易学院','40.信息工程学院','41.软件学院','42.文法学院','43.艺术学院','44.旅游学院',
                           '45.外国语学院','46.马克思主义学院','47.理学部','48.体育教研部','49.国际教育学院','50.大学生心理健康中心',
                           '51.食品与生物工程学院','52.图书馆','53.网络管理中心','54.学报编辑部','55.档案馆','56.医院',
                           '57.继续教育学院','58.实验研究中心','59.教学质量监控与评估办','60.高等教育研究所','61.资产公司']

        self.comboBox_department.addItems(department)

        # 栏目分类名称
        self.colunm_line = QtWidgets.QLineEdit(Form)
        self.colunm_line.setEnabled(False)
        self.colunm_line.setGeometry(QtCore.QRect(30, 180, 71, 20))
        self.colunm_line.setFrame(False)
        self.colunm_line.setObjectName("colunm_line")

        # 栏目选择输入
        self.comboBox_colunm = QtWidgets.QComboBox(Form)
        self.comboBox_colunm.setGeometry(QtCore.QRect(90, 180, 165, 22))
        self.comboBox_colunm.setObjectName("comboBox_colunm")

        colunm = ['1.学校通告', '2.部门通告','3.院系工作']
        self.comboBox_colunm.addItems(colunm)

        # 决定是否生成多个PDF
        self.checkBox_lots = QtWidgets.QCheckBox(Form)
        self.checkBox_lots.setGeometry(QtCore.QRect(180, 220, 71, 16))
        self.checkBox_lots.setObjectName("checkBox_lots")

        # 开始按钮
        self.Running = QtWidgets.QPushButton(Form)
        self.Running.setGeometry(QtCore.QRect(115, 250, 75, 23))
        self.Running.setObjectName("Running")
        self.Running.clicked.connect(self.clicked)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Check"))
        self.KEY_line.setText(_translate("Form", "关键字："))
        self.stardate_line.setText(_translate("Form", "起始时间："))
        self.enddate_line.setText(_translate("Form", "截止时间："))
        self.department_line.setText(_translate("Form", "发布部门："))
        self.colunm_line.setText(_translate("Form", "栏目分类："))
        self.checkBox_lots.setText(_translate("Form", "多PDF页"))
        self.Running.setText(_translate("Form", "Running！"))


    def clicked(self):
        forms.KEY = self.key_input.text()
        forms.DATA_STAR = self.dateEdit_start.text()

        # 起始时间的整理
        if self.dateEdit_start.text() == '2000/1/1':
            now = QtCore.QDate.currentDate()
            forms.DATA_STAR = now.toString(QtCore.Qt.ISODate)
            forms.DATA_STAR = forms.DATA_STAR[0:4]+'-01-01'
        else:
            head = self.dateEdit_start.text()[0:4]
            first = self.dateEdit_start.text()[4:]
            second = str.replace(first, "/", "-")
            forms.DATA_STAR = self.dateEdit_start.text()[0:4]+ second
            if len(second) <= 5:
                yue_day = re.findall(r"-[0-9]*",second)
                if len(yue_day[0]) <=2 and len(yue_day[1]) >2:
                    ny = yue_day[0][0]+"0"+yue_day[0][1]
                    year_1 = head + ny + yue_day[1]
                    forms.DATA_STAR = year_1
                elif len(yue_day[0]) <=2 and len(yue_day[1]) <=2:
                    day = yue_day[1][0]+"0"+yue_day[1][1]
                    ny = yue_day[0][0] + "0" + yue_day[0][1]
                    year_2 = head + ny + day
                    forms.DATA_STAR = year_2
                elif len(yue_day[0]) >=2 and len(yue_day[1]) <=2:
                    day = yue_day[1][0]+"0"+yue_day[1][1]
                    year_3 = head + yue_day[0] + day
                    forms.DATA_STAR = year_3


        # 结束时间的整理
        forms.DATA_END = self.dateEdit_end.text()
        if self.dateEdit_end.text() == '2000/1/1':
            now = QtCore.QDate.currentDate()
            forms.DATA_END = now.toString(QtCore.Qt.ISODate)
        else:
            heads = self.dateEdit_end.text()[0:4]
            firsts = self.dateEdit_end.text()[4:]
            seconds = str.replace(firsts, "/", "-")
            forms.DATA_END = self.dateEdit_end.text()[0:4]+ seconds
            if len(seconds) <= 5:
                yue_end_day = re.findall(r"-[0-9]*",seconds)
                if len(yue_end_day[0]) <=2 and len(yue_end_day[1]) >2:
                    ny = yue_end_day[0][0]+"0"+yue_end_day[0][1]
                    year_end_1 = heads + ny + yue_end_day[1]
                    forms.DATA_END = year_end_1
                elif len(yue_end_day[0]) <=2 and len(yue_end_day[1]) <=2:
                    day = yue_end_day[1][0]+"0"+yue_end_day[1][1]
                    ny = yue_end_day[0][0] + "0" + yue_end_day[0][1]
                    year_end_2 = heads + ny + day
                    forms.DATA_END = year_end_2
                elif len(yue_end_day[0]) >=2 and len(yue_end_day[1]) <=2:
                    day = yue_end_day[1][0]+"0"+yue_end_day[1][1]
                    year_end_3 = heads + yue_end_day[0] + day
                    forms.DATA_END = year_end_3


        if str.replace(forms.DATA_STAR,'-','') > str.replace(forms.DATA_END,'-',''):
            QtWidgets.QMessageBox.warning(self,'警告','起始时间大于结束时间')
            return

        if self.checkBox_lots.isChecked():
            forms.CHECKED = '是'
        else:
            forms.CHECKED = '否'

        forms.DEPARTMENT = re.findall(r"[0-9]*",self.comboBox_department.currentText())[0]
        forms.COLUNM = re.findall(r"[0-9]*",self.comboBox_colunm.currentText())[0]
        return  forms.CHECKED,forms.KEY, forms.DATA_STAR, forms.DEPARTMENT, forms.COLUNM, forms.DATA_END,self.run()

    def run(self):
        from scrapy.crawler import CrawlerProcess
        from scrapy.utils.project import get_project_settings
        from selenium import webdriver
        import requests, time, sys, json, os.path, pdfkit
        from scrapy import Request
        from scrapy import Spider

        # 必须引入的
        import scrapy.spiderloader
        import scrapy.statscollectors
        import scrapy.logformatter
        import scrapy.dupefilters
        import scrapy.squeues

        import scrapy.extensions.spiderstate
        import scrapy.extensions.corestats
        import scrapy.extensions.telnet
        import scrapy.extensions.logstats
        import scrapy.extensions.memusage
        import scrapy.extensions.memdebug
        import scrapy.extensions.feedexport
        import scrapy.extensions.closespider
        import scrapy.extensions.debug
        import scrapy.extensions.httpcache
        import scrapy.extensions.statsmailer
        import scrapy.extensions.throttle

        import scrapy.core.scheduler
        import scrapy.core.engine
        import scrapy.core.scraper
        import scrapy.core.spidermw
        import scrapy.core.downloader

        import scrapy.downloadermiddlewares.stats
        import scrapy.downloadermiddlewares.httpcache
        import scrapy.downloadermiddlewares.cookies
        import scrapy.downloadermiddlewares.useragent
        import scrapy.downloadermiddlewares.httpproxy
        import scrapy.downloadermiddlewares.ajaxcrawl
        import scrapy.downloadermiddlewares.chunked
        import scrapy.downloadermiddlewares.decompression
        import scrapy.downloadermiddlewares.defaultheaders
        import scrapy.downloadermiddlewares.downloadtimeout
        import scrapy.downloadermiddlewares.httpauth
        import scrapy.downloadermiddlewares.httpcompression
        import scrapy.downloadermiddlewares.redirect
        import scrapy.downloadermiddlewares.retry
        import scrapy.downloadermiddlewares.robotstxt

        import scrapy.spidermiddlewares.depth
        import scrapy.spidermiddlewares.httperror
        import scrapy.spidermiddlewares.offsite
        import scrapy.spidermiddlewares.referer
        import scrapy.spidermiddlewares.urllength
        import scrapy.pipelines

        import scrapy.core.downloader.handlers.http
        import scrapy.core.downloader.contextfactory

        process = CrawlerProcess(get_project_settings())

        # 'followall' is the name of one of the spiders of the project.
        process.crawl('SchoolSpider')
        process.start()  # the script will block here until the crawling is finished
        return hello_mainWindow



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = hello_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())