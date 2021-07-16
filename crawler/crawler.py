# for get the pdf files or url
import requests
import uuid

# for tree traversal scraping in webpage
from bs4 import BeautifulSoup

# for input and output operations
import io
import os

# For getting information about the pdfs
from PyPDF2 import PdfFileReader


# website to scrap
url = "https://en.wikipedia.org/wiki/PDF"

# get the url from requests get method
read = requests.get(url)

# full html content
html_content = read.content

# Parse the html content
soup = BeautifulSoup(html_content, "html.parser")
  # created an empty list for putting the pdfs
list_of_pdf = set()

# accessed the fist p tag in the html
l = soup.find('p')

# accessed all the anchors tag from given p tag
p = l.find_all('a')

# uid
unique_filename = str(uuid.uuid4())

import uuid
import random
random = str(uuid.UUID(int=random.getrandbits(128)))

# iterate through p for getting all the href links
for link in p:
	# original html links
	# print("links: ", link.get('href'))
	# print("\n")
	# converting the extention from .html to .pdf
	pdf_link = (link.get('href')[:-5]) + ".pdf"
	# converted to .pdf
	# print("converted pdf links: ", pdf_link)
	# print("\n")

	for link in pdf_link:

		pdf_link = url + pdf_link
		save_path = 'crawler/pdfs/'
		file_name =  str(random) + ".txt"
		completeName = os.path.join(save_path, file_name)
		text_file = open(completeName, "w")
		text_file.write(pdf_link)
		text_file.close()
		break



	# added all the pdf links to set
	# list_of_pdf.add(pdf_link) 



# for line in list_of_pdf:
	 


# save_path = 'crawler/pdfs/'
# file_name =  "pdf.txt"

# completeName = os.path.join(save_path, file_name)
# text_file = open(completeName, "w")

# s = str(list_of_pdf)
# s = s.strip('{}')
# n = text_file.write(s)

# text_file.write("\n")
# text_file.close()
# # s = s.strip(" ' ' ")




# with open('crawler/pdfs/pdf.txt','r') as pdf:

# 	for element in pdf:
# 		print(element)
		# n = text_file.write(element)
		# text_file.write("\n")
		# text_file.close()


# with open('crawler/pdfs/pdf.txt','r') as pdf:
# 	for line in pdf:
# 		s.strip().split(',')
# 		print(line)

        # with open(line.rstrip() + '.txt','w') as new_file:
        #     new_file.write(line)
