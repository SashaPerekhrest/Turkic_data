import nltk
import random
import csv

nltk.download('punkt')

file_name = 'C:/Users/matve/Desktop/workspace/studi/parce/KZ/kz_parced.txt'
delimiter = '$$$'

file = open(file_name, 'r', encoding='utf-8')
tmp = file.read()

csv_file = open('NSP_kz.csv', 'w', newline="", encoding="utf-8")
writer = csv.writer(csv_file)

# Записываем заголовки полей
writer.writerow(["sentence_A", "sentence_B", "sentence_C", "NSP", "new_url", "main_url"])

textsWithUrls = tmp.split(delimiter)

for textWithUrls in textsWithUrls:
    text = textWithUrls.split("###")[0]
    url = textWithUrls.split("###")[1]
    mainUrl = textWithUrls.split("###")[2]
    sentences = nltk.sent_tokenize(text)
    tmp = sentences
    iterator = 0
    count = len(sentences)
    for j in range(0, count - 1 , 3):
        if j+2 >= count:
            continue
        if j+1 >= count:
            continue
        if j >= count:
            continue
        if len(sentences[j]) <= 17 or len(sentences[j+1]) <= 17 or len(sentences[j+2]) <= 17:
            continue
        k = random.randint(0, 1)
        if k == 1:
            writer.writerow([sentences[j].replace('\n',''), sentences[j+1].replace('\n',''), sentences[j+2].replace('\n',''), k , url, mainUrl])
        else:
            pos = random.randint(0, 2)
            iterator = random.randint(0, len(tmp)-1)
            if pos == 0:
                writer.writerow([tmp[iterator].replace('\n',''), sentences[j+1].replace('\n',''), sentences[j+2].replace('\n',''), k , url, mainUrl])
                del tmp[iterator]
            elif pos == 1:
                writer.writerow([sentences[j].replace('\n',''), tmp[iterator].replace('\n',''), sentences[j+2].replace('\n',''), k , url, mainUrl])
                del tmp[iterator]
            elif pos == 2:
                writer.writerow([sentences[j].replace('\n',''), sentences[j+1].replace('\n',''), tmp[iterator].replace('\n',''), k , url, mainUrl])
                del tmp[iterator]
        count = len(sentences)

