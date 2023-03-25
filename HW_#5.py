# #
# # # code here Homework #1
# def split_in_half(s):
#     length = len(s)
#     half = length // 2
#     add = 0
#     if length % 2:
#         add = 1
#     left = s[:half + add]
#     right = s[half + add:]
#     return right + left
#
#
# test_split = "bbbbbcaaaaa"
# result_split = split_in_half(test_split)
# print(result_split)


# code here Homewoerk #2

def uni_char(s):
    chars = set()

    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)
            print(char)

    return True

def uni_char(s):
    return len(set(s)) == len(s)


test_pos = "abcde"
test_neg = "aabcde"

set_test_pos = set(test_pos)
set_test_neg = set(test_neg)
print(" pos string ")
print(test_pos)
print(" pos set")
print(set_test_pos)


print("\n\n neg string ")
print(test_neg)
print(" neg set")
print(set_test_neg)

result_pos = uni_char(test_pos)
print(result_pos)  # True
result_neg = uni_char(test_neg)
print(result_neg)  # False
