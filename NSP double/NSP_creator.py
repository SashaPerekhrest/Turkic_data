import csv
import random
import nltk

nltk.download('punkt')

file_name = 'tt_parced.txt'
delimiter = '$$$'
file = open(file_name, 'r', encoding="utf-8")
tmp = file.read()

csv_file = open('NSP.csv', 'w', newline="", encoding="utf-8")
writer = csv.writer(csv_file)

# Записываем заголовки полей
writer.writerow(["sentence_A", "sentence_B", "sentence_C", "NSP", "new_url", "main_url"])

textsWithUrls = tmp.split(delimiter)
count_csv  = 0

for textWithUrls in textsWithUrls:
    splited_text = textWithUrls.split("###")
    if(len(splited_text) !=3):
        continue
    text = splited_text[0]   
    url = splited_text[1]
    mainUrl = splited_text[2]
    sentences = nltk.sent_tokenize(text)

    iterator = 0
    count = len(sentences)
    sen = sentences
    j=0
    for j in range(0, count , 2):
        if(j+1 >= count):
            continue

        k = random.randint(0, 1)
        if k==0 :
            iterator = j+1
            second_news = sentences[iterator].replace('\n','')
        else:
            iterator = random.randint(0, len(sen)-1)
            second_news = sen[iterator].replace('\n','')

        del sen[iterator]
        count = len(sentences)

        news = sentences[j].replace('\n','')
        if len(news) < 5 or len(second_news) < 5:
            continue

        g = random.randint(0, 1)
        if g == 0:
            writer.writerow([news, second_news, k , url, mainUrl])
        else:
            writer.writerow([second_news, news, k , url, mainUrl])
        count_csv += 1
        print(count_csv)