#Membuat variabel global
nama = "python"
versi = "1.0.0"

def hel():
#variabel lokal
    nama = "c#"
    varsi = "1.0.2"
#akses variabel lokal
    print("nama : %s" % nama)
    print("versi : %s" % varsi)
#akses variabel global
print("nama : %s" % nama)
print("versi : %s" % versi)

#memanggil fungsi help
hel()