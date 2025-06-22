def fact(n):
    if n <= 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result = result * i
        return result


print(fact(10))

