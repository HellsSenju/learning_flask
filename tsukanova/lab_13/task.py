import pymorphy3
from math import log
from nltk import ConditionalFreqDist, ngrams, FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

morph = pymorphy3.MorphAnalyzer()

input_text = open('input.txt', 'r', encoding="utf-8")
# output_text = open('output_without_stop_words.txt', 'w', encoding="utf-8")

text = input_text.read().replace('\n', ' ')

# извлечение токенов ("слов") из текста
tokens = word_tokenize(text.lower())
input_text.close()

stop_words = stopwords.words("russian")
stop_words.extend(['т.д.', '.', ',', '"', '""', ':', ';', '(', ')', '[', ']', '{', '}', '-', '%', '•' '«', '»', '—'])

# удаление стоп слов
tokens = [word for word in tokens if word not in stop_words]
tokens_str = " ".join(word for word in tokens)
# output_text.write(tokens_str)

# кол-во существительных во единственном числе
kol = 0
for word in tokens:
    p = morph.parse(word)[0]
    if 'NOUN' in p.tag and 'sing' in p.tag:
        kol += 1

print(f'кол-во существительных в единственном числе - {kol}')


Alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п",
            "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

hits = [
    (Alphabet[i], text.count(Alphabet[i]))
    for i in range(len(Alphabet))
    if text.count(Alphabet[i])
]

all_chars = 0
for letter, frequency in hits:
    all_chars += frequency

for letter, frequency in hits:
    print(f'{letter.upper()}, {frequency}, {round(frequency/all_chars, 4) * 100} %')


# лемматизация (слова в канонической, основной форме)
lemmatize_tokens = [morph.normal_forms(word)[0] for word in tokens]
lemmatize_tokens_str = " ".join(word for word in lemmatize_tokens)

bigrams = list(ngrams(lemmatize_tokens_str.split(), 2))
bigrams_fd = ConditionalFreqDist(bigrams)

fdist = FreqDist()

kol_words = len(tokens)  # количество слов в тексте
for bigram in bigrams:
    x_y = bigrams_fd[bigram[0]][bigram[1]]  # частотность биграмы
    x = fdist.get(bigram[0])
    y = fdist.get(bigram[1])



