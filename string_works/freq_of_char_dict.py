string = "goodmorning"

wc = {}

for ch in string:

    if ch in wc:

        wc[ch]+=1

    else:

        wc[ch]=1

print(f"frequency of each character is {wc}")