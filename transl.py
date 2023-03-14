# from googletrans import Translator
# from bs4 import BeautifulSoup

# # Load the HTML file and parse it
# with open('D:/JOB TEST CODE/multiproceesing/new_folder/index.html', 'r',encoding="utf-8") as f:
#     html = f.read()
# soup = BeautifulSoup(html, 'html.parser')

# # Find all the tags containing text to translate
# tags_to_translate = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'a']
# for tag in tags_to_translate:
#     elements = soup.find_all(tag)
#     for element in elements:
#         # Translate the text using googletrans
#         translator = Translator(service_urls=['translate.google.com'])
#         translated_text = translator.translate(element.text, dest='hi').text
#         # Replace the original text with the translated text
#         element.string = translated_text

# # Write the translated HTML to a file
# with open('file_translated1.html', 'w',encoding="utf-8") as f:
#     f.write(str(soup))



# from googletrans import Translator
# from bs4 import BeautifulSoup

# # Load the HTML file and parse it
# with open('D:/JOB TEST CODE/multiproceesing/new_folder/index.html', 'r', encoding='utf-8') as f:
#     html = f.read()
# soup = BeautifulSoup(html, 'html.parser')

# # Find all the tags containing text to translate
# tags_to_translate = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'a']
# for tag in tags_to_translate:
#     elements = soup.find_all(tag)
#     for element in elements:
#         # Translate the text using googletrans
#         translator = Translator(service_urls=['translate.google.com'])
#         translated_text = translator.translate(element.text, dest='hi').text
#         # Replace the original text with the translated text
#         element.string = translated_text

# # Write the translated HTML to a file
# with open('file_translated1.html', 'w', encoding='utf-8') as f:
#     f.write(str(soup))


from multiprocessing import Pool
from googletrans import Translator
from bs4 import BeautifulSoup
import os



def convert(j):
    print(j)
    # Load the HTML file and parse it
    with open(j, mode='r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the tags containing text to translate
    tags_to_translate = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a','span']
    for tag in tags_to_translate:
        elements = soup.find_all(tag)
        for element in elements:
            try:
                # Translate the text using googletrans
                translator = Translator(service_urls=['translate.google.com'])
                translated_text = translator.translate(element.text, dest='hi').text
                # Replace the original text with the translated text
                element.string = translated_text
            except Exception as e:
            
                print(f'Error: element text is None in {tag}: {e}')
                element.string = element.text

    # Write the translated HTML to a file
    with open(j, mode='w', encoding='utf-8') as f:
        f.write(str(soup))
    print('CONVERSION COMPLETED: '+j)


if __name__ == '__main__':
    folder_path = "D:/JOB TEST CODE/multiproceesing/new_folder" # Replace with the path to your folder
    html_files = []

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is an HTML file
        if filename.endswith(".html"):
            # Add the file to the list of HTML files
            html_files.append(os.path.join(folder_path, filename))
    print(len(html_files))
    # convert(filename[1])
    pool = Pool()
    filenames = pool.map(convert, html_files)