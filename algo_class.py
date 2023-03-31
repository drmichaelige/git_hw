


# code here

a = 125 / 10
b = 125 // 10
print(a)
print (b)

# code here

def sum_of_three(n: int):
    result = 0
    original_n = n
    while n != 0:
        result = result + (n %10)
        n = n // 10

        print(f"Sum of all digits {n} is {result}")

# code here
a = 4 % 2
b = 5 % 2
print(a)
print(b)


# code here
def sum_numbers(n: int):
    final_sum = (n * (n +1))/2
    return final_sum


test_n = 5
result = sum_numbers(test_n)

print(result)

# Code here

my_list = [1, 6, 24, 7, 2,10,2, 5, 5, 7,]
print(my_list)

my_second_list = [ 9, 15]
print(my_list[2])
my_list.append(77) # to add 77 to my list
print(my_list)
#my_list.clear() # clear the list out
my_list.count(1) # to count  my list

total_ones = my_list.count(1)
total_twos = my_list.count(2)

#my_list.index() # to get index of a number in the list
# my_list.insert (1, 99) # to add to the first inedx the number 99
# my_list.pop() # to remove a number from the list
# index_to_pop = my_list.index(24) # to find the index of number 24
# my_list.remove() # to remove a specific element
# my_list.reverse()# to reverse the list
# my_list.sort() # to sort the list

print(my_list)
print(total_twos)


my_list.index(10)
index_ten = my_list.index(10)
print(index_ten)

my_list.insert(1, 99)
print(my_list)

# to remove from the list using def function

def remove_item_from_list(my_list, value):
    for i in range(len(my_list)-1):
        if my_list[i] == value:
            my_list.pop(i)
        print(my_list)
        remove_item_from_list(my_list, 77)
        print(my_list)

# new code find missing number

def find_missing_number(arr1, arr2):
    arr1.sort()
    arr2.sort()
    # 1,2,3, 4
    #1,2,3
    for i in range(len(arr2) -1):
        if arr1[i] != arr2[i]:
            return arr1[i]
    return arr1[-i]

test_arr1 = [2, 3, 1, 4]
test_arr2 = [4, 1, 3]
result = find_missing_number(test_arr1, test_arr2)
print(result)


# # method 2
#
# for num1, num2 in zip(arr1, arr2):
#
#     if num1 != num2:
#         return num1
#     return arr1[-1]
