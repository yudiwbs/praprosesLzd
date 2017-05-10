#hitung freq vocab
#proses semua file dalam satu direktori
#tujuannya untuk praproses: membuang kata yang muncul kurang dari x kali
#output adalah vocab dan freq terurut dari yang paling kecil
#loop semua file dalam satu direktori



import os
import operator
posDir = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun3/temp3/"
namaFileOut = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun3/freqkata.txt"
namaFileOutSatu =  "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun3/freqkatasatu.txt" #kata yang hanya muncul satu kali, calon dibuang

dict = {}

def prosesFile(namaFile):
    fTeks = open(namaFile)
    try:
        for line in fTeks:
            line = line.rstrip('\n').strip().casefold()  #perlu casefold?
            #print(line)
            arrKata = line.split()

            for kata in arrKata:
               #print(kata)
               if (kata in dict):
                  dict[kata] = dict[kata] + 1
               else :
                  dict[kata] = 1
               #print(str(dict))
            #endfor
        #end for

    finally:
        fTeks.close()
    return




for fn in os.listdir(posDir):
    print ("Proses"+fn)
    prosesFile(posDir+fn)
#endfor
sortedDict = sorted(dict.items(), key=operator.itemgetter(1))
print(str(dict))
print(str(sortedDict))

try:
    fOut = open(namaFileOut,"w")
    fOutSatu = open (namaFileOutSatu, "w")
    print("Total vocab:"+str(len(sortedDict)))
    jum = 0;
    for key, value in sortedDict:
        fOut.write(key+","+str(value)+"\n")
        if (value==1) :
           jum = jum +1
           fOutSatu.write(key+"\n")
    #endfor
    print ("jum vocab dgn freq 1="+str(jum))
finally:
    fOut.close()
    fOutSatu.close()




#end function

#dict = {}
#proseFile("/home/yudiwbs/lombalazada/data/out_clarity_train.label0")
#namaFile1 = "/home/yudiwbs/lombalazada/data/out_clarity_train_bersih.label0"
#proseFile(namaFile1)

#print(str(dict))