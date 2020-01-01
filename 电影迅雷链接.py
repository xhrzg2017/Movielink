print('作者 电脑初哥')
import requests,re
import time
import os
path = '电影.txt'  # 文件路径
if os.path.exists(path):  # 如果文件存在
    # 删除文件，可使用以下两种方法。
    os.remove(path)
    #os.unlink(path)
    n = 0
    for i in range(1,168):
        try:
            url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_' + str(i)+'.html'
            html = requests.get(url)
            html.encoding = 'gb2312'
            ii = html.text
            jj = r'<a href="(.*?)" class="ulink">(.*?)</a>'
            num = re.findall(jj,ii)
            for url_get,name in num:
                print(name)
                a_url = 'http://www.dytt8.net/'+str(url_get)
                response_get = requests.get(a_url)
                response_get.encoding = 'gb2312'
                html_get = response_get.text
                order = '<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">(.*?).(.*?)</a></td>'
                ftp = re.findall(order,html_get)[-1][-1]
                with open(r'电影.txt', 'a', encoding='utf-8')as file:
                    file.write(name+'\n'+'f'+str(ftp)+'\n')
        except requests.exceptions.ConnectionError:
            print('unkown error')
            continue

else:
    n = 0
    for i in range(1,168):
        try:
            url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_' + str(i)+'.html'
            html = requests.get(url)
            html.encoding = 'gb2312'
            ii = html.text
            jj = r'<a href="(.*?)" class="ulink">(.*?)</a>'
            num = re.findall(jj,ii)
            for url_get,name in num:
                print(name)
                a_url = 'http://www.dytt8.net/'+str(url_get)
                response_get = requests.get(a_url)
                response_get.encoding = 'gb2312'
                html_get = response_get.text
                order = '<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">(.*?).(.*?)</a></td>'
                ftp = re.findall(order,html_get)[-1][-1]
                with open(r'电影.txt', 'a', encoding='utf-8')as file:
                    file.write(name+'\n'+'f'+str(ftp)+'\n')
        except requests.exceptions.ConnectionError:
            print('unkown error')
            continue
