# -*- coding: UTF-8 -*-
"""
本爬虫爬取后台需要使用的图片
"""
import time
from splinter import Browser
import traceback


class Crawler:
    def __init__(self):
        # 如果下载不成功则下一张，仍然不能获取浏览返回状态则忽略
        self.url="http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=%E7%BE%8E%E5%A5%B3&step_word=&hs=0&pn=0&spn=0&di=115841179330&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=1448969331%2C3840882916&os=3613101257%2C51753532&simid=0%2C0&adpicid=0&lpn=0&ln=3900&fr=&fmq=1491741852964_R&fm=detail&ic=0&s=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=girl&bdtype=11&oriquery=&objurl=http%3A%2F%2Fimg.popo.cn%2Fuploadfile%2F2017%2F0217%2F1487316191770266.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Br5r5_z%26e3BvgAzdH3Fkjw7pyAzdH3FgjofAzdH3F8l0_8c9b9n_8_z%26e3Bip4s&gsm=&rpstart=0&rpnum=0"
        # kernel function

    def launch(self):
        # launch driver
        browser = Browser('chrome')
        browser.driver.maximize_window()
        browser.visit(self.url)
        #browser.driver.implicitly_wait(5)
        #browser.driver.Manage().Timeouts().SetPageLoadTimeout(600);

        for i in range(500):
            try:
                browser.reload()
                browser.driver.set_page_load_timeout(10)
                browser.driver.set_script_timeout(15)
                if browser.is_element_present_by_text('下载'):
                    browser.find_by_text('下载').first.click()
                else:
                    browser.evaluate_script('$(".img-switch-btn").last().click()')
            except:
                # 如果下载不成功则下一张，仍然不能获取浏览返回状态则忽略
                try:
                    browser.evaluate_script('$(".img-switch-btn").last().click()')
                except:
                    traceback.print_exc()
                    pass
            time.sleep(1.5)
            if(len(browser.windows) > 1):
                browser.windows.current = browser.windows[0]
                browser.windows.current.close_others()
                #如果下载不成功则下一张，仍然不能获取浏览返回状态则忽略
                try:
                    browser.evaluate_script('$(".img-switch-btn").last().click()')
                except:
                    pass
            else:
                # 如果下载不成功则下一张，仍然不能获取浏览返回状态则忽略
                try:
                    browser.evaluate_script('$(".img-switch-btn").last().click()')
                except:
                    pass


if __name__ == '__main__':
    crawler = Crawler()
    crawler.launch()