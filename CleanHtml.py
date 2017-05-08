from bs4 import BeautifulSoup

print("bersihkan html")

namaInput = "/home/yudiwbs/lombalazada/data/out_clarity_train_kecil.label0"
namaOutput = "/home/yudiwbs/lombalazada/data/out_clarity_train_kecil_bersih.label0"

fTeks = open(namaInput)

try:
    soup = BeautifulSoup(fTeks, 'lxml')
    teksBersih = soup.get_text()
    #print(teksBersih)

    arrBaris = teksBersih.split("\n")
    for line in arrBaris:
        line = line.rstrip('\n').strip().casefold()
        print(line)
        #endfor
    #end for
finally:
    fTeks.close()