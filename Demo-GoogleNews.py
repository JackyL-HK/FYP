query = 'Hong Kong Student Suicide'
wordList = ('student', 'suicide', 'pressure', 'sad')
skipList = '(see also|contact us|HK01.com|comments|copyright|TL/JC/RA|RT/RA|western)'
from googlesearch import search_news
from bs4 import BeautifulSoup
import requests
import re
# import spacy
import en_core_web_sm
from textblob import TextBlob
# from textblob.np_extractors import ConllExtractor
# from textblob.sentiments import NaiveBayesAnalyzer
import csv
print('Fetching news url from Google News...')
urlList = list(search_news("Hong Kong, Student, Suicide", stop=50,
                           tld='com.hk', tbs='ctr:countryHK', extra_params={'cr': 'countryHK'}))
with open('news_url.txt', 'w+', encoding='utf-8') as fp:
    fp.write('\n'.join(urlList))
print('Done fetching.')
with open('pageContent.txt', 'w+', encoding='utf-8') as fp:
    for n, url in enumerate(urlList):
        print("\n", n, url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        text = ' '.join(map(BeautifulSoup.get_text, soup.find_all('p')))
        fp.write('\n'+text)

with open("pageContent.txt", 'r', encoding='utf-8') as fp:
    pageContent = fp.read()

    with open("NegPolarity-TextBlob-Default.csv", 'w+', encoding='utf-8') as fp:
        writer = csv.writer(fp, delimiter=',')
        data = [("string", "polarity")]
        tb = TextBlob(pageContent)
        for tbs in tb.sentences:
            if not re.search(r'{}'.format(skipList), str(tbs), re.IGNORECASE):
                polarity = tbs.sentiment.polarity
                if polarity < 0:
                    row = str(tbs), polarity
                    data.append(row)
                    print(row)
        writer.writerows(data)


# tb2 = TextBlob(pageContent, analyzer=NaiveBayesAnalyzer(),
#                np_extractor=ConllExtractor())
# for tb2s in tb2.sentences:
#     polarity = tb2s.sentiment.classification
#     if polarity == 'neg':
#         print(tb2s)
#         print('pos:', tb2s.sentiment.p_pos, 'neg:', tb2s.sentiment.p_neg)


# nlp = spacy.load('en')
nlp = en_core_web_sm.load()
doc = nlp(pageContent)

with open("ShortLines.txt", 'w+', encoding='utf-8') as fp:
    for word in doc:
        if word.lemma_ in wordList:
            subtree_span = doc[word.left_edge.i: word.right_edge.i + 1]
            printText = subtree_span.text + ' | ' + subtree_span.root.text
            fp.write('\n'+printText)
            print(printText)

with open("LongLines.txt", 'w+', encoding='utf-8') as fp:
    for sentence in doc.sents:
        if not re.search(r'{}'.format(skipList), str(sentence), re.IGNORECASE):
            for word in sentence:
                if word.lemma_ in wordList:
                    printText = str(sentence) + ' | ' + str(word)
                    fp.write('\n'+printText)
                    print(printText)
                    break
