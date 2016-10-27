# coding=utf-8
import url_manager,html_downloader,html_parser,html_outputer

class LocustsMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager() 
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()   #取得url
                print 'craw %d : %s' % (count, new_url) #打印当前是第几个url
                html_cont = self.downloader.download(new_url)   #下载页面数据
                new_urls, new_data = self.parser.parse(new_url,html_cont)    #进行页面解析得到新的url以及数据

                self.urls.add_new_urls(new_urls) #添加新的url
                self.outputer.collect_data(new_data) #收集数据


                count = count + 1
            except:
                print 'craw failed'
            

            if count % 100 == 0:
                print "URLs to crawl:",len(self.urls.new_urls)

                self.outputer.output_html()   #利用outputer输出收集好的数据

if __name__=="__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_locusts = LocustsMain()   # 创建
    obj_locusts.craw(root_url)   # craw方法启动爬虫
