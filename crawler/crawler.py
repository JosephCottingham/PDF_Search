
from nltk.corpus import words
from uuid import uuid4
from lxml.html import fromstring
from requests import get
import random, time, os

base_path = os.environ.get("PDF_BASE_PATH") or 'pdf/'

def crawl():
    while True:
        try:
            print('Sleep')
            time.sleep(random.randint(0,15))
            print('Wake')
            word = random.choice(words.words())
            print(word)
            raw = get(f"https://www.google.com/search?q=filetype%3Apdf&q={word}").text
            file = open('sit', 'w')
            file.write(raw)
            file.close()
            index= 0
            print(len(raw))
            while index < len(raw):
                index = raw.find('/url?q', index)
                if index == -1:
                    break
                index = index + 7
                end_index = raw.find('&amp;', index)
                url = raw[index:end_index]
                if ('http' in url and check_pdf(url)):
                    write_url_to_text_file(url)
        except:
            continue

def check_pdf(url):
    r = get(url, allow_redirects=True)
    print(r.headers.get('content-type'))
    return r.headers.get('content-type') == 'application/pdf'

def write_url_to_text_file(url):
    text_file_name = f"{ uuid4().hex }.txt"
    text_file = open(base_path+text_file_name, "w")
    text_file.write(url)
    text_file.close()
    print(f'{url} written to: {text_file_name}')

if __name__ == '__main__':
    crawl()
