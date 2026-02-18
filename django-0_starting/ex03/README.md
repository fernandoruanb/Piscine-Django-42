## What we learned from this code

### 1) How to structure data with dictionaries

You created two dictionaries that represent a **two-step mapping**:

* `states`: **State name → State code**

  ```python
  states["Oregon"] == "OR"
  ```

* `capital_cities`: **State code → Capital city**

  ```python
  capital_cities["OR"] == "Salem"
  ```

This is a common pattern: use one dictionary to translate input into an intermediate key (code), then use the code to look up the final value.

---

### 2) How the function performs a chained lookup

Your function:

```python
def getCapitalByState(state):
    result = states[state]
    result = capital_cities[result]
    return result
```

Step-by-step:

1. Convert `"Oregon"` into `"OR"` using `states[state]`
2. Convert `"OR"` into `"Salem"` using `capital_cities[result]`
3. Return `"Salem"`

So `getCapitalByState("Oregon")` returns `"Salem"`.

---

### 3) Why `try/except KeyError` is the right error handling here

When you access a dictionary like this:

```python
states[state]
```

Python will raise a **`KeyError`** if the key doesn’t exist.

You correctly handle that by doing:

```python
except KeyError:
    return None
```

That prevents your program from crashing and lets you decide what to print in `main`.

---

### 4) How command-line arguments work (`sys.argv`)

This code:

```python
result = getCapitalByState(sys.argv[1])
```

means:

* The user runs: `python myProgram.py Oregon`
* `sys.argv[1]` becomes `"Oregon"`
* That value is passed to `getCapitalByState`

You also check:

```python
if len(sys.argv) < 2:
    sys.exit(0)
```

which avoids an “index out of range” error when the user forgets to pass an argument.

---

### 5) How `if not result:` decides what to print

Since your function returns:

* a **string** like `"Salem"` when it succeeds
* `None` when it fails

This works:

```python
if not result:
    print("Unknow state")
else:
    print(result)
```

Because `None` is **falsy** in Python, so the program prints the error message when the lookup fails.

---