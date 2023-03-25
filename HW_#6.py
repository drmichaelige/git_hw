# importing mean()
from statistics import mean

# code here Homework #1
def Average(list1):
    return mean(list1)


def Elements_less_average(list1, average):
    # traverse in the list
    for x in list1:

        # compare with all the
        # values with value
        if average <= x:
            return False
    return True

list1 = [1, 3, 5, 6, 4, 10, 2, 3]
average = Average(list1)

number_below_average = [x for x in list1 if x < average]

# Printing average of the list
print("Average of the list =", round(average, 2))
print("Numbers below Average =", number_below_average)


# code here Homework #2

# Python prog to illustrate the following in a list
def find_len(list2):
	length = len(list2)
	list2.sort()

	print("Smallest element is:", list2[0])

	print("Second Smallest element is:", list2[1])

# Driver Code
list2=[198, 3, 4, 9, 10, 9, 2]
Largest = find_len(list2)
