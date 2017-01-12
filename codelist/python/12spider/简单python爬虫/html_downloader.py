import urllib2

class HtmlDownloader(object):
	"""下载URL内容"""
	def download(self, url):
		if url is None:
			return None

		html = urllib2.urlopen(url)

		if html.getcode() != 200:
			return None

		return html.read()
		