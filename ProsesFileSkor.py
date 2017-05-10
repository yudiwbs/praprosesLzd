#memproses file skor
#contoh per baris: [-19.50937271  21.65632629]
#skor diambil yg maksimum jika
#ganti jadi probabilitas


import re

fileInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/run3/score_concis.csv"
fileOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/run3/prob_concis.csv"

fInput  = open(fileInput,"r")
fOutput = open(fileOutput, "w")

try:
    i = 0
    val = 0
    max = -1
    maxSelisih = 0

    for line in fInput:
        line2 = line.rstrip('\n').strip()
        line2 = re.sub('([\[\]])', ' ', line2)
        #buang dulu kurung siku
        angka = line2.split()


        a0 = float(angka[0])
        a1 = float(angka[1])

        selisih = abs(abs(a0)-abs(a1))


        if (a0 > a1):
            val = a0
        else:
            val = a1
        if val>max:
           max = val

        if (selisih > maxSelisih) :
            maxSelisih = selisih


        #rentang = abs(a0) + abs(a1)
        #probabilitas hanya untuk kelas 1
        #if (rentang>0):
        #   prob = abs(a1) / rentang
        #else:
        #   prob = 0

        #if (val>100) :
        #   print(angka[0] + "->" + angka[1] + "->" + str(i+1) )

        if (selisih>7) :
           print(angka[0] + "->" + angka[1] + "->" + str(selisih) + "-->" + str(i+1) )

        #fOutput.write(isi+"\n")
        #print("Proses baris ke-"+str(i+1))
        i = i+1
    #endfor
    print("maks:"+str(max))
    print("maks selisih:" + str(maxSelisih))
finally:
    fInput.close()
    fOutput.close()