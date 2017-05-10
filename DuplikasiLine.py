#kebalikannya dari sampling, secara random baris ditambahkan sampai memenuhi kuota
#misalnya tadinya 2000 baris diduplikasi sampai 10000

import random

jumTargetBaris = 6000

#clarity
namaInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun2/out_clarity_train_rapi.label0"
namaOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun2/out_clarity_train_rapi_oversampling.label0"

#conciseness
#namaInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/out_concis_train_bersih.label1"
#namaOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/out_concis_train_bersih_undersampling.label1"


fInput  = open(namaInput,"r")
fOutput = open(namaOutput,"w")

try:
    #hitung jumlah baris, sambil ambil data, jumlahnya pasti lebih besar daripada jumlah targetbaris
    arrLine = []
    try:
        i = 0
        for line in fInput:
            arrLine.append(line)
            i=i+1
    finally:
        fInput.close()

    jumBaris = i
    print("Jumlah baris:"+str(jumBaris))
    selisih = jumTargetBaris - jumBaris

    #tambah baris yang asli
    for line in arrLine:
        fOutput.write(line)
    #endfor

    #tambah baris secara random sebanyak selisih
    for i in range(0,selisih):
        x = random.randint(0, jumBaris  - 1 )
        fOutput.write(arrLine[x])
    #end for
    print("selesai..")

finally:
    fInput.close()
    fOutput.close()
