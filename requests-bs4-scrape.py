query = "Hong Kong Secondary Student"
# testurl = "http://www.scmp.com/news/hong-kong/education/article/2133086/long-hours-too-much-homework-and-stressed-pupils-there"
# testurl = "http://www.scmp.com/news/hong-kong/education/article/2137893/volunteering-gift-keeps-giving-students-cvs"
# urllist = [testurl]
from googlesearch import search, search_news
from textblob import TextBlob
from textblob import Word
from textblob.np_extractors import ConllExtractor
from textblob.sentiments import NaiveBayesAnalyzer
for url in search("Hong Kong Secondary Student", stop=20):
    print(url)
print("==============")
urllist = list(search_news("Hong Kong, Student, Suicide", stop=50))
print('\n'.join(urllist))

from bs4 import BeautifulSoup
import requests
import re

fp = open('test.txt', 'w+', encoding='utf-8')

for n, url in enumerate(urllist):
    print("\n", n, url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = ' '.join(map(BeautifulSoup.get_text, soup.find_all('p')))
    fp.write('\n'+text, )
    # wordlist = [
    #     i for i, item in enumerate(text.split()) if re.search('student', item)
    # ]
    # for n in wordlist:
    #     print(' '.join(text.split()[n - 8:n + 8]))
fp.close()

with open("test.txt", 'r', encoding='utf-8') as fp:
    # soup = BeautifulSoup(fp, 'html.parser')
    # print(*map(BeautifulSoup.get_text,soup.find_all('p')))
    # testtext = ' '.join(map(BeautifulSoup.get_text, soup.find_all('p')))
    testtext = fp.read()
print(len(testtext))


tb = TextBlob(testtext)
print('subjectivity', tb.sentiment.subjectivity)
print('polarity', tb.sentiment.polarity)
print('individual words', tb.sentiment_assessments)
# print('list of noun', tb.noun_phrases)
for sent in tb.sentences:
    print(sent)
tb2 = TextBlob(testtext, analyzer=NaiveBayesAnalyzer(),
               np_extractor=ConllExtractor())
print(tb2.sentiment)
print(tb2.noun_phrases)

# for sent in tb.sentences:

print(Word('Student').lemmatize())
print(Word('student').lemmatize())
print(Word('Students').lemmatize())
print(Word('students').lemmatize())

from IPython.display import Image
import spacy
from spacy import displacy

nlp = spacy.load('en')
doc = nlp(testtext)
# for token in doc:
#     print(token.text)
# for sentence in doc.sents:
#     print(sentence)
for word in doc:
    if word.lemma_ in ('student', 'suicide'):
        subtree_span = doc[word.left_edge.i: word.right_edge.i + 1]
        print(subtree_span.text, '|', subtree_span.root.text)
for sentence in doc.sents:
    for word in sentence:
        if word.lemma_ in ('student', 'suicide'):
            print(str(sentence).strip('\n'), '|', word)
            break
for word in doc:
    if word.lemma_ in ('student'):
        print(''.join(w.text_with_ws for w in word.subtree))

# for word in doc:1
#     if word.dep_ in ('xcomp', 'ccomp'):
#         subtree_span = doc[word.left_edge.i : word.right_edge.i + 1]
#         print(subtree_span.text, '|', subtree_span.root.text)


doc = nlp(
    u'displaCy uses CSS and JavaScript to show you how computers understand language')
for word in doc:
    if word.dep_ in ('xcomp', 'ccomp'):
        subtree_span = doc[word.left_edge.i: word.right_edge.i + 1]
        print(subtree_span.text, '|', subtree_span.root.text)
        print(subtree_span.similarity(doc))
        print(subtree_span.similarity(subtree_span.root))
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import cv2
# wordcloud = WordCloud().generate(text)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()
# cv2.imshow('wordcloud', wordcloud.to_array())
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# lower max_font_size
# wordcloud = WordCloud(width=1920, height=1080).generate(text)
# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()
