
import cv2
from pyzbar import pyzbar
import pymysql.cursors


# Veritabanı bağlantı bilgileri
db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='projem',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# İşaretçimizi oluşturalım
baglanti = db.cursor()

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
       
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        sql = "select * from film where filmAdi = '"+barcode_info+"'"
        baglanti.execute(sql)
        film_bilgisi = baglanti.fetchall()

        filmAdi         = "Filmin adi: "+film_bilgisi[0]["filmAdi"]
        filmKategori    = "Filmin kategorisi: "+film_bilgisi[0]["filmKategorisi"]
        filmTarih       = "Filmin tarihi: "+film_bilgisi[0]["filmTarihi"]
        filmYonetmen    = "Filmin Yonetmeni: "+film_bilgisi[0]["filmYonetmen"]
        filmSenarist    = "Filmin Senaristi: "+film_bilgisi[0]["filmSenarist"]
        ımbdPuani       = "Filmin IMDB puani: "+film_bilgisi[0]["ımbdPuani"]
        filmSuresi      = "Filmin suresi"+film_bilgisi[0]["filmSuresi"]
        
        cv2.putText(frame, filmAdi, (0,20), font, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, filmKategori, (0,80), font, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, filmTarih, (0,140), font, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, filmYonetmen, (0,200), font, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, filmSenarist, (0,260), font, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, ımbdPuani, (0,320), font, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, filmSuresi, (0,380), font, 0.5, (255, 255, 255), 1)
        


        #3
        with open("barcode_result.txt", mode ='w') as file:
            file.write("Recognized Barcode:" + barcode_info)
    return frame
def main():
    #1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    #2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame) #qr film adi gelir.
    
        cv2.imshow('Film bilgileri: ', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    #3
    camera.release()
    cv2.destroyAllWindows()
#4
if __name__ == '__main__':
    main()
