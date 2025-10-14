# Count frequency of elements

l = [1, 2, 2, 3, 3, 3]

n_count = {}

for n in l :

    if n in n_count:

        n_count[n]+=1

    else:

        n_count[n]=1

print(n_count)


