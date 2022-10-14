# write a loop that prompts the uset to enter a series of pizza toppings untill they enter a "quit" value
# As they enter each topping , print a message saying that we will add that topping to that pizza

topp=[] #initialisation of an empty list
message =input("Please choose atleast one topping : ")# Get user input and store in variable

topp.append(message)# append the user input to the empty list
while message!='quit': #instantiate while loop by setting the condition of the topping as not equal to "Quit"
    message=input("Please add additional toppings  : ") #Request for additional toppings
    topp.append(message) # attatch the additional toppings to the message

    for i in topp: # intantiate for loop to display user what all toppings are selected to the items
        if message!='quit': # if user doesnt
            print(i.title()) # print selected toppings if the user wants to add more toppings

        else:
            break # if the user wants to quit
topp.remove("quit") # to remove quit from the list
print("Thank you for choosing the toppings", topp) # print the complete set of toppings











