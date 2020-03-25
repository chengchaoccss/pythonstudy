from selenium import webdriver
import time


class JdSpider(object):
    def __init__(self):
        self.i = 0
        self.url = 'https://www.jd.com/'
        self.browser = webdriver.Chrome()

    # 获取页面信息 - 到具体商品的页面
    def get_html(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书')  # 搜索框输入“爬虫书”
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()  # 点击搜索
        time.sleep(3)  # 给商品页面加载时间

    # 解析页面
    def parse_html(self):
        # 把下拉菜单拉到底部,执行JS脚本
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        # 提取所有商品节点对象列表 li列表
        li_list = self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            info_list = li.text.split('\n')
            if info_list[0].startswith('每满') or info_list[1].startswith('￥'):
                price = info_list[1]
                name = info_list[2]
                comment = info_list[3]
                shop = info_list[4]
            elif info_list[0].startswith('单件'):
                price = info_list[3]
                name = info_list[4]
                comment = info_list[5]
                shop = info_list[6]
            else:
                price = info_list[0]
                name = info_list[1]
                comment = info_list[2]
                shop = info_list[3]

            print(price, comment, shop, name)

    # 主函数
    def main(self):
        self.get_html()
        while True:
            self.parse_html()
            # 判断是否该点击下一页,没有找到说明不是最后一页
            if self.browser.page_source.find('pn-next disabled') == -1:
                self.browser.find_element_by_class_name('pn-next').click()
                time.sleep(2)
            else:
                break
        print(self.i)


if __name__ == '__main__':
    spider = JdSpider()
    spider.main()