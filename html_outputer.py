# coding=utf-8
import pdb

class HtmlOutputer(object):
    #初始化
    def __init__(self):
        self.datas = []

    def collect_data(self, data):   #收集数据
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):  #输出数据
        fout = open('txt/title_summary.txt', 'w')
        fout2 = open('txt/title.txt','w')

        for data in self.datas:
            fout.write(data['title'].encode('utf-8')+' ')
            fout.write(data['summary'].replace('\n','').encode('utf-8')+'\n')
            fout2.write(data['title'].encode('utf-8')+'\n')

        fout.close()
        fout2.close()
