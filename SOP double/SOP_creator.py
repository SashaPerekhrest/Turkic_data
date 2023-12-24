import csv
import random
import nltk

nltk.download('punkt')

file_name = 'tt_parced.txt'
delimiter = '$$$'
file = open(file_name, 'r', encoding="utf-8")
tmp = file.read()

csv_file = open('SOP.csv', 'w', newline="", encoding="utf-8")
writer = csv.writer(csv_file)

# Записываем заголовки полей
writer.writerow(["sentence_A", "sentence_B", "sentence_C", "SOP", "new_url", "main_url"])

textsWithUrls = tmp.split(delimiter)
count_csv = 1
for textWithUrls in textsWithUrls:
    splited_text = textWithUrls.split("###")
    if(len(splited_text) !=3):
        continue
    text = splited_text[0]
    url = splited_text[1]
    mainUrl = splited_text[2]
    sentences = nltk.sent_tokenize(text)

    last = ''
    iterator = 0
    count = len(sentences)
    j=0
    for j in range(0, count , 2):
        if(j+1 >= count):
            continue
        sentences[j] = sentences[j].replace('\n','')
        sentences[j+1] = sentences[j+1].replace('\n','')
        k = random.randint(0, 1)
        if k == 1:
            writer.writerow([sentences[j], sentences[j+1], k, url, mainUrl])
        else:
            writer.writerow([sentences[j+1],sentences[j], k , url, mainUrl])
        print(count_csv)
        count_csv +=1