# Correcting an invalid HTML file

The challenge here is to fix using https://validator.w3.org/ a w3c validator. We did it to study the syntax. You can see the main mistakes here to help you to study HTML and review problems.

## Main HTML validation mistakes (what went wrong and how to fix)

### 1) Missing / broken document structure (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`)

**Problem:** Your snippet starts with a `<script>` before `<head>` and doesn’t show a proper `<html>...</html>` wrapper at the top. Browsers try to “auto-fix” this, but the W3C validator will report many cascading errors.

**Bad:**

```html
<script ...></script
<head> ...
```

**Fix:** Always start with:

```html
<!DOCTYPE html>
<html lang="fr">
  <head> ... </head>
  <body> ... </body>
</html>
```

---

### 2) Unclosed / malformed tags (syntax errors that break the parser)

These are the most destructive errors because once the parser gets confused, *everything after can be interpreted wrong*.

**Examples in your code:**

* Missing `>` in `</script`

  ```html
  <script ...></script
  ```
* Wrong closing tag order (you close `</article>` before `</footer>` in the first article)
* Typos in tag names:

  * `</times>` instead of `</time>`
  * `</asside>` instead of `</aside>`
* Broken anchor closing tag:

  ```html
  <li><a href="#">About</></li>
  ```

**Fix:** Make sure every opening tag has a correct closing tag and correct spelling:

```html
</script>
</time>
</aside>
</a>
```

---

### 3) `<meta charset="...">` used incorrectly

**Problem:** You wrote:

```html
<meta charset="fr" /></meta>
```

Issues:

* `charset` must be a real encoding like `utf-8`, not a language code.
* `<meta>` is a **void element** (it must not have `</meta>`).

**Fix:**

```html
<meta charset="utf-8">
```

---

### 4) `<link rel="stylesheet">` placed in the wrong place

**Problem:** You placed `<link>` inside `<body>`:

```html
<body>
  <link rel="stylesheet" href="style.css" />
```

The validator expects stylesheets in `<head>` (it may still “work” in browsers, but it’s invalid).

**Fix:**

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

---

### 5) Invalid `href` attributes (empty or missing quotes)

You have anchors like:

```html
<a href=>Opening Date Announced</a>
<a href=>Read More &&raquo;</a>
```

Problems:

* `href=` is missing quotes and a URL.
* In the second one you also use a broken HTML entity `&&raquo;`.

**Fix (placeholder links):**

```html
<a href="#">Opening Date Announced</a>
<a href="#">Read More &raquo;</a>
```

---

### 6) Heading tag mismatch (`<h2>` closed as `</h1>`)

This is a direct validation error:

**Bad:**

```html
<h2 ...>...</a></h1>
```

**Fix:**

```html
<h2 ...>...</a></h2>
```

---

### 7) Invalid nesting (putting `<p>` inside `<b>` / mixing block + inline incorrectly)

You wrote:

```html
<b class="article-lead"><p> ... </b></p>
```

Problems:

* `<p>` is a block element and should not be placed inside inline elements like `<b>`.
* The closing order is wrong (`</b>` closes before `</p>` but opened outside).

**Fix:** Put `<b>` (or better `<strong>`) inside the `<p>`:

```html
<p class="article-lead"><strong>Text here...</strong></p>
```

---

### 8) Footer/article closing order is broken

In your first article you effectively do:

```html
<footer>...
</article>
</footer>
```

That’s invalid because `<footer>` must be closed **before** you close the `<article>`.

**Fix:**

```html
</footer>
</article>
```

---

### 9) Broken HTML entities (`&&raquo;`)

You have:

```html
Read More &&raquo;
```

The correct entity is:

```html
&raquo;
```

**Fix:**

```html
Read More &raquo;
```

---

### 10) Wrong closing tags and missing closing tags in lists/anchors

Example:

```html
<li><a href="#">About</></li>
```

This breaks the list markup.

**Fix:**

```html
<li><a href="#">About</a></li>
```

---

### 11) Heading hierarchy warning (skipping levels: `h1` → `h3`)

You used:

```html
<h1>Art Gallery Blog</h1>
...
<h3>About</h3>
```

Validator warns because you skipped `h2`.

**Fix:** Use `h2` for “About” (or reorganize headings):

```html
<h2>About</h2>
```

---

## The “big idea” (why the validator explodes)

Most of your errors come from two root causes:

1. **Broken syntax** (missing `>`, wrong closing tags, typos like `</times>`, `</asside>`)
2. **Invalid structure** (styles/script/meta/link placed in wrong areas, invalid nesting)

Once you fix syntax + structure, most other warnings disappear automatically.
