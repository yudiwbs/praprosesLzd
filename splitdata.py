# penjelasan dataset: https://competitions.codalab.org/competitions/16652#participate
# dataset lomba terdiri dari satu file csv
# The features are presented in comma-separated values format:
# country,sku_id,title,category_lvl_1,category_lvl_2,category_lvl_3,short_description, price,product_type
# For example:
# my,NO037FAAA8CLZ2ANMY,RUDY Dress,Fashion,Women,Clothing,"<ul> <li>Short Sleeve</li> <li>3 Colours 8 Sizes</li> <li>Dress</li> </ul> ",33.0,local

# untuk labelnya ada dua kagori: clarity (0 dan 1) dan concisness (0 dan 1)
# supaya mengikuti lib cnn-klaisifkasiteks, maka perlu displit jadi dua file untuk setiap kategori


# ambil file teksnya

#direktori tempat data, jangan lupa tambahkan slash diujung
#rootDir = "/home/yudiwbs/lombalazada/data/persiapanrun2/"
rootDir = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun2/"

fileSumber = rootDir+"data_train_rapi.csv"
fileLabelClarity  = rootDir+"clarity_train.labels"
fileTargetClarity0 = rootDir+"out_clarity_train_rapi.label0"
fileTargetClarity1 = rootDir+"out_clarity_train_rapi.label1"

fileLabelConcis   = rootDir+ "conciseness_train.labels"
fileTargetConcis0 = rootDir+ "out_concis_train_rapi.label0"
fileTargetConcis1 = rootDir+ "out_concis_train_rapi.label1"


print("Split dataset lomba ")

#ambil data label dari clarity
arrClarity = []
fSumberClarity = open(fileLabelClarity)
try:
    for line in fSumberClarity:
        arrClarity.append(line.rstrip('\n'))
finally:
    fSumberClarity.close()

#ambil data label dari conciseness
arrConcis = []
fSumberConcis = open(fileLabelConcis)
try:
    for line in fSumberConcis:
        arrConcis.append(line.rstrip('\n'))
finally:
    fSumberConcis.close()




#ambil data dari train
fSumber = open(fileSumber)

fTargetClarity0 = open (fileTargetClarity0,"w")
fTargetClarity1 = open (fileTargetClarity1,"w")
fTargetConcis0 = open (fileTargetConcis0,"w")
fTargetConcis1 = open (fileTargetConcis1,"w")

try:
    i = 0
    for line in fSumber:
        line2 = line.rstrip('\n')
        #print(line2)
        #split berdasarkan koma
        #masalahnya bisa kecampur antar koma pemisah field dengan koma yang berada di isian
        #buang dua koma di depan dan dua koma dibelakang
        #my,AD674FAASTLXANMY,Adana Gallery Suri Square Hijab – Light Pink,Fashion,Women,Muslim Wear,<ul><li>Material : Non sheer shimmer chiffon</li><li>Sizes : 52 x 52 inches OR 56 x 56 inches</li><li>Cut with curved ends</li></ul>,49.0,local
        komaStr = line2.split(",")


        isi = ""
        for j in range(len(komaStr)):
           if (j>1) and (j<len(komaStr)-2):
              isi = isi + komaStr[j] + " "
              #print(komaStr[i])
        #endfor i
        print("Proses baris ke-"+str(i+1))

        # ----- proses clarity
        if arrClarity[i] == "1":
            #print("1111 ===============================")
            #print(isi)
            fTargetClarity1.write(isi+"\n")

        elif arrClarity[i] == "0":
            #print("0000 ===============================")
            #print(isi)
            fTargetClarity0.write(isi+"\n")
        else:
            print("<<< error clarity >>>")
        #endif

        #  ---- proses conciseness
        if arrConcis[i] == "1":
            #print("1111 ===============================")
            #print(isi)
            fTargetConcis1.write(isi+"\n")

        elif arrConcis[i] == "0":
            #print("0000 ===============================")
            #print(isi)
            fTargetConcis0.write(isi+"\n")
        else:
            print("<<< error  concis >>>")

        i = i + 1

finally:
    fSumber.close()
    fTargetClarity0.close()
    fTargetClarity1.close()
    fTargetConcis0.close()
    fTargetConcis1.close()
