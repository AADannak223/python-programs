age = (input("Enter your age or year of birth : "))
length = len(age)
age = int(age)

if length == 4:
    if age < 1900:
        print("You seem to be oldest person alive, Please register your name in world record!!!")
        exit()

    elif age > 2021:
        print("You are not yet born")
        exit()

if length == 2:
    if age > 125:
        print("You seem to be oldest person alive, Please register your name in world record!!!")
        exit()

if length == 4:
    age1 = age + 100
    print(f"You will turn 100 years old in year {age1} ")

elif length == 2:
    age1 = 100 - age
    print(f"You will turn 100 years old in year {2021 + age1}")

else:
    print("There is some problem in your age or date of birth please check and try again")
    exit()

while True:
    year = input("If you want to check your age in the particular year enter year or enter No : ")
    print(age)

    if year == 'No' or year == 'no':
        exit()

    elif length == 4 and 'True' == str(year.isnumeric()):
        i_age = int(year) - age
        print(f"You will be {i_age} years old in year {year} ")
        break

    elif length == 2 and 'True' == str(year.isnumeric()):
        i_age = (int(year) - 2021) + age
        print(f"You will be {i_age} years old in year {year} ")
        break

    else:
        print("Please enter valid year")
