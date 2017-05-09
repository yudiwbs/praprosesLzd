from bs4 import BeautifulSoup

print("bersihkan html dari file")

#clarity
#namaInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/out_clarity_train.label0"
#namaOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/out_clarity_train_bersih.label0"

#concis
#namaInput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/out_concis_train.label0"
#namaOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/out_concis_train_bersih.label0"
namaInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/out_concis_train.label1"
namaOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/out_concis_train_bersih.label1"


#validasi
#namaInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/data_valid_hanyateks.csv"
#namaOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/data_valid_hanyateks_bersih.csv"


fTeks   = open(namaInput, "r")
fOutput = open(namaOutput,"w")

try:
    soup = BeautifulSoup(fTeks, 'lxml')
    teksBersih = soup.get_text()
    #print(teksBersih)

    arrBaris = teksBersih.split("\n")
    for line in arrBaris:
        line = line.strip().casefold()
        fOutput.write(line+"\n")
        #print(line)
        #endfor
    #end for
finally:
    fTeks.close()
    fOutput.close()