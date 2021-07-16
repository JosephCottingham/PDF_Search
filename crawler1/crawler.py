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
url = input("Enter the website you'd like to scrape for PDF links ")
# url = "https://en.wikipedia.org/wiki/PDF"

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
random = str()


save_path = 'crawler/pdfs/'
file_name =  str(random) + ".txt"
completeName = os.path.join(save_path, file_name)

# iterate through p for getting all the href links
for link in p:

	# converting the extention from .html to .pdf
	pdf_link = (link.get('href')[:-5]) + ".pdf"

	pdf_link = url + pdf_link
	list_of_pdf.add(pdf_link)


save_path = 'crawler/pdfs/'
file_name =  "pdf.txt"

completeName = os.path.join(save_path, file_name)
text_file = open(completeName, "w")


#Preprocessing of pdf.txt
s = str(list_of_pdf)
s = s.strip('{}')
s = s.strip("'")
s = s.strip(" ' ' ") 
n = text_file.write(s)

text_file.write(s)
text_file.close()


# Preprocessing
f = open('crawler/pdfs/pdf.txt', 'r+')
n = f.read().replace(',', ',\n')
f.truncate(0)                    # remove file contents from begin
f.write(n)                       # write result into file :)
f.close()



#variables for for loop below
save_path_new = 'crawler/pdfs/'
file_name_new =  random + str(1) + ".txt"
completePath = os.path.join(save_path_new, file_name_new)


#Write all links to new files based on line number
f1 = open('crawler/pdfs/pdf.txt', 'r')
for i,text in enumerate(f1):
    open('crawler/pdfs/' + str(i + 1) + '.txt', 'w').write(text.replace(",", ""))


# f1 = open('crawler/pdfs/pdf.txt', 'r')
# for i,text in enumerate(f1):
#     open(completePath, 'w').write(text.replace("'", ""))
	


