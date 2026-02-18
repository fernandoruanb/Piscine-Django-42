## What you learned from this script

### 1) How to read a command-line argument

When you run:

```bash
python myProgram.py Oregon
```

Python stores the arguments in `sys.argv`:

* `sys.argv[0]` → the script name (`myProgram.py`)
* `sys.argv[1]` → the first argument (`"Oregon"`)

So this line:

```python
result = getCapitalCity(sys.argv[1])
```

passes the user’s input into your function.

---

### 2) Why `KeyError` happens with dictionaries

In Python, accessing a dictionary like this:

```python
states[capital]
```

means: “give me the value for this key **or crash if the key doesn’t exist**.”

If the key is missing, Python raises **`KeyError`**.

Your code can raise `KeyError` in two places:

```python
result = states[capital]          # if capital not in states
result = capital_cities[result]   # if code not in capital_cities
```

---

### 3) How `try/except` prevents the program from crashing

You used:

```python
try:
    ...
except KeyError:
    return None
```

This means:

* “Try to look up the keys”
* “If a key is missing, don’t crash — return `None` instead”

So `getCapitalCity()` becomes a **safe function**: it returns a capital city if found, otherwise it returns `None`.

---

### 4) How `if not result:` works in Python

In Python, `None` is considered **falsy**, so:

```python
if not result:
```

is true when `result` is `None` (or `""`, `0`, etc.).

That’s why this works:

```python
if not result:
    print("Unknow capital city")
else:
    print(result)
```

In your script:

* If the state is not found → `getCapitalCity()` returns `None` → prints `"Unknow capital city"`
* If found → prints the capital city.

---
