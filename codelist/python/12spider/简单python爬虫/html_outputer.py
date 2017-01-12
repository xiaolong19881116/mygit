class HtmlOutputer(object):
	"""HtmlOutputer 输出到html文档"""
	def __init__(self):
		self.datas = []

	def collect_date(self, data):
		if data is None:
			return
		datas.append(data)

	def output_html(self):
		fout = open("output.html","w")
		fout.write("<html>")
		fout.write("<body>")
		fout.write("<table>")

        for data in datas:
        	fout.write("<tr>")
        	fout.write("<td>%s</td>" % data['url'].encode("utf-8"))
        	fout.write("<td>%s</td>" % data['title'].encode("utf-8"))
        	fout.write("<td>%s</td>" % data['summary'].encode("utf-8"))
        	fout.write("</tr>")

		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")