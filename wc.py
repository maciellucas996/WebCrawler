import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def start(url):
    wordlist = [] #armazenar todo o conteudo do site passado
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')#requisição dos dados e transformar em html

    for each_text in soup.findAll('div', {'class': 'entry-content'}):#ele vai procurar por div e classe e tudo que existe de conteudo, transformando em string
        content = each_text.text

        words = content.lower().split()#transforma o conteudo em letras minusculas e vai dividir em linhas

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


def clean_wordlist(wordlist): #vai removar simbolos indesejados na wordlist
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%¨&*()_+'

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')#vai substituir o simbolo por vazio

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


def create_dictionary(clean_list):#cira um dicionario contendo todas as palavras
    word_count = {}

    for word in clean_list: #vai fazer um top 20 de palavras mais utilizadas no site
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1






    for key, value in sorted(word_count.items(),
                             key = operator.itemgetter(1)):
        print('% s: % s' % (key, value))

        c = Counter(word_count)

        top = c.most_common(10)
        print(top)

if __name__ == '__main__':
    start('https://www.geeksforgeeks.org/python-programming-laguage/?ref=leftbar')