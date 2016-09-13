
# while loop to control errors in input
while True:
    # ask user for number input
    number = input("Please enter a number. ")
    # if input is alphabet, keep asking for input
    if number.isalpha():
        continue
    # if input is a float, then keep asking for input
    if int(float(number)) != float(number):
        print("Please enter an integer, not a decimal!")
        continue
    
    # calculations
    remainder_4 = int(number) % 4
    remainder = int(number) % 2
    
    # if remainder is 4, then print different message. Break off from the while loop.
    if remainder_4 == 0:
        print(number + " is divisible by 4!")
        break
    # if remainder is 0, then print even number. Break off from the while loop.
    elif remainder == 0:
        print(number + " is an even number!")
        break
    else:
        # else print odd number. Break off from the while loop
        print(number + " is an odd number!")
        break
        

