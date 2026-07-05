codons={
    'F': ['UUU', 'UUC'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'Y': ['UAU', 'UAC'],
    '*': ['UAA', 'UAG', 'UGA'],
    'C': ['UGU', 'UGC'],
    'W': ['UGG'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'H': ['CAU', 'CAC'],
    'Q': ['CAA', 'CAG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'I': ['AUU', 'AUC', 'AUA'],
    'M': ['AUG'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'N': ['AAU', 'AAC'],
    'K': ['AAA', 'AAG'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'D': ['GAU', 'GAC'],
    'E': ['GAA', 'GAG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG']
}
dosya_adi = "rosalind_mrna.txt"
with open(dosya_adi, "r") as dosya:
   mrna = dosya.read().strip()
alternatives=1
for i in mrna:
    alternatives=alternatives * len(codons[i])
alternatives= alternatives * len(codons["*"])
print(alternatives %1000000)
    
