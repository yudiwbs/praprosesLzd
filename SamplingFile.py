#ambil sampling secara random
#untuk mengurangi jumlah baris (undersampling)

import random

jumTargetBaris = 4000

#clarity
#pastikan jumtargetbaris terisi
#namaInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun2/out_clarity_train_rapi.label1"
#namaOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun2/out_clarity_train_rapi_undersampling.label1"

#conciseness
#pastikan jumtargetbaris terisi
#namaInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun2/out_concis_train_rapi.label1"
#namaOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun2/out_concis_train_rapi_undersampling.label1"
namaInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun2/out_concis_train_rapi.label0"
namaOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun2/out_concis_train_rapi_undersampling.label0"



fInput  = open(namaInput,"r")
fOutput = open(namaOutput,"w")

try:
    #hitung jumlah baris, sambil ambil data, jumlahnya pasti lebih besar daripada jumlah targetbaris
    arrLine = []
    try:
        i = 0
        for line in fInput:
            arrLine.append(line.rstrip('\n'))
            i=i+1
    finally:
        fInput.close()

    print("Jumlah baris:"+str(i))

    #buang baris secara random
    probBuang = jumTargetBaris / i
    print("Prob buang:"+str(probBuang))

    i =0
    for line in arrLine:
        x = random.uniform(0, 1)
        if (x <= probBuang):
            fOutput.write(line + "\n")
            i=i+1
            print(str(i))
    #end for
finally:
    fInput.close()
    fOutput.close()
