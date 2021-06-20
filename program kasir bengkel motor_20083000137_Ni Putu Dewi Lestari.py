ppn = 0.01
diskon = 0.05

merk = ['Duration SW20 1L','Castrol Magnetic 1L', 'Federal Spupreme XX 1L', 'Yamalube 1L', 'Shell 1L']
Harga = [53000,50000,54000,45000,46000]

print ("=============================================")
print(" BIAYA OLI MOTOR ")
print ("=============================================")
print(" Kode = 1. ", merk[0],"harga = Rp.",Harga[0])
print(" Kode = 2. ",merk[1],"harga = Rp.",Harga[1])
print(" Kode = 3. ",merk[2],"harga = Rp.",Harga[2])
print(" Kode = 4. ",merk[3],"harga = Rp.",Harga[3])
print(" Kode = 5. ",merk[4],"harga = Rp.",Harga[4])
print ("=============================================")

pilihan = int(input("masukkan pilihan  = "))
jumlah = int(input("masukkan jumlah pembelian = "))

idx = 0
while idx >=0 and idx < 5 :
        idx = idx + 1
        if (pilihan - 1) == idx :
            break 
        elif pilihan == 1 :
            idx = 0
            break

totalhargasblm = jumlah*Harga[idx]
totalppn = totalhargasblm*ppn
totalhrg = totalhargasblm + totalppn


if totalhargasblm >= 200000:
    totaldiskon = totalhrg * diskon
    totalakhir = totalhrg - totaldiskon
    print("mendapatkan diskon 5% dan dikenakan ppn 1%")
    print("Harga                       = Rp.", Harga[idx])
    print("Jumlah dibeli               = ", jumlah)
    print("total harga                 = Rp.",totalhargasblm)
    print("Total harga setelah ppn     = Rp.",totalhrg)
    print("total harga setelah diskon  = Rp.",totalakhir)
else:
    print("dikenakan ppn 1% dan tidak mendapatkan diskon 5%")
    print("Harga                       = Rp.", Harga[idx])
    print("Jumlah dibeli               = ", jumlah)
    print("total harga                 = Rp.", totalhargasblm)
    print("total harga setelah ppn     = Rp.",totalhrg)
    
