query = 'Hong Kong, Student, Suicide'
wordList = ('student, suicide')
from googlesearch import search_news
from bs4 import BeautifulSoup
import requests
<<<<<<< HEAD
# import spacy
import en_core_web_sm
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
from textblob.sentiments import NaiveBayesAnalyzer
=======
import spacy
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
from textblob.sentiments import NaiveBayesAnalyzer
import csv
>>>>>>> dac151d6166d58e5751b922e046fbf2663ae01db

urlList = list(search_news("Hong Kong, Student, Suicide", stop=50))

fp = open('pageContent.txt', 'w+', encoding='utf-8')
for n, url in enumerate(urlList):
    print("\n", n, url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = ' '.join(map(BeautifulSoup.get_text, soup.find_all('p')))
    fp.write('\n'+text)
fp.close()

with open("pageContent.txt", 'r', encoding='utf-8') as fp:
    pageContent = fp.read()

<<<<<<< HEAD
with open("NegPolarity-TextBlob-Default.txt", 'w+', encoding='utf-8') as fp:
    tb = TextBlob(pageContent)
    fp.write("(")
    for tbs in tb.sentences:
        polarity = tbs.sentiment.polarity
        if polarity < 0:
            print(tbs)
            print('polarity', polarity)
            fp.write("('{}',{}),".format(tbs,polarity))
    fp.write(")")
=======
with open("NegPolarity-TextBlob-Default.csv", 'w+', encoding='utf-8') as fp:
    writer = csv.writer(fp, delimiter=',')
    data = [("string","polarity")]
    tb = TextBlob(pageContent)
    # fp.write("(")
    for tbs in tb.sentences:
        polarity = tbs.sentiment.polarity
        if polarity < 0:
            # print(tbs)
            # print('polarity', polarity)
            row = str(tbs), polarity
            data.append(row)
            print(row)
    writer.writerows(data)
    #         fp.write("('{}',{}),".format(tbs,polarity))
    # fp.write(")")
>>>>>>> dac151d6166d58e5751b922e046fbf2663ae01db
        # ((str,polar),(str,polar))
        # print('subjectivity', tbs.sentiment.subjectivity)
        # print('individual words', tbs.sentiment_assessments)

tb2 = TextBlob(pageContent, analyzer=NaiveBayesAnalyzer(),
               np_extractor=ConllExtractor())
for tb2s in tb2.sentences:
    polarity = tb2s.sentiment.classification
    if polarity == 'neg':
        print(tb2s)
        print('pos:', tb2s.sentiment.p_pos, 'neg:', tb2s.sentiment.p_neg)

<<<<<<< HEAD
# nlp = spacy.load('en')
nlp = en_core_web_sm.load()
=======
nlp = spacy.load('en')
>>>>>>> dac151d6166d58e5751b922e046fbf2663ae01db
doc = nlp(pageContent)

with open("ShortLines.txt", 'w+', encoding='utf-8') as fp:
    for word in doc:
        if word.lemma_ in ('student', 'suicide'):
            subtree_span = doc[word.left_edge.i: word.right_edge.i + 1]
            printText = subtree_span.text + ' | ' + subtree_span.root.text
            fp.write('\n'+printText)
            print(printText)

with open("LongLines.txt", 'w+', encoding='utf-8') as fp:
    for sentence in doc.sents:
        for word in sentence:
            if word.lemma_ in ('student', 'suicide'):
                printText = str(sentence) + ' | ' + str(word)
                fp.write('\n'+printText)
                print(printText)
                break
