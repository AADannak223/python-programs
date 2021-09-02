# Health management systen
# # clients - omkar, rohit and raj
# Total 6 files
# write a fuction that whan executed takes as input clients names
# def getdata();
#     iport datetime
#     return datetime.datetime.now()
#one more funtion to retrieve exercise or food for any client
import datetime

def gettime():
    import datetime
    return datetime.datetime.now()
def choice(ch):
    if ch == 1:
        c = int(input("Enter 1 for exercise and 2 for diet"))
        if (c==1):
            value = input("Type here about your exercies : ")
            with open("Omkar_exe.txt","a") as p:
                p.write( str([str(gettime())]) + ": "+ value +"\n")
            print("Successfully Written ")
        elif(c==2):
            value = input("Type here about your diet : ")
            with open("Omkar_diet.txt", "a") as p:
                p.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written")
    elif ch==2:
        c = int(input("Enter 1 for exercise and 2 for diet"))
        if (c == 1):
            value = input("Type here about your exercies : ")
            with open("Rohit_exe.txt", "a") as p:
                p.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written ")
        elif (c == 2):
            value = input("Type here about your diet : ")
            with open("Rohit_diet.txt", "a") as p:
                p.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written ")
    elif (ch == 3):
        c = int(input("Enter 1 for exercise and 2 for diet"))
        if (c == 1):
            value = input("Type here about your exercies : ")
            with open("Raj_exe.txt", "a") as p:
                p.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written ")
        elif (c == 2):
            value = input("Type here about your diet : ")
            with open("Raj_diet.txt", "a") as p:
                p.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written ")

    else:
        print("please enter valid input 1. Omkar, 2. Rohit, 3. Raj")

def retrive(choic):
    if (choic == 1):
        c = int(input("Enter 1 for exercise and 2 for diet"))
        if (c == 1):
            with open("Omkar_exe.txt") as p:
                for i in p:
                    print(i,end="")
        elif (c == 2):
            with open("Omkar_diet.txt") as p:
                for i in p:
                    print(i,end="")

    if (choic == 2):
        c = int(input("Enter 1 for exercise and 2 for diet"))
        if (c == 1):
            with open("Rohit_exe.txt") as p:
                for i in p:
                    print(i,end="")
        elif (c == 2):
            with open("Rohit_diet.txt") as p:
                for i in p:
                    print(i,end="")

    if (choic == 3):
        c = int(input("Enter 1 for exercise and 2 for diet"))
        if (c == 1):
            with open("Raj_exe.txt") as p:
                for i in p:
                    print(i,end="")
        elif (c == 2):
            with open("Raj_diet.txt") as p:
                for i in p:
                    print(i,end="")

    else:
        print("please enter valid input 1. Omkar, 2. Rohit, 3. Raj")

print("***HEALTH MANAGEMENT SYSTEM***")
a = int(input("press 1 for save data and 2 for retrive data"))

if a==1:
    b = int(input("Press 1.Omkar, 2.Rohit, 3.Raj"))
    choice(b)
else:
    b = int(input("Press 1.Omkar, 2.Rohit, 3.Raj"))
    retrive(b)

