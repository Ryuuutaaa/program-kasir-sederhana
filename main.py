menu = ["Ayam bakar", "Ayam goreng", "Sate", "Gule", "Gorengan", "Es teh", "Es jeruk", "Air mineral"]
harga = [20000, 18000, 13000, 12000, 2000, 5000, 5000, 3000]

print("Menu")
for i in range(len(menu)):
    print(f"{str(i+1)+'. '+menu[i]:<11}")
print("\nPilih menu, jika selesai tekan 0")
total = 0
pilih = 1
count = [0,0,0,0,0,0,0,0]
while (pilih!=0):
    pilih = int(input("Pilihan : "))
    if (pilih!=0):
        count[pilih-1] += 1
        total += harga [pilih-1]
print("\nAnda Pesan")
for i in range(len(menu)):
    if (count[i]!=0) :
      print(f"{str(count[i])+ ' '+ menu[i]:<11}: {str(count[i]*harga[i])}")
print(f"{'Total: ' :<11}{str(total)}")
    

