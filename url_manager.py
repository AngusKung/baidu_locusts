# coding=utf-8
import cPickle

class UrlManager(object):

    def __init__(self,path):
        if len(path) == 0:
            self.new_urls = set()
            self.crawled_urls = set()
        else:    
            with open(path,'rb') as fin:
                self.new_urls = fin.load
                self.crawled_urls = fin.load
    
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.crawled_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.crawled_urls.add(new_url)
        return new_url

    def save_urls(self,count):
        with open('urls/urls_'+str(count/1000)+'+k.pkl','wb') as fout:
            cPickle.dump(self.new_urls,fout)
            cPickle.dump(self.crawled_urls,fout)
        print "URLs have been pickled"
    

