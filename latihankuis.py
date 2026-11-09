a = ["apel","belimbing","ceri","durian"]
print(type(a))

b = ("January","Februari","Maret","April","Mei")
print(type(b))

buah = ["apel","jeruk","ceri","durian","apel"]
print(len(buah))
print(buah[2])
print(buah[1:4])

buah.append("sirsak")
print(buah)

buah[2] = "manggis"
print (buah)

buah.insert(3,"semangka")
print(buah)