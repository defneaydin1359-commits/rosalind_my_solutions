# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:49:03 2026

@author: Lenovo
"""
dosya_adi = "rosalind_dna.txt"

with open(dosya_adi, "r") as dosya:
    s = dosya.read().strip()
a=0
c=0
g=0
t=0
for i in s:
    if i=="A":
        a+=1
    elif i=="C":
        c+=1
    elif i=="G":
        g+=1
    elif i=="T":
        t+=1
print(a,c,g,t)
        
        