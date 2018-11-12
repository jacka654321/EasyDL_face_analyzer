#!/usr/bin/python  
# -*- coding:utf-8 -*-  
import http.client   
import urllib  
import json  
import urllib3  
import re  
import os  
  
class BaiduImage(object):  
    def __init__(self):  
        super(BaiduImage,self).__init__()  
        print(u'图片获取中,CTRL+C 退出程序...') 
        self.page = 60                    #当前页数  
        if not os.path.exists(r'./image'):  
            os.mkdir(r'./image')                      
      
      
    def request(self):  
        try:  
            while 1:  
                conn=http.client.HTTPSConnection('image.baidu.com')  
                request_url ='/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=%E7%BE%8E%E5%A5%B3&cg=girl&rn=60&pn='+str(self.page)  
                headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0','Content-type': 'sinanews/html'}  
                #body = urllib.urlencode({'tn':'resultjsonavatarnew','ie':'utf-8','word':'%E7%BE%8E%E5%A5%B3','cg':'girl','pn':self.page,'rn':'60'})  
                conn.request('GET',request_url,headers = headers)  
                r= conn.getresponse()  
                #print r.status  
                if r.status == 200:  
                    data = r.read()  
                      
                    data = unicode(data, errors='ignore')  
                    decode = json.loads(data)  
                    self.download(decode['imgs'])  
              
                self.page += 60  
        except Exception as e:  
            print(e)
            
        finally:  
            conn.close()  
              
    def download(self,data):  
      
        for d in data:    
            #url = d['thumbURL']   缩略图  尺寸200  
            #url = d['hoverURL']           尺寸360  
            url =d['objURL']  
            data =urllib3.urlopen(url).read()  
              
            pattern = re.compile(r'.*/(.*?)\.jpg',re.S)  
            item = re.findall(pattern,url)  
            FileName = str('image/')+item[0]+str('.jpg')  
              
            with open(FileName,'wb') as f:  
                f.write(data)  
      
if  __name__ == '__main__':  
    bi = BaiduImage()  
    bi.request()  