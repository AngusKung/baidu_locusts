# baidu_locusts
Crawl and graze all the Chinese datas from Baidu Baike, including title and summary from all the clauses.<br/>
It's made because the Chinese clause in Wikipedia has too less information.<br/>
Furthermore, it's an advanced version of "baike_spider"with greediness for all datas and kill-and-continue check points.<br/>
Suggestions or discussions are definitly welcome :)<br/>
<br/>
百度百科的中文語料爬蟲，<br/>
能夠爬取所有條目的標題和摘要！<br/>
這是一個從「baike_spider」修改而來的版本，<br/>
加強了<br/>
1.能夠爬取「所有」條目的能力。<br/>
2.因條目數過多，而能夠存檔記憶點以利分次性爬取。<br/>
3.分批次存檔並清空RAM，以免佔用過多資源<br/>
非常歡迎討論或指教 :)

### Requirement
python 2.7<br/>
urllib2<br/>
Beautifulsoup (bs4)<br/>

### Usage
>mkdir txt;mkdir urls<br/>
>python locusts_main [-new] [-load PATH]
