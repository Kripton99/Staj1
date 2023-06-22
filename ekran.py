import tkinter as tk
import qrcode
import pymysql.cursors
from PIL import Image, ImageTk



#Veritabanı bağlantı bilgleri
db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='projem',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                             
                             
def film_ekle(adi,kategorisi,tarihi,yonetmen,senarist,puan,suresi):
    baglanti = db.cursor()
    ekle = baglanti.execute('INSERT INTO film VALUES(%s,%s,%s,%s,%s,%s,%s)',(adi,kategorisi,tarihi,yonetmen,senarist,puan,suresi))
    db.commit()
    
    #qr code üret.
    img = qrcode.make(adi)
    
    type(img)  # qrcode.image.pil.PilImage
    
    #print("krkodlar/"+adi+".png")
    img.save(adi+".png")
    #-----------------

    #resim acildi
    image1 = Image.open(adi+".png")
    
    
    #olusan qr ekranda gosteriliyor
    
    #Photoımage ile gösterilebilir hale getiriyor
    test = ImageTk.PhotoImage(image1)
    
    label1 = tk.Label(image=test)
    label1.image = test

    label1.place(x=600, y=80)


    labelqr = tk.Label(root, text='qr kodunuz')
    labelqr.config(font=('helvetica', 14))
    canvas1.create_window(700, 50, window=labelqr)



root= tk.Tk()





canvas1 = tk.Canvas(root, width = 1080, height = 720,  relief = 'raised') #ekranı olusturur 
canvas1.pack()





label1 = tk.Label(root, text='Bilgileri giriniz')
label1.config(font=('helvetica', 14))

canvas1.create_window(200, 50, window=label1)

label2 = tk.Label(root, text='Film adi')
label2.config(font=('helvetica', 10))
canvas1.create_window(50, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(180, 100, window=entry1)

label3 = tk.Label(root, text='Film kategorisi')
label3.config(font=('helvetica', 10))
canvas1.create_window(50, 150, window=label3)

entry2 = tk.Entry (root) 
canvas1.create_window(180, 150, window=entry2)


label4 = tk.Label(root, text='Film tarihi')
label4.config(font=('helvetica', 10))

canvas1.create_window(50, 200, window=label4)

entry3 = tk.Entry (root) 
canvas1.create_window(180, 200, window=entry3)

label5 = tk.Label(root, text='Film Yonetmeni: ')
label5.config(font=('helvetica', 10))
canvas1.create_window(50, 250, window=label5)

entry4 = tk.Entry (root) 
canvas1.create_window(180, 250, window=entry4)


label6 = tk.Label(root, text='Film senaristi')
label6.config(font=('helvetica', 10))
canvas1.create_window(50, 300, window=label6)

entry5 = tk.Entry (root) 
canvas1.create_window(180, 300, window=entry5)



label7 = tk.Label(root, text='IMDP puanı')
label7.config(font=('helvetica', 10))
canvas1.create_window(50, 350, window=label7)

entry6 = tk.Entry (root) 
canvas1.create_window(180, 350, window=entry6)

label8 = tk.Label(root, text='Film süresi')
label8.config(font=('helvetica', 10))
canvas1.create_window(50, 400, window=label8)



entry7 = tk.Entry (root) 
canvas1.create_window(180, 400, window=entry7)








def getSquareRoot ():
    
    film_adi          = entry1.get()
    film_kategorisi   = entry2.get()
    film_tarihi       = entry3.get()
    film_yonetmeni    = entry4.get()
    film_senarist    = entry5.get()
    film_imdp        = entry6.get()
    film_suresi      = entry7.get()

    
    film_ekle(film_adi,film_kategorisi,film_tarihi,film_yonetmeni,film_senarist,film_imdp,film_suresi)
    
button1 = tk.Button(text='QR KOD ÜRET', command=getSquareRoot, bg='red', fg='white', font=('helvetica', 16, 'bold'),width=17,height=5)
canvas1.create_window(125, 500, window=button1)

root.mainloop() #goruntu sonsuz donguye girerek ekran gitmez