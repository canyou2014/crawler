import urllib2
import urllib
####################################
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http":'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)
#####################################
values = {"username":"599091274@qq.com","password":"wuyulunbi"}
user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
headers = {'User-Agent' : user_agent}
data = urllib.urlencode(values)
url = "http://passport.hupu.com/login"
timeout = 10
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request,timeout)

print response.read()
