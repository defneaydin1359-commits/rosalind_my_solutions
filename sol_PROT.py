
dosya_adi = "rosalind_prot.txt"

with open(dosya_adi, "r") as dosya:
    genetic_s = dosya.read().strip()
#start_index= genetic_s.find("AUG")+3
start_index=0
codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',  # UAA ve UAG Stop kodonları
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',  # UGA Stop kodonu, UGG Trp (W)

    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',

    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',  # AUG Start / Met (M) kodonu
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',

    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

#stop_index= min(genetic_s.find("UAG",start_index,),genetic_s.find("UAA",start_index,),genetic_s.find("UGA",start_index,))
protein=""
for i in range(start_index,len(genetic_s)-2,3):
    cur_codon= genetic_s[i:i+3]
    if codon_table[cur_codon]!="*":
        protein= protein + codon_table[cur_codon]
print(protein)
    
    
