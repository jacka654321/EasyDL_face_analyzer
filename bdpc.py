#encoding:utf-8
import os
import  re
import requests
import threading
import time
import datetime
#得到路径，建立小图片文件夹，图片默认下载其中
currentpath=os.getcwd()
if not os.path.exists(currentpath+os.sep+'小图片'):
    os.mkdir(currentpath+os.sep+'小图片')

print(time.time())
print(datetime.datetime.now().strftime('%Y-%m-%d,%H:%M:%S'))

cookies={'winWH':'%5E6_1275x531','BDIMGISLOGIN':'0','BDqhfp':'%E6%9A%97%E7%96%AE%26%260-10-1undefined%26%260%26%261','BAIDUID':'E7D429DD089C9D9728EBBD80181B2F44','FG':'1','BIDUPSID':'E7D429DD089C9D9728EBBD80181B2F44','PSTM':'1503747134','BDUSS':'0dtUmhiYTBPbEdKQ2NWT3o3S1o1VktIOTh-SldxVmZFNVVzWE1-b1VWODZBc2xaSVFBQUFBJCQAAAAAAAAAAAEAAADFKL8MSmFja0E2NTQzMjEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADp1oVk6daFZa','MCITY':'-257%3A','BDSFRCVID':'ToLsJeC62xnhUyjZzTSQJI9az25yvSRTH6aVoXb2sZg7XXgXrVnfEG0PqU8g0KubJ6-jogKK3gOTH4jP','H_BDCLCKID_SF':'tR-tVC0-tCL3fP36q4co-4FjbqOH54cXHDOH0KvL3lQ5OR5Jj65h-PIL0h5z-fDt-gQAVCoVWprBSRTh3MA--t4JLP-H0xraKKjhVRny-bQTsq0x0bQWe-bQypoa2b-tQDOMahkb5h7xOKbF05CaD5v0jaLHt6nE2I5b3RA8KJjEe-Kk-PnVeIuALqbZKxJCKRcW3hkKafFajPQkyxuByU4syP4jKMRnWnciKfn4an6GOIbg0fjO3xIdDbL824TGWHIO0KJcb66JSP3NhPJvyT8sXnO7tjQTfJuJoIIyJItBbP365ITbbtFDhUKX5-RLf2vfLPOF5l8-h45hhx-50lIhKN3WBfF8KGuHofjnK4oxOKQpyJrWy-C-0UOu053eB6AOQqON3KJmqfK9bT3v5tDULJQh2-biWb7M2MbdJncmbCDRe5LaD6JM-Uvy-40XKD600PK8Kb7Vbn3KDbbkbfJBDRCJKhbDKHQEWlr-WqIBHf_4jfvBX-C7yajKLtKOQT5KQ-3sBRDKORjhQb3pQT8rKtFOK5Oib4jgoDnIab3vOIOTXpO1j-IreGKjtjLetR4HVbcaaJToq6rY5RrJ-J08qxbXqh3yBT7Z0l8Kttn_jM5wMl603htuy4u85RIHJ65qbMomWIQHSR7y-655W4bWWb7MXnjpaDc4KKJx-xKWeIJo5t5kjCuqhUJiB5JMBan7_ncxfJOKHICCD58KjM5','BDRCVFR[feWj1Vr5u3D]':'I67x6TjHwwYf0','BDRCVFR[dG2JNJb_ajR]':'mk3SLVN4HKm','BDRCVFR[-pGxjrCMryR]':'mk3SLVN4HKm','firstShowTip':'1','tip_show_limit':'1','shituhistory':'%7B%220%22%3A%22https%3A%2F%2Ftimgsa.baidu.com%2Ftimg%3Fimage%26quality%3D80%26size%3Db9999_10000%26sec%3D1507290686003%26di%3Dc863876f2e924f47cd98ea57c09ac0a5%26imgtype%3D0%26src%3Dhttp%3A%2F%2Fa.hiphotos.baidu.com%2Fzhidao%2Fpic%2Fitem%2Fd058ccbf6c81800aa9e8443eb23533fa828b47f5.jpg%22%7D','sttbHint':'sttbHintShow','Hm_lvt_9a586c8b1ad06e7e39bc0e9338305573':'1507280641','Hm_lpvt_9a586c8b1ad06e7e39bc0e9338305573':'1507280641','uploadTime':'0','userFrom':'null','PSINO':'6','pgv_pvi':'1894510592','pgv_si':'s7478237184','BDORZ':'B490B5EBF6F3CD402E515D22BCDA1598','indexPageSugList':'%5B%22%E6%9A%97%E7%96%AE%22%2C%22%E8%89%B2%E6%96%91%E5%92%8C%E9%9B%80%E6%96%91%E7%9A%84%E5%8C%BA%E5%88%AB%E5%9B%BE%E7%89%87%22%2C%22%E8%89%B2%E6%96%91%22%5D','cleanHistoryStatus':'0'}#用自己的cookies，别拿我的干坏事

