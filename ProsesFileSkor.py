#memproses file skor
#contoh per baris: [-19.50937271  21.65632629]
#ganti jadi probabilitas

import re

fileInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/run3/score_concis.csv"
fileOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/run3/prob_concis.csv"

fInput  = open(fileInput,"r")
fOutput = open(fileOutput, "w")

try:
    i = 0
    for line in fInput:
        line2 = line.rstrip('\n').strip()
        line2 = re.sub('([\[\]])', ' ', line2)
        #buang dulu kurung siku
        angka = line2.split()

        print(angka[0]+"->"+angka[1])
        #fOutput.write(isi+"\n")
        #print("Proses baris ke-"+str(i+1))
        i = i+1
    #endfor
finally:
    fInput.close()
    fOutput.close()