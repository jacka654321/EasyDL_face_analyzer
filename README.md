EasyDL定制化图像识别-冲金说明

https://blog.csdn.net/jacka654321/article/details/83996415


爬虫和数据清洗步骤：

1、爬取 人脸素颜照、素颜大头照；

2、多重检测：

㈠调用 百度人脸识别 api(detect)，保留识别到的人脸图片；

https://aip.baidubce.com/rest/2.0/face/v3/detect

㈡调用 face++ 皮肤问题识别API接口(Face Analyze API)，分类保存图片；

https://api-cn.faceplusplus.com/facepp/v3/face/analyze

㈢调用 百度Easy DL刚训练好的 皮肤问题分类api，作机器最后筛选一遍；

https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/anchuang


3、人工筛查，去掉错误图片。
