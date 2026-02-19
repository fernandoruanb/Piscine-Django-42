## What the program does

* I define a dictionary `d` where:

  * **key** = musician name (string)
  * **value** = birth year (string like `"1942"`)

* The program **sorts the musicians**:

  1. **by year ascending** (oldest year first)
  2. **and if years are equal**, **by name alphabetically** (A → Z)

* Then it prints **only the musician names**, **one per line** (no year).

---

## Key concepts used

### 1) Dictionary (`dict`)

A dictionary stores **key → value** pairs:

* `"Hendrix" -> "1942"`

Here, the dictionary is used as a small “database” of names and years.

---

### 2) `d.items()`

`d.items()` produces an iterable of **tuples** like:

```python
("Hendrix", "1942")
("Allman", "1946")
...
```

So each `item` inside `sorted(...)` is a tuple:

* `item[0]` → name
* `item[1]` → year

---

### 3) `sorted(..., key=...)`

`sorted()` can sort any iterable.
The `key=` argument tells `sorted()` **what value to use as the sorting criterion**.

---

### 4) Composite sorting key: `(int(year), name)`

I used:

```python
key=lambda item: (int(item[1]), item[0])
```

This returns a **tuple** used for ordering:

* First element: `int(item[1])` → numeric year (so `"1911"` becomes `1911`)
* Second element: `item[0]` → name

Python sorts tuples **left to right**:

1. sort by year
2. if tied, sort by name

That’s exactly what the exercise asks for.

---

### 5) Why `int(item[1])` matters

Years are stored as strings (`"1944"`). Converting to `int` guarantees **numeric** sorting logic and avoids any weird edge cases.

---

### 6) `dict(sorted(...))` and insertion order

This line:

```python
ordered = dict(sorted(d.items(), key=...))
```

builds a **new dictionary** in the sorted order.

In modern Python (3.7+), dictionaries **preserve insertion order**, so iterating `ordered.items()` keeps the sorted order.

---

### 7) `if __name__ == '__main__':`

This block means:

* “Only run this code when the file is executed directly”
* If the file is imported by another script, this block won’t run

---

### 8) Printing only the names

I loop through the sorted dictionary:

```python
for key, value in ordered.items():
    print(f"{key}")
```

* `key` is the musician name
* you ignore `value` (the year) on purpose, because the output must show only the names

---

## Summary

This script reads a name→year dictionary, sorts entries by **(year, name)**, and prints **only the musician names** in the required order.

