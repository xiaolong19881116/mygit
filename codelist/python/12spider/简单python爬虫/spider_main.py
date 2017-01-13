import url_manager,url_parser,html_outputer,html_downloader

class SpiderMain(object):
    """docstring for SpiderMain"""
    def __init__(self):
        self.urls = url_manager.UrlManage()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = url_parser.HtmlParser()
        self.ouputer = html_outputer.HtmlOutputer()
        
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s" % (count,new_url))
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.ouputer.collect_date(new_data)
                
                if count == 1000:
                    break
                
                count = count + 1 
            except:
                print("craw faild!")
            
        self.ouputer.output_html()
        
        

if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.htm"
    spider = SpiderMain()
    spider.craw(root_url)
    #spider.urls.add_new_url(root_url)
    #print(spider.urls)
    #print(spider.urls.has_new_url())
    #new_url = spider.urls.get_new_url()
    #print(new_url)
    #print("craw %d : %s" % (1,new_url))
    #html_cont = spider.downloader.download(new_url)
    #print(html_cont)
    #new_urls,new_data = spider.parser.parse(new_url,html_cont)
    #spider.urls.add_new_urls(new_urls)
    #spider.ouputer.collect_date(new_data)
    #print(len(spider.urls.new_urls))
    #spider.ouputer.output_html()
