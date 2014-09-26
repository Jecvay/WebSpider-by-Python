from urllib.error import HTTPError, URLError
from html.parser import HTMLParser
import urllib.request
import urllib.parse
import urllib

_ljwLT = ''

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



def saveFile(data):
    save_path = 'D:\\temp.txt'
    f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()

# /////////////////////// main ////////////////////////




urla = 'http://cas.nwpu.edu.cn/cas/login?service=http%3A%2F%2Fportal.nwpu.edu.cn%2Fdcp%2Findex.jsp'

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')]
urlaopen = opener.open(urla)
dataa = urlaopen.read()

hparser = MyHTMLParser()
# print(dataa.decode())
hparser.feed(dataa.decode())

#############################
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
# print(postData)

full_url = urllib.request.Request(url, postData, header)

try:
    response = urllib.request.urlopen(full_url)
    data = response.read()
    saveFile(data)
#    print(data.decode())


except HTTPError as e:
    print('Error code: ', e.code)
except URLError as e:
    print('Reason: ', e.reason)
    the_page = response.read()
    print(the_page)