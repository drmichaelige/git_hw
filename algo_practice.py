# importing mean()
from statistics import mean
# code here
# Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.

def find_first_two_lowest_elements(list2):
    if len(list2) < 2:
        return list2

    lowest = second_lowest = float('inf')

    for i in list2:
        if i < lowest:
            second_lowest = lowest
            lowest = i
        elif i < second_lowest:
            second_lowest = i

    return [lowest, second_lowest]

list2 = [9, 2, 3, 7, 5, 8, 1, 6, 4]
print(find_first_two_lowest_elements(list2))