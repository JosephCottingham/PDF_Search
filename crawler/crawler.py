
# for get the pdf files or url
import requests
  
# for tree traversal scraping in webpage
from bs4 import BeautifulSoup
  
# for input and output operations
import io
  
# For getting information about the pdfs
from PyPDF2 import PdfFileReader


# website to scrap
url = "https://www.geeksforgeeks.org/how-to-extract-pdf-tables-in-python/"
  
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
  
# iterate through p for getting all the href links
for link in p: 
      
    # original html links
    print("links: ", link.get('href'))
    print("\n")
      
    # converting the extention from .html to .pdf
    pdf_link = (link.get('href')[:-5]) + ".pdf"
      
    # converted to .pdf
    print("converted pdf links: ", pdf_link)
    print("\n")
      
    # added all the pdf links to set
    list_of_pdf.add(pdf_link)

s = str(list_of_pdf)

text_file = open("pdf.txt", "w")
n = text_file.write(s)
text_file.close()