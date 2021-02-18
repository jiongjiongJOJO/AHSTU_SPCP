import requests
import random
import os
import demjson
import time

userid = os.getenv("USERID")
password = os.getenv("PASSWORD")
data_yiqing = os.getenv("DATA")
send_key = os.getenv("SEND")

time_temper = 3

selectChar = ["2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "m", "n",
              "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "J",
              "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
codeInput = ''
for i in range(4):
    codeInput += selectChar[random.randint(0, 54)]
# 登录
headers = {'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1',
           'Origin': 'http://xgb.ahstu.edu.cn', 'Content-Type': 'application/x-www-form-urlencoded',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Referer': 'http://xgb.ahstu.edu.cn/SPCP/Web/',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
data = {'StuLoginMode': '1', 'txtUid': userid, 'txtPwd': password, 'codeInput': codeInput}
response = requests.post('http://xgb.ahstu.edu.cn/SPCP/Web/', headers=headers, data=data, verify=False,
                         allow_redirects=False)
cookies = {}
cookies['CenterSoftWeb'] = response.headers['Set-Cookie'][
                           response.headers['Set-Cookie'].find('=') + 1:response.headers['Set-Cookie'].find(';')]

# 体温填报
def Temper(time):
    if (time == 0):
        date = ['0', '0']
    elif (time == 1):
        date = ['4', '1']
    else:
        date = ['8', '2']
    # 随机体温
    Temper = random.randint(0, 9)
    headers = {'Connection': 'keep-alive', 'Cache-Control': 'max-age=0','Accept-Encoding':'gzip, deflate',
               'Upgrade-Insecure-Requests': '1', 'Origin': 'http://xgb.ahstu.edu.cn',
               'Content-Type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Referer': 'http://xgb.ahstu.edu.cn/SPCP/Web/Temperature/StuTemperatureInfo',
               'Accept-Language': 'zh-CN,zh;q=0.9'}
    data = {'TimeNowHour': date[0], 'TimeNowMinute': date[1], 'Temper1': '36', 'Temper2': Temper}
    response = requests.post('http://xgb.ahstu.edu.cn/SPCP/Web/Temperature/StuTemperatureInfo', headers=headers,
                             cookies=cookies, data=data)
    # 输出结果
    if ('填报成功！' in response.text):
        print('体温填报-填报成功！')
    else:
        print('第'+str(time+1)+'次体温填报失败')
        url_server = 'https://sctapi.ftqq.com/'+send_key+'.send?title=体温填报第 ' + str(
            time + 1) + ' 次失败&desp=' + response.text
        requests.get(url_server)

# 疫情填报
def yiqing():
    headers = {'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1',
               'Origin': 'http://xgb.ahstu.edu.cn', 'Content-Type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Referer': 'http://xgb.ahstu.edu.cn/SPCP/Web/Report/Index', 'Accept-Language': 'zh-CN,zh;q=0.9', }

    data = demjson.decode(data_yiqing)
    response = requests.post('http://xgb.ahstu.edu.cn/SPCP/Web/Report/Index', headers=headers, cookies=cookies,
                             data=data)
    if ('提交成功！' in response.text):
        print('疫情填报-提交成功！')
    else:
        print('疫情填报失败')
        url_server = 'https://sctapi.ftqq.com/'+send_key+'.send?title=疫情填报失败&desp=' + response.text
        requests.get(url_server)



for i in range(time_temper):
    Temper(i)
    time.sleep(2)
yiqing()
