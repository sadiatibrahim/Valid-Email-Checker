# Names: Sadiat Ibrahim, Jennifer Jung
# Date: 2/25/21
# Course Number and Section: CSC 330 002
# Quarter: Winter
# Project #: 3

# We worked on the code together.

# Import re module
import re

# The first character must be a letter, then followed by 0 or more letters/numbers then @ symbol. 
# After that it is followed by one or more letters/numbers then a period. Finally it will end on one or more letters/numbers.
regex = '^[a-z|A-Z][a-z|A-Z|0-9]*[@][a-z|A-Z|0-9]+[.][a-z|A-Z|0-9]+$'

# function that checks if it follows the regex, and prints message accordingly. 
def Search(email):
    check = re.search(regex, email)
    if check :
        print("That is a valid email address!")
    else:
        print("That is NOT a valid email address!")


# Main program that takes in the user's input, if the input is a string, it calls the Search function which is a helper function to check if the input is a valid email.
# It will keep asking for strings until a token is recieved to stop the program, which is q.
while(True):
    user_input = input("Input a string or 'q' to quit: ")
    if user_input == 'q':
        print("Have a nice day!")
        break
    else:
        Search(user_input)
                      
