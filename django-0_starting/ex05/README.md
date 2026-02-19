## What this script does (high level)

* It receives **one command-line argument**: a comma-separated list of names.
* For each name, it checks if the text matches:

  * a **US state name** (like `"Oregon"`)
  * or a **capital city name** (like `"Denver"`)
* Then it prints one of these:

  * `"Denver is the capital of Colorado"` (if input is a capital)
  * `"Salem is the capital of Oregon"` (if input is a state)
  * or `"X is neither a capital city nor a state"` (if it matches none)

---

## Core data structures

### Dictionaries (`dict`)

We have two dictionaries:

* `states`: maps **State name → abbreviation**

  * `"Oregon" -> "OR"`
* `capital_cities`: maps **abbreviation → capital**

  * `"OR" -> "Salem"`

This is basically a two-step mapping:

State name → abbreviation → capital

and also the reverse direction:

Capital → abbreviation → state name

---

## Case-insensitive comparisons

We use `.lower()` to compare strings ignoring uppercase/lowercase:

```python
if value.lower() == data.lower():
```

So `"denver"`, `"DENVER"`, `"Denver"` all match the same.

---

## Guard clauses (`if not data: return None`)

Most functions start with:

```python
if not data:
    return None
```

Meaning:

* if `data` is `None`, `""`, or anything “empty”, stop early.

This prevents errors like calling `.lower()` on `None`.

---

## Iterating over dictionaries

We frequently do:

```python
for key, value in some_dict.items():
```

That means:

* loop over each **key/value pair** inside the dictionary.

This is how you search for a match when you don’t have direct access by key.

---

## “Lookup” helper functions (your building blocks)

My functions are small utilities for “finding something”:

### 1) Find abbreviation by capital name

`findSiglaCapital(data)`

* Input: `"Denver"`
* Output: `"CO"`

It loops through `capital_cities` and matches by **value**.

### 2) Find abbreviation by state name

`findSiglaState(data)`

* Input: `"Oregon"`
* Output: `"OR"`

It loops through `states` and matches by **key**.

### 3) Check if input is a capital

`isCapitalCity(data)`

* If input is a capital, it returns the **capital name** (same string stored in the dict).
* If not, returns `None`.

### 4) Check if input is a state

`isStateTarget(data)`

* If input is a state, returns the **official state name** (the key from dict).
* If not, returns `None`.

### 5) Convert abbreviation into capital

`findCapitalBySigla("OR") -> "Salem"`

### 6) Convert abbreviation into state

`findStateBySigla("OR") -> "Oregon"`

---

## Main decision logic (`isValid`)

`isValid(data)` does the “controller” work:

1. It checks:

   * `isCapital = isCapitalCity(data)`
   * `isState = isStateTarget(data)`

2. If it matches **a state**:

   * get abbreviation from state
   * get capital from abbreviation
   * print: `"Capital is the capital of State"`

3. Else if it matches **a capital**:

   * get abbreviation from capital
   * get state from abbreviation
   * print the same pattern

4. Else:

   * print: `"X is neither a capital city nor a state"`

Key concept here:

* Using `None` as “not found”
* Using `if (isCapital or isState)` as a simple validation gate

---

## Command-line input parsing

### `sys.argv`

* `sys.argv` is the list of command-line arguments.
* `sys.argv[0]` is the script name.
* `sys.argv[1]` is the first argument you pass.

I check:

```python
if len(sys.argv) < 2:
    sys.exit(0)
```

So the program exits quietly if no argument was provided.

---

## Splitting multiple inputs with commas

I do:

```python
listArgs = sys.argv[1].strip().split(",")
```

Meaning:

* remove spaces at the edges (`strip`)
* split by commas into a list

Example input:

```
"Oregon, Denver,  , Trenton"
```

Then you loop each item:

```python
for arg in listArgs:
    test = arg.strip()
    if not test:
        continue
    isValid(test)
```

Concepts used here:

* `strip()` cleans spaces before/after each item
* `if not test: continue` skips empty items (like `""`)

---

## Output formatting (f-strings)

I print using f-strings:

```python
print(f"{capital} is the capital of {isState}")
```

This is Python’s modern string interpolation.

---

