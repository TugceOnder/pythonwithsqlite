import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz.

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

def tablo_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)") # Sorguyu çalıştırıyoruz.
    con.commit() # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.
def deger_ekle():
    cursor.execute("INSERT INTO kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',261)")
    con.commit()

def deger_ekle2(isim, yazar, yayınevi, sayfa_sayısı):
        cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)", (isim, yazar, yayınevi, sayfa_sayısı))
        con.commit()

def verileri_al():
    cursor.execute("Select * From kitaplık") # Bütün bilgileri alıyoruz.
    data = cursor.fetchall() #Veritabanından bilgileri çekmek için fetchall() kullanıyoruz.
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)

def verileri_al2():
    cursor.execute("Select İsim, Yazar From kitaplık")  # isim ve yazarın ismini  özellikleri getir
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)

def verileri_al3(yayınevi): # verilen degere göre verileri getirme
    cursor.execute("Select * From kitaplık where Yayınevi = ?",(yayınevi,)) # Sadece yayınevi ,Everest olan kitapları alıyoruz.
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)

def verigüncelle(eski_yayınevi,yeniyayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi =  ?",(yeniyayınevi,eski_yayınevi))
    con.commit() # veri tabanı güncellemek veya eklemek istediğimiz

def verilerisil(yazar):
    cursor.execute("Delete  From kitaplık where Yazar = ?",(yazar,))
    con.commit()

#isim = input("İsim:")
#yazar = input("Yazar:")
#yayınevi = input("Yayınevi:")
#sayfa_sayısı = int(input("Sayfa Sayısı:"))

#deger_ekle2(isim, yazar, yayınevi, sayfa_sayısı)   # degerler ekleniyor
#deger_ekle()

#verileri_al2();   # lisedeki kitaplıkları sıraıyor

#verileri_al3("index")  # index verisini getirir
#verigüncelle("Everest","index")
#verilerisil("Ahmet Ümit") # tablodaki ""Ahmet Ümit yazar isimli verileri siliyor
verileri_al() #degisikleri görmek için


con.close()