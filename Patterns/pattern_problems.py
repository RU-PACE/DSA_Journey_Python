"""
Approach for pattern problems:

There are 4 general rules for solving a pattern-based question:

1) We always use nested loops for printing the patterns. For the outer loop, we count the number of lines/rows and loop for them.
2) Next, for the inner loop, we focus on the number of columns and somehow connect them to the rows by forming a logic such that for each row we get the required number of columns to be printed.
3) We print the ‘*’ inside the inner loop.
4) Observe symmetry in the pattern or check if a pattern is a combination of two or more similar patterns.
"""


"""
*****
*****
*****
*****
*****
"""


def pattern_1(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()


pattern_1(5)


"""
*
**
***
****
*****
"""


def pattern_2(n):
    for i in range(n):
        for j in range(i):
            print("*", end="")
        print()


pattern_2(6)


"""
1
12
123
1234
12345
"""


def pattern_3(n):
    for i in range(1, n+1):
        for j in range(1, i):
            print(j, end="")
        print()


pattern_3(6)


"""
1
22
333
4444
55555
"""


def pattern_4(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end="")
        print()


pattern_4(5)


"""
*****
****
***
**
*
"""


def pattern_5(n):
    for i in range(1, n):
        for j in range(n-i):
            print("*", end="")
        print()


pattern_5(6)


"""
1234
123
12
1
"""

def pattern_6(n):
    for i in range(1, n):
        for j in range(1, n-i):
            print(j, end="")
        print()


pattern_6(6)

