# Python program to get the Fibonacci series between 0 to 50
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number in the Fibonacci is the sum total of the preceding two numbers before it.

num_1 = 0
num_2 = 1

for i in range(50):
    print(num_1)

    next_num = num_1 + num_2
    num_1 = num_2
    num_2 = next_num