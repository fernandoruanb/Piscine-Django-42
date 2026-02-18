## What this program does

You run the script passing a **capital city** as an argument, and it prints the **state name** that matches that capital.

Example:

```bash
python myProgram.py Denver
```

Output:

```
Colorado
```

---

## Data structures (your “database”)

### `states` dictionary

Maps **State name → State code**:

* `"Colorado" -> "CO"`

### `capital_cities` dictionary

Maps **State code → Capital city**:

* `"CO" -> "Denver"`

So your “chain” is:

**State name → code → capital city**

But your program needs the reverse direction:

**capital city → code → state name**

---

## Function-by-function explanation

### 1) `findTheKeyByValue(value)`

```python
def findTheKeyByValue(value):
    for key, target in capital_cities.items():
        if (value == target):
            return key
    return None
```

Goal: given a **capital city** (like `"Denver"`), find its **state code** (like `"CO"`).

How it works:

* Loops over `(key, value)` pairs of `capital_cities`
* Compares the input `value` with `target` (the dict’s value)
* Returns the corresponding `key` (the code)

If nothing matches, returns `None`.

So:

* `findTheKeyByValue("Denver")` → `"CO"`

---

### 2) `findTheStateByCapital(capital)`

```python
def findTheStateByCapital(capital):
    for key, target in states.items():
        if (target == capital):
            return key
    return None
```

Goal: given a **state code** (like `"CO"`), find the **state name** (like `"Colorado"`).

How it works:

* Loops over `(state_name, state_code)` in `states`
* If the code matches, returns the name

So:

* `findTheStateByCapital("CO")` → `"Colorado"`

---

### 3) `getCapitalByState(capital)`

```python
def getCapitalByState(capital):
    result = findTheKeyByValue(capital)
    result = findTheStateByCapital(result)
    return result
```

Despite the name, this function is actually doing:

**getStateByCapital(capital)**

Step-by-step:

1. Convert capital city → state code
   `result = findTheKeyByValue(capital)`
2. Convert state code → state name
   `result = findTheStateByCapital(result)`
3. Return the state name

Example:

* Input: `"Denver"`
* Step 1 returns `"CO"`
* Step 2 returns `"Colorado"`
* Final output: `"Colorado"`

If step 1 fails, it returns `None`, and step 2 will also return `None`.

---

## Main execution (command-line handling)

```python
if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(0)
```

* Ensures the user provided an argument (`sys.argv[1]`)
* Exits cleanly if not

Then:

```python
result = getCapitalByState(sys.argv[1])
```

Finally:

```python
if not result:
    print("Unknow capital city")
else:
    print(result)
```

* If `result` is `None` → prints the error message
* Otherwise prints the state name

---
