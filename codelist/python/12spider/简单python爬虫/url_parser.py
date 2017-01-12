from bs4 import BeatifulSoup
import re
import urlparse
class HtmlParser(object):
	"""url解析器：解析Url内容"""

	def _get_new_urls(self,page_url,html_cont):
		new_urls = set()
		#/view/123.htm
		links = soup.find_all("a",href = re.compile(r"/view/\d+\.htm"))
		for link in links:
			new_url = link["href"]
			new_full_url = urlparse.urljoin(page_url,new_url)
			new_urls.add(new_full_url)

		return new_urls

    def _get_new_data(self,page_url,html_cont):
    	#<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
    	res_data = {}
    	res_data['url'] = page_url
    	title_node = soup.find("dd",class_ = "lemmaWgt-lemmaTitle-title").find("h1")
    	res_data['title'] = title_node.get_text()
    	#<div class="lemma-summary" label-module="lemmaSummary">
    	summary_node = soup.find("div",class_ = "lemma-summary")
    	res_data['summary'] = summary_node.get_text()
    	retrun res_data

	def parse(self, page_url,html_cont):
		if page_url is None or html_cont is None:
			return None
		
		soup = BeatifulSoup(html_cont,"html.parser",from_encoding = "utf-8")
		new_urls = self._get_new_urls(page_url,html_cont)
		new_data = self._get_new_data(page_url,html_cont)
		return new_urls,new_data