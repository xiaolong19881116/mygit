#/user/bin/env python   

# -*- coding:utf-8 -*-
import urllib.request

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        
        html = urllib.request.urlopen(url)
        
        if html.getcode() != 200:
            return None
        
        return html.read()
        