# coding:utf-8
# 题目一： 写一个网页数据操作类。完成下面的功能：
# 提示：需要用到urllib模块
# get_httpcode()获取网页的状态码，返回结果例如：200,301,404等 类型为int
# get_htmlcontent() 获取网页的内容。返回类型:str
# get_linknum()计算网页的链接数目。
import urllib
class aWeb:
    def __init__(self, url):
        self.url = url

    def get_httpcode(self):
        return self.url.getcode()

    def get_htmlcontent(self):
        aWeb = (urllib.urlopen(self.url)).read()
        return aWeb

    def get_linknum(self):
        pass