headers={'Host':'image.baidu.com',#封装头部，否则有些图片下载不下来
'Referer':'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E6%9A%97%E7%96%AE',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
print(datetime.datetime.now().strftime('%Y-%m-%d,%H:%M:%S'))
#得到页面上图片的url与相关搜索的url
def search(searchurl):
    response = requests.get(searchurl,cookies=cookies,headers=headers)
    text=response.text
    s = re.findall(r'thumbURL":"([a-zA-z]+://[\w\.%=/\d,&]*)', text)#所有图片的url
    m = re.findall(r'search/index.(\S*)"', text)#当前页面指向其他页面的url
    return s,m

#根据传入的url与jpg名字下载图片
def download_pic(url,name):
    path=os.getcwd()+os.sep+'小图片'
    data=requests.get(url,cookies=cookies,headers=headers).content
    with open(path+os.sep+name,'wb') as f:
        f.write(data)
    print('图片下载完成：%s' % name)
    print(datetime.datetime.now().strftime('%Y-%m-%d,%H:%M:%S'))   


gimagelist=[]#图片的url
queue=[]#相关搜索的url
queue.append('tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E7%BE%8E%E5%A5%B3')#默认搜索关键词美女，你也可以换成其他的关键词url的index?后面的部分
gCondition=threading.Condition()#线程相关
visited=set()#用来存放已经搜过的页面的url
class Producer(threading.Thread):
    def run(self):
        print('%s started' % threading.current_thread())
        global gimagelist
        global gCondition
        global queue
        for j in range(3):#我默认循环一次，你也可以改很多
            a=queue.pop(0)#从队列中取出一个关键词url尾部
            searchurl='http://image.baidu.com/search/index?'+a#封装成url
            if searchurl not in visited:#如果没有访问过
                imgs,otherurl=search(searchurl)

                gCondition.acquire()#上锁
                for i in imgs:
                    gimagelist.append(i)#添加图片url
                gCondition.notify_all()#唤醒所有等待的消费者
                gCondition.release()#释放锁
                visited.add(searchurl)#标记为已访问过
                queue.extend(otherurl)#将相关搜索的url放入



class Consumer(threading.Thread):
    def run(self):
        print('%s started' % threading.current_thread())
        print(datetime.datetime.now().strftime('%Y-%m-%d,%H:%M:%S'))
        while True:
            global gimagelist
            global gCondition

            gCondition.acquire()#上锁
            while len(gimagelist)==0:
                gCondition.wait()#没有则等待
            url=gimagelist.pop()
            name=url.rsplit('/')[-1]#取名字，以url后面的部分做名字
            gCondition.release()
            download_pic(url,name)#下载图片
            
print(datetime.datetime.now().strftime('%Y-%m-%d,%H:%M:%S'))

# if __name__=='__main__':
Producer().start()

for i in range(10):#十个消费者线程数
    Consumer().start()
 