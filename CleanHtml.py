from bs4 import BeautifulSoup

print("bersihkan html")



namaInput = "/home/yudiwbs/lombalazada/data/out_clarity_train.label0"
namaOutput = "/home/yudiwbs/lombalazada/data/out_clarity_train_bersih.label0"

fTeks   = open(namaInput)
fOutput = open (namaOutput,"w")

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