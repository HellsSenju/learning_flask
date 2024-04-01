# ОБЗОР СИСТЕМ РЕКОМЕНДАЦИЙ В ОБЛАСТИ МЕДИЦИНЫ
# cтр 164

import pymorphy3
from math import log
from nltk import ConditionalFreqDist, ngrams
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

morph = pymorphy3.MorphAnalyzer()

file = open('text.txt', 'r', encoding="utf-8")
text = file.read()

# извлечение токенов ("слов") из текста
tokens = word_tokenize(text.lower())
file.close()

stop_words = stopwords.words("russian")
stop_words.extend(['т.д.', '.', ',', '"', '""', ':', ';', '(', ')', '[', ']', '{', '}', '-', '%', '•' '«', '»'])

# удаление стоп слов
tokens = [word for word in tokens if word not in stop_words]

# кол-во существительных во множественном числе
kol = 0
for word in tokens:
    p = morph.parse(word)[0]
    if 'NOUN' in p.tag and 'plur' in p.tag:
        kol += 1

print(f'кол-во существительных во множественном числе - {kol}')

# лемматизация (слова в канонической, основной форме)
lemmatize_tokens = [morph.normal_forms(word)[0] for word in tokens]
lemmatize_tokens_str = " ".join(word for word in lemmatize_tokens)

bigrams = list(ngrams(lemmatize_tokens_str.split(), 2))
bigrams_fd = ConditionalFreqDist(bigrams)

summ_freq = 0  # суммарная частотность всех биграм
for bigram in bigrams:
    summ_freq += bigrams_fd[bigram[0]][bigram[1]]

res = {}
for bigram in bigrams:
    a = bigrams_fd[bigram[0]][bigram[1]]  # частотность биграмы
    d = summ_freq - a  # суммарная частотность остальных биграм
    b = 0  # суммарная частотность отличных от данной биграм с той же самой левой частью
    c = 0  # суммарная частотность отличных от данной биграм с той же самой правой частью
    for b_ in bigrams:
        if bigram[0] == b_[0] and bigram[1] != b_[1]:
            b += bigrams_fd[b_[0]][b_[1]]

        if bigram[0] != b_[0] and bigram[1] == b_[1]:
            c += bigrams_fd[b_[0]][b_[1]]

    res[bigram] = (a * log(a + 1) + b * log(b + 1) + c * log(c + 1) + d * log(d + 1) - (a + b) * log(a + b + 1) -
                   (a + c) * log(a + c + 1) - (b + d) * log(b + d + 1) - (c + d) * log(c + d + 1) +
                   (a + b + c + d) * log(a + b + c + d))


# сортировка биграм по значению Log-Likelihood
sorted_res = sorted(res.items(), key=lambda x: x[1], reverse=True)

print('10 наиболее статистически значимых биграм: ')
for item in sorted_res[:10]:
    print(item)
