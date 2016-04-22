# -*- coding:utf-8 -*-
import urllib2
import re
import os
import time
class Spider:
    def __init__(self):
         self.siteURL = 'http://bbs.hupu.com/bxj-'
         self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
         self.header = {'User-Agent':self.user_agent}
        # self.siteURL = 'http://www.2cto.com/meinv/gaoqing/list_5_'
    def getPage(self, pageIndex):
        url = self.siteURL + str(pageIndex)
        request = urllib2.Request(url, headers=self.header)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')
    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('</td><td id="" class="p_title"><div id(.*?)<td class="p_chkbox">',re.S)
        reitems = re.findall(pattern, page)
        contents = []
        pattern1 = re.compile('</div>\s*<a id="" href="(.*?)">(.*?)</a>\s*<span class="light.*?<a.*?title="(.*?)">.*?class="p_author".*?class="u".*?>(.*?)</a><br.*?>(.*?)</td>.*?class="p_re">(.*?)</td><.*?class="p_retime.*?<a.*?title.*?>(.*?)</a><br.*?>(.*?)</td>',re.S)
        for reitem in reitems:
            items = re.findall(pattern1, reitem)
            if len(items) != 0:
                item = items[0]
                voteNum = item[5].split('/')
                # print 'http://bbs.hupu.com'+item[0],item[1],item[2], item[3], item[4],voteNum[0],voteNum[1], item[6], item[7]
                contents.append(['http://bbs.hupu.com'+item[0],item[1],item[2], item[3], item[4],voteNum[0],voteNum[1], item[6], item[7]])

        return contents
    def saveContent(self, content):
        path = "HUPU"
        isExists = os.path.exists(path)
        ISOTIMEFORMAT='%Y-%m-%d'

        timeName = time.strftime(ISOTIMEFORMAT,time.localtime())
        if not isExists:
            os.makedirs(path)
        fileName = path + "/" + "hupu" + timeName +".txt"
        f = open(fileName, 'a+')
        for i in content:

            f.write(i[1].encode('utf-8'))
            f.write("("+i[0]+")"+"\t")
            f.write((i[5])+"\\")
            f.write((i[6])+"\t")
            f.write(i[2].encode('utf-8')+"\n")
            f.write(i[4].encode('utf-8')+"\t")
            f.write(i[3].encode('utf-8')+"\n")
            f.write(i[7].encode('utf-8')+"\t")
            f.write(i[8].encode('utf-8')+"\n")


    def test(self, start, end):
        ISOTIMEFORMAT='%Y-%m-%d'

        timeName = time.strftime(ISOTIMEFORMAT,time.localtime())
        fileName = "HUPU" + "/" + "hupu" + timeName +".txt"
        f = open(fileName, 'w+')
        f.close()
        contents = []
        for pageIndex in range(start, end + 1):
            contents.extend(self.getContents(pageIndex))
        contents.sort(cmp = lambda x, y: int(x[5])-int(y[5]) or int(x[6])-int(y[6]), reverse=True)
        self.saveContent(contents)




spider = Spider()
spider.test(1,5)