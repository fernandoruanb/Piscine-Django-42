# Discover types in Python

That exercise is very simple, it is to make us know the different types of variables in Python. To solve it, we can create an array with different types of variables and use a for loop to print the value and its type.

# Explanation of `var.py`

This script defines a function that creates variables of different Python types and prints
both their values and their types to the standard output.

The goal is to show how Python automatically knows the type of each value, without manually
writing the type names in the code.

---

## 1. Function definition

```python
def my_var():
````

* This line defines a function named `my_var`.
* A function is a reusable block of code that runs only when it is called.
* All the code inside the function is indented.

---

## 2. Creating variables of different types

```python
vars = [
    42,
    "42",
    "quarante-deux",
    42.0,
    True,
    [42],
    {42: 42},
    (42,),
    set(),
]
```

This list contains **9 values**, each with a different type:

| Value             | Type    | Explanation                                |
| ----------------- | ------- | ------------------------------------------ |
| `42`              | `int`   | Integer number                             |
| `"42"`            | `str`   | String containing characters               |
| `"quarante-deux"` | `str`   | Another string                             |
| `42.0`            | `float` | Floating-point number                      |
| `True`            | `bool`  | Boolean value                              |
| `[42]`            | `list`  | List containing one element                |
| `{42: 42}`        | `dict`  | Dictionary (key-value pair)                |
| `(42,)`           | `tuple` | Tuple with one element (comma is required) |
| `set()`           | `set`   | Empty set                                  |

The variable name `vars` ends with an underscore to avoid conflict with Python’s built-in
function `vars()`.

---

## 3. Looping through the values

```python
for var in vars:
```

* This loop goes through each element in the list `vars`.
* On each iteration, the current value is stored in the variable `var`.

---

## 4. Printing the value and its type

```python
print(f"{var} has a type {type(var)}")
```

This line uses an **f-string**:

* The `f` before the string allows expressions inside `{}`.
* `{var}` inserts the current value.
* `{type(var)}` calls the built-in `type()` function, which returns the type of `var`.

Example:

```python
var = 42
type(var)
```

Returns:

```
<class 'int'>
```

This satisfies the requirement of the exercise because the type names (`int`, `str`, etc.)
are **not written explicitly** in the code.

---

## 5. Script entry point

```python
if __name__ == '__main__':
    my_var()
```

* This block checks whether the file is being run directly.
* If it is, the function `my_var()` is called.
* This prevents the function from running automatically if the file is imported
  as a module in another script.

---

## 6. Final behavior

When running:

```bash
python3 var.py
```

The script prints each value followed by its type
