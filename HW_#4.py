
# code here Homework #1
def sum_numbers(n: int):
    final_sum = (n * (n +1))/2
    return final_sum


test_n = 5
result = sum_numbers(test_n)

print(result)

#code here Homework #2

def max_number(n:int):

    max = list[0]
    for x in list:
        if x >= max:
            max = x
    return max

list = [124, 21, 32]
print(max(list))


#code here Homework #3

def count_odd_even(n):
    odds = 0
    evens = 0

    while n != 0:
        current_digit = n % 10
        if current_digit % 2:
            odds += 1
        else:
            evens += 1
        n = n // 10

        print(f"Odd digits: {odds}")
        print(f"Even digits: {evens}")

test_n = 34560
count_odd_even(test_n)
