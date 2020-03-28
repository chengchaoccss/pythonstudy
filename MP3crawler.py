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