
# Reading a file in Python: explanation of the example

This example demonstrates two different ways to read a file in Python and print
numbers that are separated by commas and newlines.  
It also explains **why using `with` is the recommended approach**.

---

## Goal of the code

The file `numbers.txt` contains numbers like this:

```

1,2,3
4,5,6
7,8,9

```

The objective is to print **each number on its own line**, without commas:

```

1
2
3
4
5
6
7
8
9

````

---

## Example 1: Using `with` (recommended)

```python
with open("numbers.txt", "r") as file:
    for line in file:
        numbers = line.strip().split(",")
        for num in numbers:
            print(num)
````

### Step-by-step explanation

### 1. Opening the file with `with`

```python
with open("numbers.txt", "r") as file:
```

* `open("numbers.txt", "r")` opens the file in **read mode**.
* `with` creates a **context manager**.
* `as file` assigns the opened file object to the variable `file`.
* When the `with` block ends, Python **automatically closes the file descriptor**.

This guarantees that the file is always closed, even if an error happens while reading.

---

### 2. Iterating over the file line by line

```python
for line in file:
```

* Each iteration reads one line from the file.
* Example value of `line`:

  ```
  "1,2,3\n"
  ```

---

### 3. Cleaning and splitting the line

```python
numbers = line.strip().split(",")
```

* `strip()` removes leading and trailing whitespace characters such as `\n`.
* `split(",")` separates the string at each comma.

Example:

```python
"1,2,3\n".strip().split(",")
# Result: ["1", "2", "3"]
```

---

### 4. Printing each number on a new line

```python
for num in numbers:
    print(num)
```

* Loops through the list of numbers.
* Prints each number individually.

---

## Example 2: Without `with` (manual file handling)

```python
file = open("numbers.txt", "r")
try:
    for line in file:
        numbers = line.strip().split(",")
        for num in numbers:
            print(num)
finally:
    file.close()
```

### Why this is more dangerous

* `open()` opens a **file descriptor** at the operating system level.
* If an error happens before `file.close()` is called, the file may remain open.
* Leaving file descriptors open can cause resource leaks.

---

### Why `try / finally` is needed here

```python
try:
    ...
finally:
    file.close()
```

* `try` executes the file-reading logic.
* `finally` **always runs**, even if an exception occurs.
* This ensures the file is closed manually.

This structure is exactly what `with` does internally.

---

## Key concept summary

| Concept         | Explanation                                         |
| --------------- | --------------------------------------------------- |
| `open()`        | Opens a file and allocates a file descriptor        |
| `with`          | Automatically manages opening and closing resources |
| `strip()`       | Removes whitespace like `\n` from strings           |
| `split(",")`    | Splits a string into a list using commas            |
| File iteration  | Reads the file line by line efficiently             |
| `try / finally` | Manual way to guarantee file closure                |

---

## Final rule of thumb

> **Always use `with` when working with files in Python.**
> It is safer, cleaner, and prevents resource leaks without extra code.

```
```
