# importing mean()
from statistics import mean

# code here Homework #1
def reorder_even_first(list1):
    odd, even = 0, len(list1)-1
    while odd < even:
        if list1[odd] % 2 == 0:
            odd += 1
        elif list1[even] % 2 == 1:
            even -= 1
        else:
            list1[odd], list1[even] = list1[even], list1[odd]
            odd += 1
            even -= 1
    return list1

list1 = ([7, 3, 5, 6, 4, 10, 3, 2])

print(reorder_even_first(list1))

# Code here Homework6_#2

def increment_number(digits):
    carry = 1
    for i in range(len(digits)-1, -1, -1):
        digits[i] += carry
        if digits[i] == 10:
            digits[i] = 0
            carry = 1
        else:
            carry = 0
            break
    if carry == 1:
        digits.insert(0, 1)
    return digits

digits = [1, 2, 9]
result = increment_number(digits)
print(result)  # Output: [1, 3, 0]
