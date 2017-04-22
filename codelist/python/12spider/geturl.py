def getAllLinkReg(url,regStr):
	urls = set()
	from urllib.request import urlopen
	from bs4 import BeautifulSoup
	import urllib.parse
	import re
	html = urlopen(url)
	bsObj = BeautifulSoup(html.read())
	for link in bsObj.findAll("a",href=re.compile(regStr)):
		if 'href' in link.attrs:
			new_url = link.attrs['href']
			print(new_url)
			#urls.add(new_url)
			#new_full_url = urllib.parse.urljoin(url,new_url)

#https://www.youtube.com/watch?v=To3YL92HZyc&index=1&list=PLXO45tsB95cKKyC45gatc8wEc3Ue7BlI4
getAllLinkReg("https://www.youtube.com/watch?v=7j8-wN34hd4&index=1&list=PLbu9W4c-C0iB--RNIzTXVksxQEI4vLK5-","^/watch.*index")