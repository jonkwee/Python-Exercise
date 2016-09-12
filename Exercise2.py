
while True:
    number = input("Please enter a number. ")
    if number.isalpha():
        continue
    if int(float(number)) != float(number):
        print("Please enter an integer, not a decimal!")
        continue

    remainder_4 = int(number) % 4
    remainder = int(number) % 2
    if remainder_4 == 0:
        print(number + " is divisible by 4!")
        break
    elif remainder == 0:
        print(number + " is an even number!")
        break
    else:
        print(number + " is an odd number!")
        break
        

