"""
Using the song “10 green bottles”, display the lines
“There are [num] green bottles hanging on the wall, [num] green bottles hanging on the wall, 
and if 1 green bottle should accidentally fall”. Then ask the question “how many green bottles will be hanging on the wall?”
If the user answers correctly, display the message “There will be [num] green bottles hanging on the wall”. 
If they answer incorrectly, display the message “No, try again” until they get it right.
 When the number of green bottles gets down to 0, display the message “There are no more green bottles hanging on the wall”.

"""



total_count = 10

while(total_count>0):

    print(f"There are {total_count} green bottles hanging on the wall,if 1 green bottle should accidentally fall")

    answer = int(input("how many green bottles will be hanging on the wall?"))

    if answer == total_count - 1:

        print(f"There will be {answer} green bottles hanging on the wall")
        
        total_count = total_count - 1

    else:
        
        print(f"try again")

print("no more bottles")


