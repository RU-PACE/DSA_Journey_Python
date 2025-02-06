# Big O Notation in Python: Time and Space Complexity

This repository explores Big O notation and its practical implications in Python programming. Big O notation is a way to express the long-term growth rate of a function, typically the time or space required by an algorithm as the input size grows. It doesn't measure the *exact* time or space, but rather how these resources scale with increasing input.

## Table of Contents

- [Introduction to Big O Notation](#introduction-to-big-o-notation)
- [Common Big O Notations](#common-big-o-notations)
- [Time Complexity](#time-complexity)
- [Space Complexity](#space-complexity)
- [Python Examples for Time Complexity](#Python-Examples-for-Time-Complexity)
- [Python Examples for Space Complexity](#Python-Examples-for-Space-Complexity)
- [Conclusion](#conclusion)
- [Big O Notation Graph](https://www.bigocheatsheet.com/) 

## Introduction to Big O Notation

Big O notation uses a special notation to describe the limiting behavior of a function. It focuses on the dominant part of the function that grows the fastest as the input size (often denoted as 'n') approaches infinity. We ignore constant factors and smaller terms.


## Common Big O Notations

Here's a list of common Big O notations, ordered from fastest to slowest growth:

| Notation | Name           | Description                                     | Example                               |
|----------|----------------|-------------------------------------------------|---------------------------------------|
| O(1)     | Constant       | Execution time/space is constant.                 | Accessing an element in a list by index. |
| O(log log n) | Log-logarithmic | Extremely slow growth.                             | Some specialized algorithms.          |
| O(log n) | Logarithmic     | Grows logarithmically.                            | Binary search.                         |
| O(n^(1/3)) | Cube root      | Growth rate between logarithmic and linear.        | Some number theory algorithms.        |
| O(n^(1/2)) | Square root     | Growth rate between logarithmic and linear.        | Operations on perfect square numbers.   |
| O(n)     | Linear         | Grows linearly with input size.                   | Traversing a list.                     |
| O(n log n)| Linearithmic   | Grows linearly multiplied by a logarithmic factor. | Merge sort.                            |
| O(n^2)   | Quadratic      | Grows quadratically.                              | Nested loops.                          |
| O(n^2 log n)| Quadratic-logarithmic | Grows quadratically multiplied by a logarithmic factor. | Some sorting algorithms in specific scenarios. |
| O(n^3)   | Cubic          | Grows cubically.                                  | Matrix multiplication.                 |
| O(n^4)   | Quartic        | Grows to the power of 4.                          | Some complex algorithms.               |
| O(2^n)   | Exponential    | Grows exponentially.                              | Recursive Fibonacci (naive approach).   |
| O(n!)     | Factorial      | Grows factorially (extremely slow).                 | Permutations.                          |
| O(n^n)   | n to the power of n | Extremely slow growth.                             | Some complex combinatorial problems. |

## Time Complexity

Time complexity refers to how the *execution time* of an algorithm scales with the input size.

## Space Complexity

Space complexity refers to how much *memory* an algorithm requires as the input size grows. This includes the space used for input data, variables, and auxiliary data structures.

---

## Python Examples for Time Complexity

### 1. **O(1) - Constant Time**
- **Description**: Execution time remains constant regardless of input size.
- **Python Example**:
  ```python
  def get_first_element(arr):
      return arr[0]  # Single operation
  ```
- **Graph**: Flat line on the time vs. input size plot.

### 2. **O(log log n) - Log-Logarithmic**
- **Description**: Grows slowly, seen in optimized algorithms.
- **Python Example**:
  ```python
  def log_log_n(n):
      i = n
      while i > 1:
          i = int(i ** 0.5)  # Reduces input size exponentially
  ```
- **Graph**: Slightly increasing curve.

### 3. **O(log n) - Logarithmic**
- **Description**: Common in divide-and-conquer algorithms (e.g., binary search).
- **Python Example**:
  ```python
  def binary_search(arr, target):
      left, right = 0, len(arr)-1
      while left <= right:
          mid = (left + right) // 2
          if arr[mid] == target:
              return mid
          elif arr[mid] < target:
              left = mid + 1
          else:
              right = mid - 1
  ```
- **Graph**: Gentle upward slope.

### 4. **O(n^(1/3)) - Cube Root**
- **Description**: Rare, seen in specialized mathematical algorithms.
- **Python Example**:
  ```python
  def cube_root_loop(n):
      for i in range(int(n ** (1/3))):
          print(i)  # Runs ∛n times
  ```
- **Graph**: Curves upward slower than linear.

### 5. **O(√n) - Square Root**
- **Description**: Appears in prime checks or brute-force factorization.
- **Python Example**:
  ```python
  def is_prime(n):
      if n <= 1:
          return False
      for i in range(2, int(n ** 0.5) + 1):
          if n % i == 0:
              return False
      return True
  ```
- **Graph**: Similar to cube root but steeper.

### 6. **O(n) - Linear**
- **Description**: Time grows proportionally with input size.
- **Python Example**:
  ```python
  def linear_search(arr, target):
      for num in arr:  # Iterates n times
          if num == target:
              return True
      return False
  ```
- **Graph**: Straight diagonal line.

### 7. **O(n log n) - Linearithmic**
- **Description**: Efficient sorting algorithms (e.g., merge sort).
- **Python Example**:
  ```python
  def merge_sort(arr):
      if len(arr) > 1:
          mid = len(arr) // 2
          L = arr[:mid]
          R = arr[mid:]
          merge_sort(L)
          merge_sort(R)
          # Merging two sorted arrays (O(n) per merge)
          i = j = k = 0
          while i < len(L) and j < len(R):
              if L[i] < R[j]:
                  arr[k] = L[i]
                  i += 1
              else:
                  arr[k] = R[j]
                  j += 1
              k += 1
          while i < len(L):
              arr[k] = L[i]
              i += 1
              k += 1
          while j < len(R):
              arr[k] = R[j]
              j += 1
              k += 1
  ```
- **Graph**: Curved line between O(n) and O(n²).

### 8. **O(n²) - Quadratic**
- **Description**: Nested loops (e.g., bubble sort).
- **Python Example**:
  ```python
  def bubble_sort(arr):
      for i in range(len(arr)):
          for j in range(len(arr)-1):
              if arr[j] > arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]
  ```
- **Graph**: Steep parabolic curve.



### 9. **O(n² log n)**
- **Description**: Slower than quadratic, seen in some sorting algorithms.
- **Python Example**:
  ```python
  def quadratic_log_n(n):
      for i in range(n):  # O(n)
          for j in range(n):  # O(n)
              # O(log n) operation inside nested loops
              k = 1
              while k < n:
                  k *= 2
  ```
- **Graph**: Between O(n²) and O(n³).

### 10. **O(n³) - Cubic**
- **Description**: Triple nested loops (e.g., matrix multiplication).
- **Python Example**:
  ```python
  def cubic_example(matrix):
      n = len(matrix)
      result = [[0]*n for _ in range(n)]
      for i in range(n):          # O(n)
          for j in range(n):      # O(n)
              for k in range(n):  # O(n)
                  result[i][j] += matrix[i][k] * matrix[k][j]
  ```
- **Graph**: Sharper rise than O(n²).

### 11. **O(n⁴)**
- **Description**: Rare, often indicates highly inefficient code.
- **Python Example**:
  ```python
  def quartic_example(n):
      count = 0
      for a in range(n):          # O(n)
          for b in range(n):      # O(n)
              for c in range(n):  # O(n)
                  for d in range(n):  # O(n)
                      count += 1
  ```
- **Graph**: Extremely steep curve.

### 12. **O(2ⁿ) - Exponential**
- **Description**: Recursive algorithms without memoization (e.g., Fibonacci).
- **Python Example**:
  ```python
  def fibonacci(n):
      if n <= 1:
          return n
      return fibonacci(n-1) + fibonacci(n-2)  # Branches exponentially
  ```
- **Graph**: Near-vertical line as n increases.

### 13. **O(nⁿ)**
- **Description**: Extremely inefficient (e.g., all permutations of a set).
- **Python Example**:
  ```python
  def n_power_n(n):
      for i in range(n ** n):  # Runs nⁿ times
          print(i)
  ```
- **Graph**: Fastest-growing curve on the plot.

---

## Python Examples for Space Complexity

### Common Space Complexities:
- **O(1)**: Fixed memory (e.g., variables).
  ```python
  def constant_space(n):
      total = 0  # Single variable
      for i in range(n):
          total += i
      return total
  ```
- **O(n)**: Linear memory (e.g., arrays).
  ```python
  def linear_space(n):
      arr = [0] * n  # Array of size n
      return arr
  ```
- **O(n²)**: Quadratic memory (e.g., 2D matrices).
  ```python
  def quadratic_space(n):
      matrix = [[0]*n for _ in range(n)]  # n x n matrix
      return matrix
  ```

## Graph Interpretation
- **X-axis**: Input size (n)
- **Y-axis**: Time/Memory usage
- **Key Takeaway**: Aim for lower complexities (left side of the graph) for scalable code.


## Conclusion
Understanding Big O helps optimize algorithms. Always analyze both time and space complexity when solving problems in Python.

---