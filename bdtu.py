#encoding:utf-8
import urllib  
import time  
from selenium import webdriver  
  
class Crawler:  
  
    def __init__(self):  
        self.url = 'http://image.baidu.com/i?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%89%8B%E6%9C%BA&oq=shouji&rsp=1' # url to crawl  
        self.img_xpath = '//ul/li/div/a/img' # xpath of img element  
        self.download_xpath = '//ul/li/div/div/span/a[@class="downloadicon"]' # xpath of download link element  
        self.img_url_dic = {}  
  
    # kernel function  
    def launch(self):  
        # launch driver  
        driver = webdriver.Firefox()  
        driver.maximize_window()  
        driver.get(self.url)  
  
        img_xpath = self.img_xpath  
        download_xpath = self.download_xpath  
        img_url_dic = self.img_url_dic  
          
        # 模拟滚动窗口以浏览下载更多图片    
        pos = 0     
        for i in range(10):    
            pos += i*500 # 每次下滚500    
            js = "document.documentElement.scrollTop=%d" % pos    
            driver.execute_script(js)  
            # get image desc and download  
            for img_element, link_element in zip(driver.find_elements_by_xpath(img_xpath), driver.find_elements_by_xpath(download_xpath)):  
                img_desc = img_element.get_attribute('data-desc') # description of image  
                img_desc = self.filter_filename_str(img_desc)  
                  
                img_url = link_element.get_attribute('href') # url of source image  
                if img_url != None and not img_url_dic.has_key(img_url):    
                    img_url_dic[img_url] = ''   
                    ext = img_url.split('.')[-1]  
                    filename = img_desc + '.' + ext  
                    print(img_desc, img_url)  
                    urllib.request.urlretrieve(img_url, 'd:\\%s' % filename)  
                    time.sleep(1)  
        driver.close()  
  
    # filter invalid characters in filename  
    def filter_filename_str(self, s):  
        invalid_set = ('\\','/',':','*','?','"','<','>','|',' ')  
        for i in invalid_set:  
            s = s.replace(i, '_')  
        return s      
  
if __name__ == '__main__':  
    crawler = Crawler()  
    crawler.launch()  