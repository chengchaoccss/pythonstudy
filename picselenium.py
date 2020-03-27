from selenium import webdriver
from lxml import etree
from urllib import request
import time

class Baidu_pic(object):
    def __init__(self,kw):
        self.kw = kw
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result" \
                   "&fr=&sf=1&fmq=1585138027868_R&pv=&ic=0&nc=1&z=0&hd=0&latest=0&copyright=0&se=1&showtab=0&fb=0" \
                   "&width=&height=&face=0&istype=2&ie=utf-8&sid=&word="+self.kw
        self.driver.get(self.url)
        self.ele = self.driver.find_element_by_xpath("//div[@class='imgbox'][1]/a")
        self.newurl=self.ele.get_attribute('href')
        self.name = 1

    def run(self):
        self.driver.get(self.newurl)
        while True:
            try:
                source = self.driver.page_source
                html = etree.HTML(source)
                pic_url = html.xpath("//img[@class='currentImg']")
                for res in pic_url:
                    pic = res.get("src")
                    request.urlretrieve(pic, "baidupic/"+str(self.name)+".jpg")
                    print("下载完成{}张".format(self.name))
                    self.name += 1
                    self.driver.find_element_by_xpath("//span[@class='img-next']").click()
                    time.sleep(2)
                if self.name == 50:
                    break
            except:
                continue


if __name__ == '__main__':
    kw = input("请输入图片名称:")
    baidu = Baidu_pic(kw)
    baidu.run()
