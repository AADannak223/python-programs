# Python Practice problem 8 (Easy, 10 points)
# Rohan Das Is A Fraud
# Rohan das is a fraud by nature.
# Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values (randomly generated) as wrong.
# Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!
# So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates Rohan’s multiplication table.
# Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.
# Note: Rohan’s function returns a list of numbers like this
# Rohan Das’s Function Input:
# rohanMultiplication(6)
# Rohan’s function returns this output:
# [6, 12, 18, 26, …., 60]
# You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it to the screen! If the table is correct, your function returns None.



import random

def wrong_table(num):
    wrong = random.randint(1, 9)
    table = [i * num for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 9)
    return table

def check_table(tab):
    table = [i * tab[0] for i in range(1, 11)]
    if table == tab:
        print("Rohan's table is correct")
        return tab
    else:
        print("Rohans table is wrong and the correct table is : ")
        return table

if __name__ == "__main__":

    no = int(input("Enter the no to make a table : "))
    tab = wrong_table(no)
    print(f"Rohan's table is : {tab}")
    print(check_table(tab))
