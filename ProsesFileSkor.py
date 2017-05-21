#memproses file skor
#contoh per baris: [-19.50937271  21.65632629]
#ganti jadi probabilitas
# HATI_HATI BARIS DUMMY


import re
import numpy as np

#HATI2 nama file
#fileInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/run4/score_concis_run4.csv"
#fileOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/run4/prob_concis_run4.csv"

fileInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun6/score_clarity_training.csv"
fileOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun6/prob_clarity_training.csv"


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()



fInput  = open(fileInput,"r")
fOutput = open(fileOutput, "w")

try:
    i = 0
    for line in fInput:
        line2 = line.rstrip('\n').strip()
        line2 = re.sub('([\[\]])', ' ', line2)
        #buang dulu kurung siku
        angka = line2.split()
        a0 = float(angka[0])
        a1 = float(angka[1])
        scores = []
        scores.append(a0)
        scores.append(a1)
        prob = softmax(scores)
        fOutput.write(str(prob[1])+"\n")
        i = i+1
        print("proses baris ke:"+str(i))
    #endfor
finally:
    fInput.close()
    fOutput.close()