#reduksi vocab

import re

# fileKataBuang = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun3/temp3/testkatabuang.txt"
# fileInput     = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun3/temp3/coba.csv"
# fileOutput    = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun3/temp3/coba_vocabbuang.csv"


fileKataBuang = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun3/freqkatasatu.txt"
fileInput     = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun3/data_train_rapi_casefold.csv"
fileOutput    = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun3/data_train_rapi_casefold_vocabbuang.csv"

fKataBuang = open(fileKataBuang,"r")
fInput  = open(fileInput,"r")
fOutput = open(fileOutput, "w")

try:
    #load kata
    listKata = fKataBuang.read().split("\n")

    pola =""
    #tambah /b untuk wholeword
    for kata in listKata:
        if not(kata==""):
            pola = pola + "\\b" + kata + "\\b" + "|"

    #pattern = re.compile("|".join(listKata))  #nggak wholeword
    pattern = re.compile(pola)
    print(pola)

    i = 0
    for line in fInput:
        line2 = line.rstrip('\n')
        line2 = pattern.sub("", line2).strip()
        #print(line2)
        fOutput.write(line2+"\n")
        print("Proses baris ke-"+str(i+1))
        i = i+1
        # if (i==10):  #debug
        #     break
    #endfor
finally:
    fKataBuang.close()
    fInput.close()
    fOutput.close()
