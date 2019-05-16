import urllib, sys
import ssl
import base64
import re

def get(path):
    f=open(path,'rb') #二进制方式打开图文件
    ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
    print(str(ls_f))

    host = 'https://tysbgpu.market.alicloudapi.com'
    path = '/api/predict/ocr_general'
    method = 'POST'
    appcode = '37c6afe5b3cb440e970eca0bbb306884'
    querys = ''
    bodys = {}
    url = host + path

    bodys[''] = "{\"image\":\""+ls_f.decode("utf-8")+"\",\"configure\":\"{\\\"min_size\\\":2,\\\"output_prob\\\":false}\"}"
    print(bodys[''])
    post_data = bodys[''].encode("utf-8")
    request = urllib.request.Request(url, post_data)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = urllib.request.urlopen(request, context=ctx)
    content = response.read()
    if (content):
        str_content = content.decode("utf-8")
        print(str_content)

        str2 = re.search(r'"word":"*[^\d]*\d{12}"}', str_content, re.M | re.I)
        print(str2.group())
        result_1 = re.findall(r"\d+\.?\d*", str2.group())[0]
        print(result_1)

        str3 = re.search(r'"word":"*[^\d]*\d{8}"}', str_content, re.M | re.I)
        print(str3.group())
        result_2 = re.findall(r"\d+\.?\d*", str3.group())[0]
        print(result_2)
        return result_1,result_2


