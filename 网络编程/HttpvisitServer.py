# 2018年8月14日 14:36:18
# 作为客户端与HTTP服务交互
# 通过HTTP协议访问多种服务，如下载数据或者与基于REST的API进行交互
# 对于简单的事情，使用urllib.request模块就够了，比如发送一个简单的HTTP GET请求到远程的服务上
'''
from urllib import request,parse

# base URL being accessed
url = 'http://httpbin.org/get'

# Dictionary of query parameters(if any)
parms={
    'name1':'value1',
    'name2':'value2'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Make a POST request and read the response
u=request.urlopen(url+'?'+querystring)
resp=u.read()
'''
# 如果需要使用POST方法在请求主体中发送查询参数，可以将参数编码后作为可选参数提供给urlopen()函数
'''
from urllib import request,parse

url='http://httpbin.org/post'

parms={
    'name1'='value1',
    'name2'='value2'
}
querystring=parse.urlencode(parms)

u=request.urlopen(url,querystring.encode('ascii'))
resp=u.read()
'''
# 如果需要在发出的请求中提供一些自定义的HTTP头，例如修改user-agent字段，可以创建一个包含字段值的字典，并创建一个request实例然后将其传给urlopen().
'''
from urllib import request,parse

headers = {
    'User-agent':'none/ofyourbusiness',
    'Spam':'Eggs'
}

req = request.Request(url,querysting.encode('ascii'),headers=headers)
u = request.urlopen(req)
resp = u.read()
'''
# 如果需要交互的服务比上面的例子都要复杂，也许应该去看看 requests 库（https://pypi.python.org/pypi/requests）。
# 