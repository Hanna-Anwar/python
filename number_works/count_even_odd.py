
arr = [1,2,4,3,6,8,7,5,12,13,0]

even_count = 0

# even_count = []

odd_count = 0

# odd_count = []

for i in arr:

    if i % 2 ==0:

      even_count+=1

    else:
       
       odd_count+=1

print(f"{even_count} even count")
print(f"{odd_count} odd count")


