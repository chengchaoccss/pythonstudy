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



import requests
from lxml import etree


def gethtml(url):
    try:
        kw ={"cookie":'PHPSESSID=acv8qokcug9ool4kv6ciiju5t1; Hm_lvt_7b4781cf7490e2d992d9731db206ded1=1585384727; __gads=ID=64d28d4d2c450402:T=1585384740:S=ALNI_Ma1YuE-EBecg8Kk7dPrsLEnK9-maA; Hm_lpvt_7b4781cf7490e2d992d9731db206ded1=1585385455',
             "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
        res = requests.get(url,headers=kw,timeout=30)
        res.raise_for_status()
    except:
        print("有问题!")
    else:
        return res.text


def parsehtml(html):
    resp = etree.HTML(html)
    newurl = resp.xpath('//div[@class="list_info"]/h2/a/@href')
    for i in newurl:
        aurl ="https://www.aixdzs.com"+i
        newhtml = gethtml(aurl)
        lastwork = parsenewhtml(newhtml)
        # print(lastwork)
        dataserve(lastwork)


def dataserve(lastwork):
    for i in lastwork:
        # with open('./books/'+i[0]+'.zip','wb') as f:
        #     data= requests.get(i[1])
            # f.write(data.content)
            # f.close()
            # print(f'<<{i[0]}>>下载完成!')
        print(f'<<{i[0]}>>下载完成!')


def parsenewhtml(newhtml):
    newres =etree.HTML(newhtml)
    name = newres.xpath('//div[@class="d_info"]/h1/text()')
    txt_link = newres.xpath('//div[@id="txt_down"]/a[@title="TXT全集更多下载"]/@href')
    epub_link = newres.xpath('//div[@id="epub_down"]/a[last()]/@href')
    lastname = name[0].split("t")[0]
    last_txtlink = "https://www.aixdzs.com" + txt_link[0]
    last_epublink = "https://www.aixdzs.com" + epub_link[0]
    yield [lastname,last_txtlink,last_epublink]


def main():
    for i in range(1,230):
        url = f"https://www.aixdzs.com/sort/3/index_4_2_0_{i}.html"
        html = gethtml(url)
        parsehtml(html)


if __name__ == '__main__':
    main()