import sys
import re
import os.path
from nltk.corpus import stopwords

location = raw_input("Where is the file?")
location_string = str(location)
file = open(location_string, 'r').read().replace(r'\n',' ')

word_list = re.sub("[^\w-]","\n", file).split()

cache_stop_word = set(stopwords.words("english"))
cache_stop_word.update(('and','I','A','And','So','arnt','This','When','It','many','Many','so','cant','Yes','yes','No','no','These','these', 'study'))
print cache_stop_word

def test_function():
    print file
    cleaned_text = ' '.join([word for word in word_list if word not in cache_stop_word])
    print cleaned_text
    save_to_file(cleaned_text)

def save_to_file(cleaned_text):
    print 'creating new text file'
    name_of_file = raw_input('Input name of the text file:') + '.txt'
    save_path = raw_input('Where you want to save it:')
    complete_name = os.path.join(save_path, name_of_file)

    try:
        file = open(complete_name, 'w')
        file.write(cleaned_text)
        file.close()
    except:
        print 'There is something wrong!'
        sys.exit(0)

test_function()
