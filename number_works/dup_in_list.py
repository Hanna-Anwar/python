# Find duplicates in a list

l = [1, 2, 3, 2, 4, 1, 5]

not_seen = []

dup =[]

for i in l:#1,2,3,2

    if i not in not_seen:#1,2,3

        not_seen.append(i)#[1,2,3]

    else:

        dup.append(i)

print(dup)



