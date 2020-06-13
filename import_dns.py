# coding:utf-8
import requests
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

domain=('crjy.cpou.cn','ycdz.cpou.cn','yzdz.cpou.cn','gzfy.cpou.cn','pmrs.cpou.cn','plrs.cpou.cn','pftp.cpou.cn','media.cpou.cn','lesson.cpou.cn','apptest.cpou.cn','mtest.cpou.cn','ntm.cpou.cn','zxks.cpde.cn','gwzgtest.cpou.cn','yczb.cpde.cn','yczb.cpou.cn','rtx.cpde.cn','media.cpde.cn','lesson.cpde.cn','ycdz.cpoc.cn','yzdz.cpoc.cn','pmrs.cpoc.cn','plrs.cpoc.cn','pftp.cpoc.cn','media.cpoc.cn','lesson.cpoc.cn','apptest.cpoc.cn','mtest.cpoc.cn','ntm.cpoc.cn','gwzgtest.cpoc.cn','yczb.cpoc.cn','rtx.cpoc.cn','zw.cptc.cn','cgk.cptc.cn','dept.cptc.cn','jgdm.cptc.cn','huodong.cpde.cn','gzfyv2.cpde.cn','baoxian.cpde.cn','yzxtcx.cn','ciems.cn','cipsbc.cn','cicnpl.cn','zybx.cpde.cn','zjds.cpoc.cn','up.cpde.cn','hbexam.cpoc.cn')
ip=('10.10.20.117','10.10.20.117','10.10.20.117','10.10.20.118','10.10.30.133','10.10.30.135','10.10.30.173','10.10.20.69','10.10.20.69','10.10.20.81','10.10.20.83','10.10.7.163','10.10.15.5','10.10.16.205','10.10.80.51','10.10.80.51','10.10.16.133','10.10.20.69','10.10.20.69','10.10.20.117','10.10.20.117','10.10.30.133','10.10.30.135','10.10.30.173','10.10.20.69','10.10.20.69','10.10.20.81','10.10.20.83','10.10.7.163','10.10.16.205','10.10.80.51','10.10.16.133','10.10.7.222','10.10.15.221','10.10.15.1','10.10.116.205','10.10.20.85','10.10.20.85','10.10.20.85','10.10.15.222','10.10.15.222','10.10.15.222','10.10.15.222','10.10.20.85','10.10.20.118','10.10.20.81','10.10.3.14')
x=0
def add_dns(domain,ip):
    url = "https://10.254.254.254/api/ad/v2/lc/dns-intranet-record/a?x_id=3e128282-a956-11ea-a395-000bab93beb9"
    headers = {
            'Host': '10.254.254.254',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'X-Requested-With':'XMLHttpRequest',
            'Content-Length': '118',
            'Origin': 'https://10.254.254.254',
            'Connection': 'keep-alive',
            'Referer': 'https://10.254.254.254/index?x_id=3e128282-a956-11ea-a395-000bab93beb9',
            'Cookie': 'language=zh_CN; UEDC_LOGIN_POLICY_VALUE=checked; session_id_443=3e1284d0-a956-11ea-a395-000bab93beb9',
            }
    payload = {
           'name':domain,
           'description':'',
           'state':'ENABLE',
           'type':'A',
           'a_records':[{'address':ip,'ttl':60}],
    }
    r = requests.post(url, json=payload, headers=headers,verify=False)
    print (r.json())
    print('写入成功')


while x<60:
    print(domain[x],ip[x])
    add_dns(domain[x],ip[x])
    x=x+1
    time.sleep(0.5)

