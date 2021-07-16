import requests
# Library for parsing HTML
from bs4 import BeautifulSoup
base_url = 'https://dumps.wikimedia.org/enwiki/'
index = requests.get(base_url).text
soup_index = BeautifulSoup(index, 'html.parser')
# Find the links on the page
dumps = [a['href'] for a in soup_index.find_all('a') if 
         a.has_attr('href')]

# print(dumps)


dump_url = base_url + '20210520/'

# print(dump_url)
# Retrieve the html
dump_html = requests.get(dump_url).text
# Convert to a soup
soup_dump = BeautifulSoup(dump_html, 'html.parser')
# Find list elements with the class file
soup_dump = soup_dump.find_all('li', {'class': 'file'})[:10]

# print(soup_dump)
  
# get the url from requests get method
read = requests.get(dump_url)
  
# full html content 
html_content = read.content
  
# Parse the html content 
soup = BeautifulSoup(html_content, "html.parser")
  # created an empty list for putting the pdfs
list_of_links = set()

# accessed the fist p tag in the html
l = soup.find('li')

# print(l)

# accessed all the anchors tag from given p tag
p = l.find_all('a')

# print(p)

# iterate through p for getting all the href links
for link in p:
	
	# original html links
	# print("links: ", link.get('href'))
	# print("\n")
	
	# converting the extention 
	bz2_link = (link.get('href')[:-5]) + ".bz2"
	
	# converted to .pdf
	print("converted bz2 links: ", bz2_link)
	print("\n")
	bz2_link = "https://dumps.wikimedia.org" + bz2_link
	# added all the pdf links to set
	list_of_links.add(bz2_link)


print(list_of_links)



import tensorflow as tf
from tensorflow import keras
import subprocess

# from tensorflow.python.keras.utils import get_file
saved_file_path = tf.keras.utils.get_file(
    fname = 'enwiki-20210520-pages-articles-multistream.xml.bz2', origin = 'https://dumps.wikimedia.org/enwiki/20210520/enwiki-20210520-pages-articles-multistream.xml.bz2')

print(saved_file_path)
lst = []
# data_path = "~/.keras/datasets/enwiki-20210520-pages-articles-multistream.xml.bz2"
# Iterate through compressed file one line at a time
for line in subprocess.Popen(['bzcat'], 
                              stdin = open(saved_file_path), 
                              stdout = subprocess.PIPE).stdout:
                              lst.append((line))
print(lst)