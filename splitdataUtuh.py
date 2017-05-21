# untuk labelnya ada dua kagori: clarity (0 dan 1) dan concisness (0 dan 1)
# supaya mengikuti lib cnn-klaisifkasiteks, maka perlu displit jadi dua file untuk setiap kategori
# bedanya dengan splitdata.py, program yang ini mengambil utuh semua baris!

# ambil file teksnya

# direktori tempat data, jangan lupa tambahkan slash diujung
# rootDir = "/home/yudiwbs/lombalazada/data/persiapanrun2/"
rootDir = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/persiapanrun3/"

fileSumber = rootDir + "data_train_rapi_casefold_vocabbuang.csv"
fileLabelClarity = rootDir + "clarity_train.labels"
fileTargetClarity0 = rootDir + "out_clarity_train_rapi_casefold_vocabbuang.label0"
fileTargetClarity1 = rootDir + "out_clarity_train_rapi_casefold_vocabbuang.label1"

fileLabelConcis = rootDir + "conciseness_train.labels"
fileTargetConcis0 = rootDir + "out_concis_train_rapi_casefold_vocabbuang.label0"
fileTargetConcis1 = rootDir + "out_concis_train_rapi_casefold_vocabbuang.label1"

print("Split dataset lomba ")

# ambil data label dari clarity
arrClarity = []
fSumberClarity = open(fileLabelClarity)
try:
    for line in fSumberClarity:
        arrClarity.append(line.rstrip('\n'))
finally:
    fSumberClarity.close()

# ambil data label dari conciseness
arrConcis = []
fSumberConcis = open(fileLabelConcis)
try:
    for line in fSumberConcis:
        arrConcis.append(line.rstrip('\n'))
finally:
    fSumberConcis.close()

# ambil data dari train
fSumber = open(fileSumber)

fTargetClarity0 = open(fileTargetClarity0, "w")
fTargetClarity1 = open(fileTargetClarity1, "w")
fTargetConcis0 = open(fileTargetConcis0, "w")
fTargetConcis1 = open(fileTargetConcis1, "w")

try:
    i = 0
    for line in fSumber:
        print("Proses baris ke-" + str(i + 1))

        # ----- proses clarity
        if arrClarity[i] == "1":
            fTargetClarity1.write(line)
        elif arrClarity[i] == "0":
            fTargetClarity0.write(line)
        else:
            print("<<< error clarity >>>")
        # endif

        #  ---- proses conciseness
        if arrConcis[i] == "1":
            fTargetConcis1.write(line)
        elif arrConcis[i] == "0":
            fTargetConcis0.write(line)
        else:
            print("<<< error  concis >>>")

        i = i + 1
finally:
    fSumber.close()
    fTargetClarity0.close()
    fTargetClarity1.close()
    fTargetConcis0.close()
    fTargetConcis1.close()
