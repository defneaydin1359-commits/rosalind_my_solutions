file = "rosalind_subs.txt"
with open(file, "r") as dosya:
    satirlar = [satir.strip() for satir in dosya.readlines() if satir.strip()]
main = satirlar[0]
subs= satirlar[1]
indexes=[]
for i in range(len(main)-len(subs)+1):
    if main[i:len(subs)+i]==subs:
        indexes.append(i+1)
print(" ".join(map(str, indexes)))