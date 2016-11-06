# coding=utf-8
import pdb

class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self, count):
        fout = open('txt/title_summary_'+(count%1000)+'k.txt', 'w')
        fout2 = open('txt/title_'+(count%1000)+'k.txt','w')

        for data in self.datas:
            fout.write(data['title'].encode('utf-8')+' ')
            fout.write(data['summary'].replace('\n','').encode('utf-8')+'\n')
            fout2.write(data['title'].encode('utf-8')+'\n')

        fout.close()
        fout2.close()
    
    def reset_datas(self):
        self.datas = [] 
