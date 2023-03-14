


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

test = 125

sum_of_three(test)