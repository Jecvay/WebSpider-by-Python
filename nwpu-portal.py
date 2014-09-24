from urllib.error import HTTPError, URLError
import urllib.request
import urllib.parse
import urllib

url = 'http://cas.nwpu.edu.cn/cas/login'

header = {
    'Referer': 'http://cas.nwpu.edu.cn/cas/login?service=http%3A%2F%2Fportal.nwpu.edu.cn%2Fdcp%2Findex.jsp',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729)'
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

postData = urllib.parse.urlencode(postDict)
postData = postData.encode('utf-8')
# print(postData)
full_url = urllib.request.Request(url, postData, header)
print(full_url)
try:
    response = urllib.request.urlopen(full_url)
    data = response.read()
    print(data)
    save_path = 'D:\\temp.txt'
    f_obj = open(save_path, 'wb')
    f_obj.write(data)

except HTTPError as e:
    print('Error code: ', e.code)
except URLError as e:
    print('Reason: ', e.reason)
    the_page = response.read()
    print(the_page)