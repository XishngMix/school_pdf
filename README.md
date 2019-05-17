# school_pdf
通过pyqt5关联的scrapy


本程序用的是selenium == 3.0来驱动phantomJS已达到想要的目的。 
设计思路：
首先先通过scrapy建立最初的框架，以及相应的检索信息，因为需要将爬取的数据最终转换为PDF格式，所以在设置中添加了
ITEM_PIPELINES ={
    'SchoolSpider.pipelines.SchoolspiderPipeline': 300,
}

在piplines中通过迭代生成的数据来转换成HTML后再生成PDF文件。

在login.py中用selenium == 3.0来驱动 phantomJS 已达到兼容大多数教师的目的，

在hello.py中，定义QPushButton连接的效果，可以参考https://blog.csdn.net/La_vie_est_belle/article/details/79017358
