## What the program does (big picture)

Your script has a pipeline with **3 steps**:

1. **Read the file** line-by-line and store each cleaned line into a list (`myPeriodicTable`).
2. **Convert each line** into a dictionary entry (`myJson`) where:

   * key = element name (left side of `=`)
   * value = raw fields string (right side of `=`)
3. **Parse the raw fields** and generate an **HTML file** (`periodic_table.html`) containing one block per element.

---

## Step 1 — Reading the file into a list (`getTheList`)

```python
def getTheList():
    with open("periodic_table.txt", "r") as periodicTable:
        for line in periodicTable:
            myPeriodicTable.append(line.strip())
```

**Concepts:**

* `with open(...)` ensures the file is closed automatically.
* `for line in periodicTable` iterates **one line at a time**.
* `strip()` removes `\n` and surrounding spaces.
* You end up with a list of lines like:

```
[
  "Hydrogen = position:0, number:1, small: H, molar:1.00794, electron:1 None ...",
  ...
]
```

---

## Step 2 — Building a dict from those lines (`getTheJson`)

```python
def getTheJson(data):
    for line in myPeriodicTable:
        element = line.split("=", 1)[0].strip()
        myJsonUnit = line.split("=", 1)[1].strip()
        myJson[element] = myJsonUnit
```

**Concepts:**

* Each line is split into two parts at the **first** `=`:

  * left: element name (e.g. `"Hydrogen"`)
  * right: everything after `=` (the fields chunk)
* So `myJson` becomes something like:

```python
{
  "Hydrogen": "position:0, number:1, small: H, molar:1.00794, electron:1 None...",
  "$Helium":   "position:1, number:2, small: He, molar:4.002602, electron:2 None...",
  ...
}
```
---

## Step 3 — Parsing the “chunk” and generating HTML (`mountHTML`)

### The key concept: parsing the right-side chunk

For each element, `value` is a **raw string** like:

```
"position:0, number:1, small: H, molar:1.00794, electron:1 None None"
```

You want to transform this into a dictionary like:

```python
fields = {
  "position": "0",
  "number": "1",
  "small": "H",
  "molar": "1.00794",
  "electron": "1"
}
```

### Visual “chunk” breakdown

Take one chunk:

```
value = "position:0, number:1, small: H, molar:1.00794, electron:1 None"
```

#### 1) Split by comma → separate **field chunks**

```python
for nextData in value.split(","):
```

This produces pieces like:

* `"position:0"`
* `" number:1"`
* `" small: H"`
* `" molar:1.00794"`
* `" electron:1 None"`

#### 2) Clean and split by `:` → separate **key/value**

```python
captured = nextData.strip().replace("$", "")
key, val = captured.split(":", 1)
fields[key.strip()] = val.strip()
```

So for `" small: H"`:

* `captured` becomes `"small: H"`
* `key = "small"`
* `val = "H"`

And you store it in `fields`.

#### 3) Pull only what you need (with safe defaults)

```python
number   = fields.get("number", "")
small    = fields.get("small", "")
molar    = fields.get("molar", "")
electron = fields.get("electron", "")
```

Using `get(..., "")` prevents `None` from appearing when something is missing.

---

## How the HTML is assembled

### 1) You create one HTML block per element and append to `rows`

```python
rows.append(f"""
  <table> ... </table>
""")
```

So `rows` is a list of HTML strings.

### 2) You join everything into the `<body>`

```python
doc = f"""
<body>
  {''.join(rows)}
</body>
"""
```

That creates **one final HTML document string**, and you write it to `periodic_table.html`.

---

## Summary (mental model)

* **List stage**: file → `myPeriodicTable` (raw cleaned lines)
* **Dict stage**: each line → `myJson[element] = raw_fields`
* **Chunk parsing stage**: raw_fields string → `fields` dict
* **HTML stage**: `fields` → HTML block → append to `rows`
* **Final assembly**: `''.join(rows)` → injected into `<body>` → write file

