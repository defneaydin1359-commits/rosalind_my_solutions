with open("rosalind_gc.txt", "r") as dosya:
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
ratios={}
for key in g_codes:
    code=g_codes[key]
    gc_number=0
    for a in code:
        if a=="G" or a=="C":
            gc_number+=1
    ratios[key]= ((gc_number/ len(code))*100)
print(f"{max(ratios, key=ratios.get)}\n{round(max(ratios.values()),6)}")
#çok hoş bi kod oldu çok beğendim