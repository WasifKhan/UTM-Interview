<!-- .slide: data-state="title" -->

# Arrays and Hash Tables

---

## Topics
- Arrays
- Hash Tables
- Interview Problems

---

## Arrays
- Arrays in Memory
- Static vs Dynamic Arrays
- Matrices

---

## Arrays in Memory
- An **array** is a data structure that is stored in a contiguous block of computer memory
- A **memory address** is a location in computer memory, conventionally written in hexadecimal
- Every element in an array takes up the same amount of space

![](images/.png)
<!-- .element class="fragment" -->

---

## Arrays in Memory
- To calculate where an element in an array is stored, three things are required
- The memory address at which the array begins: `start`
- The size of each element in the array: `size`
- The index of the element: `index`
- The location in memory of any element is then: `start + size*index`
- This calculation is why indexing elements from zero is conventional
- The runtime of looking up an element in an array is O(1)

---

## Static vs Dynamic Arrays
- A **static array** is an array of a fixed size that can store a fixed number of elements
- Python tuples are implemented as immutable static arrays
- A **dynamic array** is an array that can scale its size up or down if needed
- Python lists are implemented as mutable dynamic arrays

---

## Static vs Dynamic Arrays
- When a dynamic array gets too full, it automatically allocates itself more memory
- First, the dynamic array requests a new, larger block of memory from the operating system
- Then, the dynamic array copies itself over to the new block of memory
- The old block of memory is released back to the operating system
- Program interactions with the operating system are called **system calls**
- System calls are beyond the scope of this course
- The important thing to understand is that resizing is an expensive operation
- The runtime of resizing a dynamic array is O(n)

---

## Matrices
- Python lists can store any value, from simple data types, to tuples, dictionaries or other lists
- How is this possible?
- For an array implementation to work, all elements in the array must have the same size
- Python data structures don't store their elements directly
- They store the memory address of each element, and find the element by the address
- Each memory address has the same size, so an array implementation works

---

## Matrices
- A **matrix** is a two dimensional version of an array
- A list of lists is often used to represent a matrix
- In order to correspond to a matrix, each internal list must be of the same length
- This list of lists:
```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
- Corresponds to this matrix:

![](images/.png)
<!-- .element class="fragment" -->

---

## Matrices
- To access an individual element in a matrix, two indices are needed instead of one
- Consider this matrix:
```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
- What element is at `matrix[0][1]`?
- What element is at `matrix[2][0]`?

---

## Hash Tables
- Hash Tables in Memory
- Hash Functions
- Collision Resolution

---

## Hash Tables in Memory
- A **hash table** is a data structure that maps **keys** to **values**
- Like an array, a hash table is stored in a contiguous block of memory
- Unlike an array, the memory allocated to a hash table often has empty gaps:
- In Python, dictionaries and sets are implemented with hash tables

![](images/.png)
<!-- .element class="fragment" -->

---

## Hash Functions
- A hash table uses the key to decide where in the allocated memory to store the value
- The function that maps keys to memory addresses is called a **hash function**
- A good hash function must be quick and easy to compute, to achieve quick lookup
- The runtime of looking up an element in a hash table is O(1)

---

## Hash Functions
- The modulus operator can provide a simple hash function for integers:
```
def hash_function(key):
    return key % 10
```
- Memory addressess are simplified as integers between 0-9
- This hash function is quick and easy to compute

---

## Hash Functions
- Using `hash_function`, store the following dictionary in memory:
```
dict = {
    34: "hash",
    56: "tables",
    99: "are",
    22: "fun"
}
```

![](images/.png)
<!-- .element class="fragment" -->

---

## Collision Resolution
- It's possible for two different keys to map to the same memory address
- This is called a **collision**
- There are two main strategies for resolving collisions
- **Chaining** stores all the values in the same location of the hash table
- For example, each location in the hash table could store a list of values
- **Open addressing** looks for a different slot in the allocated memory to store the value

---

## Collision Resolution
- Python uses a complex form of open addressing called **random probing**
- Python scales dictionaries in size when they get too full, similar to a dynamic array
- Fully understanding the implementation details of dictionaries is beyond the scope of this course
- However, a basic grasp of what's going on underneath the hood is important

---

## Interview Problems
- Find Duplicate Element
- Create Transpose of a Matrix
- Propagate Zeroes in a Matrix

---

## Find Duplicate Element
- <code class="code-info">Problem:</code> Implement the function `find_duplicate_element`
- `find_duplicate_element` takes in a Python list
- `find_duplicate_element` outputs the first duplicate element in the list
- `find_duplicate_element` outputs `None` if there are no duplicates

---

## Find Duplicate Element
- Keep track of seen elements in a dictionary:
```
def find_duplicate_element(lst):
    seen = set()
    for element in lst:
        if element in seen:
            return element
        else:
            seen.add(element)
    return None
```
- The seen element is used as a key for quick lookup
- The runtime of `find_duplicate_element` is O(n)

---

## Create Transpose of a Matrix
- <code class="code-info">Problem:</code> Implement the function `create_transpose`
- `create_transpose` takes in a Python list of lists representing a matrix
- `create_transpose` outputs a new matrix, representing the transpose of the original

---

## Create Transpose of a Matrix
- The original height becomes the new width, the original width becomes the new height:
```
def create_transpose(matrix):
    original_height = len(matrix)
    if not original_height:
        return []
    original_width = len(matrix[0])
    if not original_width:
        return []
    transpose = [None] * original_width
    for i in range(original_width):
        transpose[i] = [None] * original_height
    for i in range(original_width):
        for j in range(original_height):
            transpose[i][j] = matrix[j][i]
    return transpose
```
- Initialize transpose matrix filled with `None` representing no data
- Copy over values while transposing them
- The runtime of `create_transpose` is O(n\*m)

---

## Propagate Zeroes in a Matrix
- <code class="code-info">Problem:</code> Implement the function `propagate_zeros`
- `propagate_zeros` takes in a Python list of lists representing a matrix
- `propagate_zeros` modifies the matrix by propagating zeros
- Any row or column that originally contained a zero becomes all zeros
- `propagate_zeros` outputs the modified matrix

---

## Propagate Zeroes in a Matrix
- Remember which rows and columns need to be zeroed out in two dictionaries:
```
def propagate_zeros(matrix):
    height = len(matrix)
    if not height:
        return matrix
    width = len(matrix[0])
    if not width:
        return matrix
    zeroed_columns = set()
    zeroed_rows = set()
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 0:
                zeroed_columns.add(i)
                zeroed_rows.add(j)
```
- The runtime of `propagate_zeros` is O(n\*m)

---

<!-- .slide: data-state="title" -->

# End of 
# Arrays and Hash Tables

