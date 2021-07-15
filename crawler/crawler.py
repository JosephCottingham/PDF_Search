import re
from urllib import urlopen

html = urlopen("http://www.nycgo.com/venues/thalia-restaurant#menu")
html_doc = html.read()

match = re.search(b'\"(.*?\.pdf)\"', html_doc)
pdf_url = "http://www.nycgo.com" + match.group(1).decode('utf8')


text_file = open("pdf.txt", "w")
n = text_file.write(pdf_url)
text_file.close()