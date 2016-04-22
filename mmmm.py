# -*- coding:utf-8 -*-
import os
import urllib
import urllib2
import re
# import tool
class Spider:
    def __init__(self):
        self.siteURL = 'http://www.taobao.com'
        # self.tool = tool.Tool()
    def getPage(self,pageindex):
        url = self.siteURL+str(pageindex)+".html"
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')
    def getContents(self,pageindex):
        page = self.getPage(pageindex)
        pattern = re.compile('<div class="picbox".*?<div class="name"><a target="_blank" href="(.*?)".*?>(.*?)</a></div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            contents.append([item[0], item[1]])
        return contents
    def getDetailPage(self, infoURL):
        response = urllib2.urlopen(infoURL)
        return response.read().decode('gbk')
    # def getBrief(self, page):
    #     pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
    #     result = re.search(pattern, page)
    #     return self.tool.replace(result.group(1))
    def getAllImg(self, page):
        pattern = re.compile('<div class="list-pic".*?>(.*?)<!--',re.S)
        content = re.search(pattern, page)
        # print content.group(1)
        patternImg = re.compile('<div class="img-wrap"><a id.*?<img.*?src="(.*?)" title.*?',re.S)
        if content == None:
            return None
        images = re.findall(patternImg,content.group(1))
        return images
    def saveImgs(self, images,foldname, name):
        number = 1
        print u"发现",name,u"共有",len(images),u"张照片"
        for imageURL in images:
            splitPath = imageURL.split('.')
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = "jpg"
            fileName = foldname+ "/" +name+str(number) + "." + fTail
            self.saveImg(imageURL, fileName)
            number += 1
    def saveIcon(self, iconURL, name):
        splitPath = iconURL.split('.')
        fTail = splitPath.pop()
        fileName = name + '/icon.' + fTail
        self.saveImg(iconURL, fileName)
    # def saveBrief(selfself, content,name):
    #     fileName = name + "/" + name + ".txt"
    #     f = open(fileName, "w+")
    #     print u"正在偷偷保存她的个人信息为",fileName
    #     f.write(content.encode('utf-8'))
    def saveImg(self, imageURL,fileName):
        imageURL1 = imageURL
        u = urllib2.urlopen(imageURL1)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        print u"保存图片为",fileName
        f.close()
    def mkdir(self,path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists=os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            print u"新建了名字叫做",path,u'的文件夹'
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print u"名为",path,'的文件夹已经创建成功'
            return False
    def savePageInfo(self,pageindex):
        contents = self.getContents(pageindex)
        foldname = "xuexi2"
        self.mkdir(foldname)
        for item in contents:
            detailURL = item[0]
            detailPage = self.getDetailPage(detailURL)
            # brief = self.getBrief(detailPage)
            images = self.getAllImg(detailPage)
            if images == None:
                continue

            # self.saveBrief(brief,item[2])
            # self.saveIcon(item[1],item[2])
            self.saveImgs(images, foldname, item[1])

    def savePagesInfo(self, start,end):
        for i in range(start,end+1):
            self.savePageInfo(i)
spider = Spider()
spider.savePagesInfo(1,12)
