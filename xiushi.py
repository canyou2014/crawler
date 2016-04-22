# -*- coding:utf-8 -*-
import urllib2
import urllib
import re

class xiushi:
    def __init__(self):
        self.page = 1
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
        self.headers = {'User-Agent' : self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self, page):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(page)
            request = urllib2.Request(url, headers = self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"connect error", e.reason
                return None
    def getPageItems(self, page):
        pageCode = self.getPage(page)
        if not pageCode:
            print "loading error"
        pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?title="(.*?)">.*?</a>.*?<div.*?class'+
                     '="content".*?>(.*?)<!--.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
        items = re.findall(pattern,pageCode)
        pagesStories = []
        for item in items:
            haveimg = re.search("img", item[2])
            if not haveimg:
                pagesStories.append([item[0].strip(), item[1].strip(),item[3].strip()])
        return pagesStories
    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.page)
                if pageStories:
                    self.stories.append(pageStories)
                    self.page += 1
    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "Q":
                self.enable = False
                return
            print u"第%d页\n发布人:%s\n%s\n赞:%s\n" %(page,story[0],story[1],story[2])

    def start(self):
        print u"reading, Enter"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStrories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStrories, nowPage)

spider = xiushi()
spider.start()







# page = 2
# url = 'http://www.qiushibaike.com/hot/page/' + str(page)
# user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
# headers = {'User-Agent' : user_agent}
# try:
#     request = urllib2.Request(url, headers=headers)
#     response = urllib2.urlopen(request)
#
#     content = response.read().decode('utf-8')
#     pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?title="(.*?)">.*?</a>.*?<div.*?class'+
#                      '="content".*?>(.*?)<!--.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
#     items = re.findall(pattern,content)
#
#     for item in items:
#         haveimg = re.search("img", item[2])
#         if not haveimg:
#             print item[0], item[1], item[2], item[3]
#     # print response.read()
# except urllib2.URLError, e:
#     if hasattr(e, "code"):
#         print e.code
#     if hasattr(e, "reason"):
#         print e.reason
