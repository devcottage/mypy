import os, sys

dw = {0:0}

for word in sys.stdin:
    wlen = int(len(word))

    if not wlen in dw.keys():
        dw[wlen] = 0

    dw[wlen] = int(dw[wlen]) + 1

for key in dw.keys(): 
    print(f"{key} : {dw[key]}")

