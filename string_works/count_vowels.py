# Count vowels in a string

string = input("enter a string: ").lower()

vowels="aeiou"

v_count =0

for ch in string:

    if ch in vowels:

        v_count+=1

print(f"vowel count is {v_count}")