#proses hasil prediksi dari predict2_yw

#clarity
#fileInput  = "/media/yudiwbs/programdata/ubuntu/cnn-text-classification-tf/runs/1494293835/prediction.csv"
#fileOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/run1/prediksi_clarity_downsample.predict"

#conciseness
fileInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/run1/prediction_concis_mentah_run1.csv"
fileOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/run1/prediksi_concis_downsample.predict"



fInput  = open(fileInput,"r")
fOutput = open(fileOutput, "w")

try:
    i = 0
    for line in fInput:
        line2 = line.rstrip('\n')
        #split berdasarkan koma
        #contoh: kita mau ambil angka yg terakhir
        #alksdfjlaj asjfdlkasjfd asdf, akldsfj a, alksf , 1.0
        komaStr = line2.split(",")
        isi = komaStr[len(komaStr)-1]
        #print(isi)
        #for j in range(len(komaStr)):
        #   if (j>1) and (j<len(komaStr)-2):
        #      isi = isi + komaStr[j] + " "
        #endfor
        fOutput.write(isi+"\n")
        print("Proses baris ke-"+str(i+1))
        i = i+1
    #endfor
finally:
    fInput.close()
    fOutput.close()