#proses hasil prediksi dari predict2_yw
#jangan lupa hapus baris terakhir efek dummy

#clarity
#fileInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/run2/prediction_run2_clarity.csv"
#fileOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/run2/clarity_run2.predict"

#conciseness
fileInput  = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/run2/prediction_run2_concis.csv"
fileOutput = "/media/yudiwbs/programdata/ubuntu/lombalazada/data/validasi/run2/concis_run2.predict"



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
        fOutput.write(isi+"\n")
        print("Proses baris ke-"+str(i+1))
        i = i+1
    #endfor
finally:
    fInput.close()
    fOutput.close()