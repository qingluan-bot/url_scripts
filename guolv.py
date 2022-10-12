#/bin/bash

from encodings.utf_8 import decode
import statistics
import sys
from os import system
import re
from tokenize import Ignore
import urllib3
import requests
import os

#过滤类，覆盖写入
class guolv:
    


    #获取当前路径
    def get_path():
        path = os.getcwd()





    #过滤出主域的url
    def mainurl(urls_file):
        dir = os.getcwd()
        f = open("./main_urls.txt".format(dir), "w",encoding='utf-8',errors='ignore')
        with open(urls_file,'r',encoding='utf-8',errors='ignore') as d:
            url = []
            for i in d.readlines():
                i = i.strip('\n')
                try:
                    xieyi = i.split('/',3)[0]
                    domain = i.split('/',3)[2]
                except Exception:
                    i=i
                res = xieyi + r"//" + domain
                print(res)
                url.append(res)
                f.write(res + '\n')
        f.close()
        return url






        







    #过滤出域名
    def domain(urls_file):
        f =  open("./domains.txt", "w",encoding='utf-8',errors='ignore')
        with open(urls_file,'r',encoding='utf-8') as d:
            domain = []
            for i in d.readlines():
                i = i.strip('\n')
                if i.find('https://www.') == 0:
                    i=i.replace('https://www.','')
                elif i.find('https://') == 0:
                    i=i.replace('https://','')
                elif i.find('http://www.') == 0:
                    i=i.replace('http://www.','')
                elif i.find('http://') == 0:
                    i=i.replace('http://','')
                else:
                    i=i
                if i.find('/'):
                    i=i.split('/',1)[0]
                print(i)
                domain.append(i)
                f.write(i + '\n')
        f.close()
        return domain













    #请求响应200
    def get_code_status(urls_file):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
        }
        g =  open("./code_200.txt", "w",encoding='utf-8',errors='ignore')
        with open(urls_file, 'r', encoding='utf-8',errors='ignore') as f:
            code = []
            for url in f.readlines():
                url = url.strip('\n')
                #print(url)
                disable_warnings()
                try:
                    res = requests.get(
                        url, headers=header, verify=False, allow_redirects=False
                    )
                except Exception as error:
                    print(error)
                code = res.status_code
                if code == 200:
                    print('状态码 {}:{}'.format(code, url))
                    code.append(url)
                    g.write(url + '\n')
        g.close()
        return code
        







    #含有asp jsp jspx php 等的url

    def jiagou(urls_file):
        o =  open("./jiagou_urls.txt", "w",encoding='utf-8',errors='ignore')
        with open(urls_file,'r',encoding='utf-8',errors='ignore') as f:  #判断url是否有.php? .asp? .aspx? .jsp?
            jiagou = []
            for i in f.readlines():
                res = re.compile(r'\.php\?')
                datas = res.findall(i)
                if datas != []:
                    jiagou.append(res)
                    o.write(i)
                else:
                    res = re.compile(r'\.asp\?')
                    datas = res.findall(i)
                    if datas != []:
                        jiagou.append(res)
                        o.write(i)
                    else:
                        res = re.compile(r'\.aspx\?')
                        datas = res.findall(i)
                        if datas != []:
                            jiagou.append(res)
                            o.write(i)
                        else:
                            res = re.compile(r'\.jsp\?')
                            datas = res.findall(i)
                            if datas != []:
                                jiagou.append(res)
                                o.write(i)
        o.close()
        return jiagou







        #过滤gov
    def nogov(urls_file):
        dir = os.getcwd()
        f = open("{}/nogov_urls.txt".format(dir), "w",encoding='utf-8',errors='ignore')
        with open(urls_file,'r',encoding='utf-8',errors='ignore') as d:
            nogov = []
            for i in d.readlines():
                i = i.strip('\n')
                if i.find("gov")  != -1:
                    continue
                print(i)
                nogov.append(i)
                f.write(i + '\n')
        f.close()
        return nogov



    #域名转换为url
    def domain_to_url(urls_file):
        f = open("./domain_to_url.txt", "w",encoding='utf-8',errors='ignore')
        with open(urls_file,'r',encoding='utf-8',errors='ignore') as d:
            domain_to_url = []
            for i in d.readlines():
                i = i.strip('\n')
                if i.find('http') == -1:
                    i = 'http://' + i + '/'            
                else:
                    i = i
                domain_to_url.append(1)
                f.write(i + '\n')
        f.close()
        return domain_to_url










    #只是去掉www.
    def nowww(urls_file):
        f = open("./nowwww.txt", "w",encoding='utf-8',errors='ignore')
        with open(urls_file,'r',encoding='utf-8',errors='ignore') as d:
            nowww = []
            for g in d.readlines():
                g = g.strip('\n')
                g = g.replace('www.','')
                nowww.append(g)
                f.write(g + '\n')
        f.close()
        return nowww







    

def disable_warnings():
    """
    解除去掉证书后总是抛出异常告警
    """
    urllib3.disable_warnings()






if __name__ == '__main__':
    urls_file = sys.argv[1]
    #guolv.get_code_status(urls_file)
    #guolv.mainurl(urls_file)
    #guolv.domain(urls_file)
    #guolv.jiagou(urls_file)
    #guolv.get_path()
    #guolv.nogov(urls_file)
    #guolv.domain_to_url(urls_file)
    #guolv.nowww(urls_file)