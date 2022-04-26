girilen_deger = int(input("Hangi sayıya kadar ki asal sayıları arıyorsunuz? : "))
asal = []

for i in range(2, girilen_deger):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        asal.append(i)

print("\n0 - {} arasında toplam {} tane asal sayı vardır.".format(girilen_deger, len(asal)))
print("Bu sayılar: ")
print(asal)
