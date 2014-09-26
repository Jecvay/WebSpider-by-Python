from urllib.error import HTTPError, URLError
from html.parser import HTMLParser
import urllib.request
import urllib.parse
import urllib
import http.cookiejar

_ljwLT = ''
_ljwURL = ''

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global _ljwLT
        find = False
        if tag == 'input':
            for name, value in attrs:
                if find == True:
                    print(value)
                    _ljwLT = value
                if value == 'lt':
                    print('name=', name, '  value=', value)
                    find = True

class GetHref(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global _ljwURL
        find = False
        for name, value in attrs:
            if name == 'href':
                print('name=', name, '  value=', value)
                _ljwURL = value


def saveFile(data):
    save_path = 'D:\\temp.txt'
    f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()


# /////////////////////// main ////////////////////////


######################## GET

urla = 'http://cas.nwpu.edu.cn/cas/login?service=http%3A%2F%2Fportal.nwpu.edu.cn%2Fdcp%2Findex.jsp'

urlarequest = urllib.request.Request(urla, headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
})
urlaopen = urllib.request.urlopen(urlarequest)
dataa = urlaopen.read()
hparser = MyHTMLParser()
hparser.feed(dataa.decode())

######################## POST
url = 'http://cas.nwpu.edu.cn/cas/login'

header = {
    'Connection': 'Keep-Alive',
  #  'Content-Length' : '245',
    'Host' : 'cas.nwpu.edu.cn',
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Referer': 'http://cas.nwpu.edu.cn/cas/login?service=http://portal.nwpu.edu.cn/dcp/index.jsp',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729)'
  #  'Cookie' : 'neusoftnwpudcp=R4QyJjSBpwny8lZQPQzYT3yJpxLyG1T9QQJV0Ly6Wr2fDT9gNCNY!2005067793; neusoftnwpudcp_NS_Sig=oenCV62a-zpBuly5'
}

postDict = {
    'encodedService': 'http%3a%2f%2fportal.nwpu.edu.cn%2fdcp%2findex.jsp',
    'service'	:'http://portal.nwpu.edu.cn/dcp/index.jsp',
    'serviceName':	'null',
    'loginErrCnt'	:'0',
    'username'	:'2012303505',
    'password'	:'bcdljw38',
    'lt'	:'LT_nwpuapp1_-576204-cpccvEbkegnqKOrJ8j9t'
}

print(_ljwLT)
postDict['lt'] = _ljwLT


postData = urllib.parse.urlencode(postDict)
postData = postData.encode('utf-8')


cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
head = []
for key, value in header.items():
    tmp = (key, value)
    head.append(tmp)
print(head)
opener.addheaders = head
response = opener.open(url, postData)
data = response.read()

######################## JUMP
hparser = GetHref(convert_charrefs=True)
hparser.feed(data.decode('gb2312'))
print(_ljwURL)
urla = _ljwURL
urlarequest = urllib.request.Request(urla, headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
})
urlaopen = urllib.request.urlopen(urlarequest)
dataa = urlaopen.read()
print(dataa.decode())


####################### 此处需要Cookies
urla = 'http://portal.nwpu.edu.cn/dcp/forward.action?path=/portal/portal&p=wkHomePage'

urlaopen = opener.open(urla)
dataa = urlaopen.read()
print(dataa.decode('gb2312'))
hparser.feed(dataa.decode('gb2312'))
print(_ljwURL)

urla = _ljwURL
urlaopen = opener.open(urla)
dataa = urlaopen.read()
print(dataa.decode())
saveFile(dataa)


urla = 'http://cas.nwpu.edu.cn/cas/login?service=http%3A%2F%2F222.24.192.69%2FmhLogin.jsp'
urlaopen = opener.open(urla)
dataa = urlaopen.read()
print(dataa.decode('gb2312'))
hparser.feed(dataa.decode('gb2312'))
print(_ljwURL)

urla = _ljwURL
urlaopen = opener.open(urla)
dataa = urlaopen.read()
print(dataa.decode('gb2312'))


urla = 'http://222.24.192.69/gradeLnAllAction.do?type=ln&oper=fainfo&fajhh=4308'
urlaopen = opener.open(urla)
dataa = urlaopen.read()
print(dataa.decode('gb2312'))
saveFile(dataa)