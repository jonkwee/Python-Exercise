from datetime import datetime

# control while loop variable
control = False

# use datetime module to get current year        
date = datetime.now()
currentyear = date.year

# ask for name
name = input("What is your name?: ")

# keep asking if year is not the right type of input I want.
while not control:
    year = input("What year were you born on?: ")
    if year.isalpha():
        print("Please enter a date!")
        continue
    if len(year) != 4:
        print("Please enter the year in this format, yyyy. ")
        continue
    if int(year) > int(currentyear):
        print("Are you from the future? I don't think so!")
        continue
    elif int(currentyear) - int(year) > 100:
        print("You are already over 100!")
        continue
    control = True

# keep asking if repeat is not the right number I want.
control = False
while not control:
    repeat = input("Please key a random number between 0-10: ")
    if repeat.isalpha():
        print("Please enter a number between 0-10!: ")
        continue
    if int(repeat) > 10 or int(repeat) < 0:
        print("Please enter a number between 0-10!: ")
        continue
    control = True

# calculate year to 100
yearto100 = int(currentyear) + (100 - (int(currentyear) - int(year)))

# print out the message 'repeat' amount of times
for num in range(int(repeat)):
    print(name + " ,you will be 100 in " + str(yearto100) + " !")
