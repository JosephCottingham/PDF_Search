import nltk
# nltk.download('wordnet')
# from nltk.corpus import wordnet as wn

from uuid import uuid4
from lxml.html import fromstring
from requests import get



def crawl():
    # for ss in wn.synsets('car'):
    #     for word in ss.lemma_names():
    word = '{word}'
    raw = get(f"https://www.google.com/search?q=filetype%3Apdf&q={word}").text
    # raw = get(f"http://www.pdfsearchengine.net/searchresult.html?cx=partner-pub-9634067433254658%3A9653363797&cof=FORID%3A10&ie=UTF-8&q=filetype%3Apdf+{word}&qfront={word}&siteurl=http%3A%2F%2Fwww.pdfsearchengine.net%2F&algorithm=filetype%3Apdf+").text
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

def check_pdf(url):
    r = get(url, allow_redirects=True)
    print(r.headers.get('content-type'))
    return r.headers.get('content-type') == 'application/pdf'

def write_url_to_text_file(url):
    text_file_name = f"{ uuid4().hex }.txt"
    text_file = open(text_file_name, "w")
    text_file.write(url)
    text_file.close()
    print(f'{url} written to: {text_file_name}')

if __name__ == '__main__':
    crawl()
