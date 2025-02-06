# Data Structures and Algorithms (DSA) in Python

Welcome to the **Data Structures and Algorithms (DSA) Repository**! This repository contains well-explained Python implementations of fundamental DSA concepts, along with code explanations, complexity analysis, and use cases.

[//]: # (## 📁 Repository Structure)

[//]: # (This repository is structured as follows:)

[//]: # (```)

[//]: # (DSA-Python/)

[//]: # (│-- README.md   # Documentation)

[//]: # (│-- DataStructures/)

[//]: # (│   ├── arrays.py)

[//]: # (│   ├── linked_list.py)

[//]: # (│   ├── stack.py)

[//]: # (│   ├── queue.py)

[//]: # (│   ├── hash_table.py)

[//]: # (│   ├── binary_tree.py)

[//]: # (│   ├── graph.py)

[//]: # (│-- Algorithms/)

[//]: # (│   ├── sorting/)

[//]: # (│   │   ├── bubble_sort.py)

[//]: # (│   │   ├── quick_sort.py)

[//]: # (│   │   ├── merge_sort.py)

[//]: # (│   ├── searching/)

[//]: # (│   │   ├── binary_search.py)

[//]: # (│   │   ├── linear_search.py)

[//]: # (│   ├── graph_algorithms/)

[//]: # (│   │   ├── dijkstra.py)

[//]: # (│   │   ├── bfs.py)

[//]: # (│   │   ├── dfs.py)

[//]: # (│-- Complexity_Analysis.md # Big O Notation Guide)

[//]: # (```)

---

## 🛠 Data Structures

### 1. Arrays
#### ✅ Explanation:
Arrays store elements of the same data type in contiguous memory locations.

#### 🔹 Python Implementation:
```python
class Array:
    def __init__(self, size):
        self.array = [None] * size  # Initializing array with None values
        self.size = size

    def insert(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of range")

    def display(self):
        return self.array
```
#### 🔹 Complexity:
- Access: **O(1)**
- Insert/Delete: **O(n)** (Shifting elements)

---

### 2. Linked List
#### ✅ Explanation:
A linked list consists of nodes where each node stores a value and a reference to the next node.

#### 🔹 Python Implementation:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
```
#### 🔹 Complexity:
- Access: **O(n)**
- Insert/Delete: **O(1)** at the beginning, **O(n)** at the end

---

### 3. Stacks
#### ✅ Explanation:
A stack follows **LIFO (Last In, First Out)** order. Operations occur only at one end.

#### 🔹 Python Implementation:
```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0
```
#### 🔹 Complexity:
- Push: **O(1)**
- Pop: **O(1)**

---

## 🚀 Algorithms

### 1. Searching Algorithms
#### ✅ Binary Search (O(log n))
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

### 2. Sorting Algorithms
#### ✅ Quick Sort (O(n log n))
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

---

### 3. Graph Algorithms
#### ✅ Depth First Search (DFS) (O(V + E))
```python
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
```

---

## 📊 Complexity Analysis
| Algorithm | Best Case | Average Case | Worst Case |
|-----------|-----------|-------------|------------|
| **Binary Search** | O(1) | O(log n) | O(log n) |
| **Bubble Sort** | O(n) | O(n²) | O(n²) |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) |
| **DFS/BFS** | O(V + E) | O(V + E) | O(V + E) |

---

[//]: # (## 📚 Resources)

[//]: # (- **CLRS - Introduction to Algorithms**)

[//]: # (- **Grokking Algorithms**)

[//]: # (- **Leetcode & GeeksforGeeks DSA Practice**)

[//]: # ()
[//]: # (## 💡 Contributions)

[//]: # (Contributions are welcome! If you find a bug or want to add improvements, feel free to open a pull request.)

---

## 🔗 Connect with Me
📧 Email: rupeshkumarthakur135@gmail.com  

[//]: # (🔗 LinkedIn: [Rupesh Kumar Thakur]&#40;https://www.linkedin.com/in/rupesh-kumar-thakur&#41;)

---

