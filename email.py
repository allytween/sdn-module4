"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""

# adding comments for Lab 4:
# creating an empty list named addresses
addresses = []

# prompting the user to affirm if they DO
# or do NOT have an email address to input
more = input("Do you have an email address to enter (y/n)? ")

# starting the while loop. The user had input
# a value into the variable 'more'. Now we're
# checking that value and checking it against
# several conditions
#--------------------------------------------
# sidebar: I would have personally used the
# '.lower()' method so I didn't have to worry about
# them typing a Y or N. To each their own.
#--------------------------------------------
while more == "y":
    # the user input that they DO have an email
    # address to input. Now we are asking for them
    # to enter that email, which will be stored
    # in the variable 'email'
    email = input("Enter the address: ")
    # the '.append' method will add the information
    # stored into variable 'email' on to the end of
    # the list 'addresses'
    addresses.append(email)
    # we are now asking the user if they have another
    # email address to input, and we will start the
    # while loop again to try the new input against
    # our conditions
    more = input("Do you have another address(y/n)? ")
    # this nested while loop is checking conditions for
    # when the user has entered anything BUT 'y'
    while more != "y":
        # if the user input 'n', we will break out of
        # the loop and move on to the next block of code
        if more == "n":
            break
        # if the user gave us any other input (garbage
        # input in our case), we will kindly ask them
        # again to choose either y or n, and the
        # main loop will start over again
        else:
            more = input("Please enter a y or n: ")

# this code will output the information stored in the
# 'addresses' list to the console
print(addresses)
