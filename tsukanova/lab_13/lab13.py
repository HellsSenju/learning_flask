# ОБЗОР СИСТЕМ РЕКОМЕНДАЦИЙ В ОБЛАСТИ МЕДИЦИНЫ
# cтр 164

import pymorphy3
from pymystem3 import Mystem
from nltk import BigramCollocationFinder, BigramAssocMeasures, FreqDist, ConditionalFreqDist, SnowballStemmer, bigrams
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from itertools import permutations, chain
from functools import partial

file = open('text.txt', 'r', encoding="utf-8")
text = file.read()

# извлечение токенов ("слов") из текста
tokens = word_tokenize(text.lower())
file.close()

stop_words = stopwords.words("russian")
stop_words.extend(['т.д.', '.', ',', '"', '""', ':', ';', '(', ')', '[', ']', '{', '}', '«', '»', '-', '%', '•'])

filtered_tokens = list()
filtered_tokens_str = " ".join([word for word in tokens if word not in stop_words])

# Удаляем из текста Стоп-слова
for token in tokens:
    if token not in stop_words:
        filtered_tokens.append(token)

# m = Mystem()

# слова в канонической, основной форме
# lemmatized_words = m.lemmatize(filtered_tokens_str)


morph = pymorphy3.MorphAnalyzer()

# слова в канонической, основной форме
main_words_form = set()

# кол-во существительных во множественном числе
kol = 0
for word in filtered_tokens:
    p = morph.parse(word)[0]
    print(morph.normal_forms(word)[0])
    main_words_form.add(p.normal_form)
    if 'NOUN' in p.tag and 'plur' in p.tag:
        kol += 1

print(f'кол-во существительных во множественном числе - {kol}')

str = ""
bigrams = set(chain.from_iterable(map(partial(permutations,
                                              r=2),
                                      zip(filtered_tokens_str,
                                          filtered_tokens_str[1:],
                                          filtered_tokens_str[2:]))))
print(bigrams)

# Создание списка двусловий (биграмм)
finder = BigramCollocationFinder.from_words(filtered_tokens)

bigram_measures = BigramAssocMeasures()

print(finder.nbest(bigram_measures.raw_freq(), len(filtered_tokens)))

n = len(filtered_tokens)
word_fd = FreqDist(filtered_tokens)
bigram_fd = ConditionalFreqDist(bigrams(filtered_tokens))
