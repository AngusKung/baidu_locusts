# coding=utf-8
import url_manager,html_parser,html_outputer

class LocustsMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager() 
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.parser.download(new_url)
                new_urls, new_data = self.parser.parse(new_url,html_cont)

                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)


                count = count + 1
            except:
                print 'craw failed'
            

            if count % 100 == 0:
                print "URLs to crawl:",len(self.urls.new_urls)
            if count % 10000 == 0:
                self.outputer.output_html(count)
                self.outputer.reset_datas
                self.urls.save_urls(count)

if __name__=="__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_locusts = LocustsMain()
    obj_locusts.craw(root_url)
