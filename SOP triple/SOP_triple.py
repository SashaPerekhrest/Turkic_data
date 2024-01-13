import nltk
import random
import csv

nltk.download('punkt')

file_name = 'C:/Users/matve/Desktop/workspace/studi/parce/KG/kg_parced.txt'
delimiter = '$$$'

file = open(file_name, 'r', encoding="utf-8")
tmp = file.read()

csv_file = open('SOP.csv', 'w', newline="", encoding="utf-8")
writer = csv.writer(csv_file)
writer.writerow(["sentence_A", "sentence_B", "sentence_C", "SOP", "new_url", "main_url"])

textsWithUrls = tmp.split(delimiter)

for textWithUrls in textsWithUrls:
    text = textWithUrls.split("###")[0]
    url = textWithUrls.split("###")[1]
    mainUrl = textWithUrls.split("###")[2]
    sentences = nltk.sent_tokenize(text)

    last = ''
    iterator = 0
    count = len(sentences)
    for j in range(0, count , 3):
        if j+2 >= count:
            continue
        if len(sentences[j]) <= 17 or len(sentences[j+1]) <= 17 or len(sentences[j+2]) <= 17:
            continue
        k = random.randint(0, 1)
        if k == 1:
            writer.writerow([sentences[j].replace('\n',''), sentences[j+1].replace('\n',''), sentences[j+2].replace('\n',''), k , url, mainUrl])
        else:
            pos = random.randint(0, 4)
            if pos == 0:
                writer.writerow([sentences[j].replace('\n',''), sentences[j+2].replace('\n',''), sentences[j+1].replace('\n',''), k , url, mainUrl])
            elif pos == 1:
                writer.writerow([sentences[j+1].replace('\n',''), sentences[j].replace('\n',''), sentences[j+2].replace('\n',''), k , url, mainUrl])
            elif pos == 2:
                writer.writerow([sentences[j+1].replace('\n',''), sentences[j+2].replace('\n',''), sentences[j].replace('\n',''), k , url, mainUrl])
            elif pos == 3:
                writer.writerow([sentences[j+2].replace('\n',''), sentences[j].replace('\n',''), sentences[j+1].replace('\n',''), k , url, mainUrl])
            else:
                writer.writerow([sentences[j+2].replace('\n',''), sentences[j+1].replace('\n',''), sentences[j].replace('\n',''), k , url, mainUrl])
        count = len(sentences)
