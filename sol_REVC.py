# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 17:40:18 2026

@author: Lenovo
"""
comp_dna=""
dosya_adi = "rosalind_revc.txt"

with open(dosya_adi, "r") as dosya:
    dna = dosya.read().strip()
for i in dna:
    if i=="A":
        b="T"
    elif i=="T":
        b="A"
    elif i=="G":
        b="C"
    elif i=="C":
        b="G"
    comp_dna= comp_dna + b
print(comp_dna[::-1])