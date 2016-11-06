# coding=utf-8
import argparse
import sys

import url_manager,html_parser,html_outputer

class LocustsMain(object):

    def __init__(self,path=""):
        self.urls = url_manager.UrlManager(path)
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.root_url = "http://baike.baidu.com/view/21087.htm"
        self.path = path
        self.new = True if len(path)==0 else False

    def crawl(self):
        if self.new:
            count = 1
            self.urls.add_new_url(self.root_url)
        else:
            count = int(self.path.split('_')[1].split('k')[0])

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
    parser = argparse.ArgumentParser()
    parser.add_argument('-new', help='Start a whole new crawling session', action="store_true")
    parser.add_argument('-load', help='Load former urls in pickle form and continue crawling', dest="path", action="store")
    
    if len(sys.argv[1:])==0:
        parser.print_help()
        parser.exit()
    args = parser.parse_args()

    if args.new:
        obj_locusts = LocustsMain()
        obj_locusts.crawl()
    else:
        obj_locusts = LocustsMain(args.path)
        obj_locusts.crawl()
        
