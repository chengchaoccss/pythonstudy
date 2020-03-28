# import requests
# import re
# from lxml import etree
#
# def gethtml(url):
#     try:
#         kv = {
#             "cookie": '__mta=256735540.1585380208103.1585380900703.1585380904829.6; uuid_n_v=v1; uuid=02D0385070C511EA88BB43CCA600DB6602C3CC9165164BED8D9B4195D2280C36; _csrf=603f65cca50c35269c42bd02a585d39d57101e278503aa82fd6582b9d98147ba; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1585380206; _lxsdk_cuid=17120062789c8-09b2dd8ef9bcab-f313f6d-190140-1712006278ac8; _lxsdk=02D0385070C511EA88BB43CCA600DB6602C3CC9165164BED8D9B4195D2280C36; mojo-uuid=5a3bb5bae9593282054922ffe1eab504; mojo-session-id={"id":"048ee3e95fb71c50af90cf0380b6d71c","time":1585380208044}; mojo-trace-id=8; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1585380904; _lxsdk_s=1712006278b-fd-b2-979%7C%7C12',
#             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
#         res = requests.get(url,headers = kv,timeout =30)
#         res.raise_for_status()
#     except:
#         print("访问出错!")
#     else:
#         res.encoding=res.apparent_encoding
#         return res.text
#
# def parsehtml(html,list,starlist):
#     reg = etree.HTML(html)
#     name =reg.xpath('//p[@class="name"]/a/text()')
#     star = reg.xpath("//p[@class ='star']/text()")
#     list += name
#     for i in star:
#         starlist.append(i)
#     return None
#
# def main():
#     namelist = []
#     starlist=[]
#     result = []
#     for i in range(0,100,10):
#         url = "https://maoyan.com/board/4?offset="+str(i)
#         html = gethtml(url)
#         parsehtml(html,namelist,starlist)
#     for i in range(len(namelist)):
#         print(f'{i}{namelist[i]}  {starlist[i].strip()}')
#
# if __name__=="__main__":
#     list = []
#     main()

#### 音乐爬虫 ####
`
import requests
from lxml import etree

def gethtml(url):
    try:
        kw = {
            'cookies':'UM_distinctid=17121941056289-00038658d91354-f313f6d-190140-17121941057216; CNZZDATA1260502790=625044373-1585405157-https%253A%252F%252Fblog.csdn.net%252F%7C1585405157',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
        res = requests.get(url,headers=kw,timeout=30)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
    except:
        print("访问出错!")
    else:
        return res.text

def parsehtml(html):
    response = etree.HTML(html)
    name = response.xpath('//tr/td[@class="song-name"]/text()')
    link = response.xpath('//tr/td[@class = "song-bitrate"]/a[last()]/@href')
    name = name[1::]
    for i in range(len(name)):
        print(f'{i+1}:{name[i]}')

    if len(name)==0:
        print('该平台没有相关歌曲,可以换一个平台!')
    else:
        ind = int(input("请输入需要下载的序号:"))
        print(f'{name[ind-1]}下载中......')
        downloadmp3(link[ind-1],name[ind-1])
    # print(link[ind-1])

def downloadmp3(link,name):
    with open(f'D:/mp3/{name}.mp3','wb') as f:
        data = requests.get(link)
        # print(f'{name}下载中......')
        f.write(data.content)
        print(f'{name}-下载完成!')
        f.close()

def main():
    while True:
        sname = input('请输入歌曲名称:')
        station=''
        plat = input('请输入音乐平台:1)qq 2)网易 3)酷我 4)酷狗 5)咪咕:')
        if plat == '1':
            station = 'qq'
        elif plat =='2':
            station = 'wy'
        elif plat =='3':
            station = 'kuwo'
        elif plat =='4':
            station = 'kg'
        elif plat=='5':
            station = 'migu'
        else:
            print('输入错误!')

        url = f'https://music.hwkxk.cn/?kw={sname}&lx={station}'
        # print(url)
        html = gethtml(url)
        parsehtml(html)
        code = input('继续下载?y/n:')
        if code == 'y':
            pass
        else:
            break

if __name__ == '__main__':
    main()