#html dibiarkan tapi ditambah spasi misal <li>xxx</li> jadi < li > xxx <  / li >
#semua baris digunakan (semua field digabung)
#menggunakan casefold

import re

#namaInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/data_train.csv"
#namaOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/data_train_rapi_casefold.csv"


#validasi
namaInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/data_valid.csv"
namaOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/data_valid_rapi_casefold.csv"


fInput   = open(namaInput, "r")
fOutput  = open(namaOutput,"w")

try:
    i = 0
    for line in fInput:
        line2 = line.rstrip('\n').casefold()
        line2 = re.sub('([^0-9a-zA-Z])', r' \1 ', line2)
        #print(line2)
        fOutput.write(line2+"\n")

finally:
    fInput.close()
    fOutput.close()