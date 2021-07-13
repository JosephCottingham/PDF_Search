import os, time
from uuid import uuid4
import fitz
import pytesseract
import io
from PIL import Image
from db import (insert_pdf_record, insert_keyword_record, insert_pdf_keyword_relation_record)
test_pdf = 'research/Paving the Way to Equity CMS OMH Progress Report.pdf'

base_path = os.environ.get("PDF_BASE_PATH") or 'pdf/'


def check_for_new_pdf():
    files = os.listdir(base_path)
    print(f'File Check Status: {files}')
    for file in files:
        try:
            if file.split('.')[-1] != 'txt':
                continue
            url = open(f"{base_path}{file}", "r").read()
            print(url)
            r = requests.get(url, allow_redirects=True)
            if r.headers.get('content-type') != 'application/pdf' or header.get('content-length', None) and header.get('content-length', None) < 2e8:
                return
            file_path = base_path+uuid4().hex + '.pdf'
            open(file_path, 'wb').write(r.content)
            index_pdf(file_path, url)
            os.remove(f"{base_path}{file}")
        except Exception as e:
            print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
            traceback.print_exc()
            continue

def index_pdf(path_to_file, url):
    file_name = path_to_file.split('/')[-1]
    print(f'PDF: { file_name }')
    pdf_file = fitz.open(path_to_file)
    if abs(get_avg_images_per_page(pdf_file)) < .10 and get_avg_words_per_page(pdf_file) > 15:
        print('PDF Failed Index requirements')
        os.remove(path_to_file)

    word_list = []
    img_paths = []
    for page_index in range(len(pdf_file)):
        page = pdf_file[page_index]
        for image_index, img in enumerate(page.getImageList(), start=1):
            xref = img[0]
            base_image = pdf_file.extractImage(xref)
            image_bytes = base_image["image"]
            # get the image extension
            image_ext = base_image["ext"]
            # load it to PIL
            image = Image.open(io.BytesIO(image_bytes))
            # save it to local disk
            img_path = f"pdf_imgs/image{page_index+1}_{image_index}.{image_ext}"
            img_paths.append(img_path)
            image.save(open(img_path, "wb"))
        word_list = word_list + get_words_from_pdf_page(page)
            
    for img_path in img_paths:
        word_list += get_words_from_image(img_path)
    keyword_list = get_keywords_from_list(word_list, num=10)
    print(f'Keywords: {keyword_list}')
    os.remove(path_to_file)
    insert_index_into_db(keyword_list, url, file_name)


def get_keywords_from_list(word_list, num=10):
    top_word_occurrences = []
    word_occurrences = {}
    for word in word_list:
        if not word_occurrences.get(word):
            word_occurrences[word] = 0
        else:
            word_occurrences[word] += 1

        if word in top_word_occurrences:
            continue

        if len(top_word_occurrences) < num:
            top_word_occurrences.append(word)
        else:
            lowest_top_word_index = 0
            for index in range(1, len(top_word_occurrences)):
                if word_occurrences[top_word_occurrences[index]] < word_occurrences[top_word_occurrences[lowest_top_word_index]]:
                    lowest_top_word_index=index
            if word_occurrences[top_word_occurrences[lowest_top_word_index]] < word_occurrences[word]:
                top_word_occurrences[lowest_top_word_index] = word
    return top_word_occurrences
    

    
def get_words_from_image(path_to_file):
    img = Image.open(path_to_file)  
    word_string = pytesseract.image_to_string(img)
    word_list = []
    for word in word_string.split(' '):
        for word_2 in word.split('\n'):
            if word_2 != '':
                word_list.append(word_2)
    return word_list

def get_words_from_pdf_page(page):
    word_list = []
    for word in page.get_text_words():
        word_list.append(word[4])
    return word_list

def get_avg_images_per_page(pdf_file):
    total_images = 0
    total_pages = len(pdf_file)
    for page_index in range(total_pages):
        page = pdf_file[page_index]
        total_images += len(page.getImageList())
    return float(total_images) / float(total_pages)

def get_avg_words_per_page(pdf_file):
    total_words = 0
    total_pages = len(pdf_file)
    for page_index in range(total_pages):
        page = pdf_file[page_index]
        total_words += len(page.get_text_words())
    return float(total_words) / float(total_pages)


def insert_index_into_db(keywords, url, title):
    pdf_id = insert_pdf_record(url, title)
    for keyword in keywords:
        keyword_id = insert_keyword_record(keyword)
        insert_pdf_keyword_relation_record(pdf_id, keyword_id)


if __name__ == '__main__' and True:
    while True:
        check_for_new_pdf()
        time.sleep(10)