#mengurangi dimensi, buang stopwords
#perlu hitung freq kata

import operator



def proseFile(namaFile):
    fTeks = open(namaFile)
    try:
        for line in fTeks:
            line = line.rstrip('\n').strip().casefold()
            #print(line)
            arrKata = line.split(" ")

            for kata in arrKata:
               #print(kata)
               if (kata in dict):
                  dict[kata] = dict[kata] + 1
               else :
                  dict[kata] = 0
            #endfor
        #end for

    finally:
        fTeks.close()
    return


#end function

dict = {}
#proseFile("/home/yudiwbs/lombalazada/data/out_clarity_train.label0")
namaFile = "/home/yudiwbs/lombalazada/data/out_clarity_train_bersih.label0"
proseFile(namaFile)
sortedDict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
print(str(sortedDict))
#print(str(dict))