# You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. Your first input should be the number of test cases and then take all the cases as input from the user.
#
# Input:
# 3
#
# 451
#
# 10
#
# 2133
#
# Output:
# Next palindrome for 451 is 454
#
# Next palindrome for 10 is 11
#
# Next palindrome for 2311 is 2222

def check_p(num):
    original_num = num
    sum = 0
    while num > 0:
        d = num % 10
        num = num // 10
        sum = (sum * 10) + d

    return original_num == sum


def find_p(num):
    while True:
        num += 1
        if check_p(num):
            return num


no_of_input = int(input("Enter the number of input : "))
list1 = []

for i in range(no_of_input):
    list1.append(int(input("Enter the number : ")))

print(list1)
result = list(map(find_p, list1))
print(result)