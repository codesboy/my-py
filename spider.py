# 简单爬虫
from urllib import request
import re

class Spider():
    url = 'https://www.panda.tv/cate/lol'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    # root_pattern = '<div class="video-info">[\s\S]*</div>'

    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    # 获取数据
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls
    
    # 分析格式化获取到的数据
    def __analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern,html)
            number = re.findall(Spider.number_pattern,html)
            anchor = {'name':name,'number':number}
            anchors.append(anchor)
        # print(anchors[0])
        return anchors 
    
    # 数据优化
    def __refine(self,anchors):
        l = lambda anchor:{
            "name":anchor['name'][0].strip(),
            "number":anchor['number'][0]
            }

        return map(l,anchors)
    
    # 对数据进行排序
    def __sort(self,anchors):
        return sorted(anchors, key = self.__sort_seed, reverse=True) #reverse=True是倒序
    
    # 参与排序的数字
    def __sort_seed(self,anchor):
        r = re.findall('\d.+\d',anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000

        return number
    
        
    # 数据展示
    def __show(self,anchors):
        for anchor in anchors:
            print(anchor['name'] + '---' + anchor['number'])
    
    
    # 入口方法
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)
        # a =1




spider=Spider()
spider.go()