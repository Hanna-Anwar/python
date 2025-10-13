s =input("enter a string :")  #hello

rev = " "

for ch in s: #h e
    
    rev = ch + rev  #rev=h+"", e +h

print(rev)


#Or

s =input("enter a string :")  

reverse_str = s[::-1]

print(reverse_str)
