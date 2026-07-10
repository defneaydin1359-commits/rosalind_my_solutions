with open("rosalind_grph.txt", "r") as dosya:
    satirlar = [satir.strip() for satir in dosya.readlines() if satir.strip()]
# fasta kodu okuyan kısım
indexes=[]
for i in satirlar:
    if i.startswith(">"):
        indexes.append(satirlar.index(i))
g_codes={}
for i,j in zip(indexes,indexes[1:]):
    g_codes[satirlar[i][1:]]="".join(element.strip() for element in satirlar[i+1:j])
g_codes[satirlar[j][1:]]="".join(element.strip() for element in satirlar[j+1:])
# /*
nodes={}
for key1 in g_codes:
    for key2 in g_codes:
        if g_codes[key1]!=g_codes[key2] and g_codes[key1][0:3]==g_codes[key2][-3:]:
            print(key2,key1)