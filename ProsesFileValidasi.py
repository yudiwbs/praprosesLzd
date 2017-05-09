#proses file validasi (data_valid.csv)
#bagusnya nanti digabung dengan splitdata (split data pake ini)


fileInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/data_valid.csv"
fileOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/data_valid_hanyateks.csv"

fInput  = open(fileInput,"r")
fOutput = open(fileOutput, "w")

try:
    i = 0
    for line in fInput:
        line2 = line.rstrip('\n')
        #split berdasarkan koma
        #masalahnya bisa kecampur antar koma pemisah field dengan koma yang berada di isian
        #buang dua koma di depan dan dua koma dibelakang
        #my,AD674FAASTLXANMY,Adana Gallery Suri Square Hijab – Light Pink,Fashion,Women,Muslim Wear,<ul><li>Material : Non sheer shimmer chiffon</li><li>Sizes : 52 x 52 inches OR 56 x 56 inches</li><li>Cut with curved ends</li></ul>,49.0,local
        komaStr = line2.split(",")
        isi = ""
        for j in range(len(komaStr)):
           if (j>1) and (j<len(komaStr)-2):
              isi = isi + komaStr[j] + " "
        #endfor
        fOutput.write(isi+"\n")
        print("Proses baris ke-"+str(i+1))
        i = i+1
    #endfor
finally:
    fInput.close()
    fOutput.close()

