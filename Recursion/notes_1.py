# def fun():
#     print("HELLO_1")
#     fun()
#     print("HELLO_2")
#
#
# # Uncomment the line below to test the function
# fun()  # This will cause a RecursionError due to infinite recursion

def fun(n, depth=0):
    indent = "  " * depth
    print(f"{indent}→ enter fact({n})")
    if n <= 0:
        return 0  # Base case to stop recursion
    else :
        result = n + fun(n - 1, depth + 1)
        print(f"{indent}← exit fact({n}) with result {result}")
        return result

    print("HELLO_1")
    fun(n-1)
    print("HELLO_2")


# Uncomment the line below to test the function
fun(3)  # This will cause a RecursionError due to infinite recursion


# When a recursive function calls itself, each call is added to the call stack. "Recursion unwinds" refers to the process where, after reaching the base case, the function calls start returning one by one in reverse order (from the deepest call back to the first). During unwinding, any code after the recursive call is executed for each level as the stack unwinds. This is why you see outputs like `HELLO_2` after the recursive call, once the base case is reached and the function returns back up the stack.