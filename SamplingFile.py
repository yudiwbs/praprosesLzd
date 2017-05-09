#ambil sampling secara random
#untuk mengurangi jumlah baris (undersampling)

import random

jumTargetBaris = 3000

namaInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/out_clarity_train_bersih.label1"
namaOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/out_clarity_train_bersih_undersampling.label1"


fInput  = open(namaInput,"r")
fOutput = open(namaOutput,"w")

try:
    #hitung jumlah baris, sambil ambil data, jumlahnya lebih besar daripada jumlah targetbaris
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
