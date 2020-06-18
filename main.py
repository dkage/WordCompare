import requests
import os


directory = 'words_files'
if not os.path.exists(directory):
  os.makedirs(directory)

url_br = 'https://raw.githubusercontent.com/pythonprobr/palavras/master/palavras.txt'
url_en = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'

response = requests.get(url_br)
open('words_files/words_br.txt', 'wb').write(response.content)
response = requests.get(url_en)
open('words_files/words_en.txt', 'wb').write(response.content)


file_br = open('words_files/words_br.txt', 'r', encoding='UTF8')
words_br = file_br.read().splitlines()

file_en = open('words_files/words_en.txt', 'r', encoding='UTF8')
words_en = file_en.read().splitlines()

words_repeated = list()
print('looking for words')
for word in words_br:
    if word in words_en:
        print('found word %s' % word)
        words_repeated.append(word)
print('finished')

with open('words_repeated.txt', 'w', encoding='UTF8') as f:
    for word in words_repeated:
        f.write("%s\n" % word)
        print(word)
