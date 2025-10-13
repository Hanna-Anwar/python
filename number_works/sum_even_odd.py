# Sum of even and odd numbers in a list

nums = [1, 2, 3, 4, 5, 6,10]

even_sum=0

odd_sum =0

for i in nums:

    if i%2==0:

        even_sum+=i

    else:

        odd_sum+=i


print(f"even sum = {even_sum}")

print(f"odd sum = {odd_sum}")