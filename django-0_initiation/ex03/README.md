# Copy HTML Spier

In that exercise we need to copy a HTML using the extracted CSS. In other words, we need to learn how to use the
CSS and connect them to the tags in a HTML file. That is the challenge here.

## HTML overview: tags and attributes used in your snippet

### `<!DOCTYPE html>`

Declares the document type as **HTML5**. This makes the browser render the page in standards mode (not quirks mode).

---

## Root structure

### `<html lang="en">`

The root element of the document.

* **`lang="en"`**: declares the primary language of the page as English (important for accessibility tools and SEO).

---

## Head section

### `<head> ... </head>`

Contains **metadata** and links to external resources (not visible as page content).

### `<meta charset="utf-8">`

Sets the character encoding to **UTF-8**, which supports most characters and symbols.

### `<meta name="viewport" content="width=device-width, initial-scale=1.0">`

Controls how the page scales on mobile devices.

* **`name="viewport"`**: targets the viewport settings.
* **`content="width=device-width, initial-scale=1.0"`**:

  * `width=device-width`: use the device’s screen width
  * `initial-scale=1.0`: start at normal zoom level

### `<meta name="author" content="Fernando Ruan">`

Metadata describing the document author.

* **`name="author"`**: the metadata type.
* **`content="Fernando Ruan"`**: the author name.

### `<link rel="stylesheet" href="./style.css">`

Links an external **CSS file** to the HTML.

* **`rel="stylesheet"`**: tells the browser this link is a stylesheet.
* **`href="./style.css"`**: path to the CSS file (`./` means “in the same folder as this HTML file”).

### `<title>Copy HTML Spier</title>`

Sets the page title shown in the **browser tab** and used by bookmarks/search results.

---

## Body section

### `<body> ... </body>`

Contains all the visible content rendered in the page.

---

## List / layout container

### `<ul> ... </ul>`

An **unordered list** (a list of items). You’re using it as a layout container for two columns.

### `<li> ... </li>`

A **list item** inside the `<ul>`.
In your CSS, each `li` is styled as a column (`width: 50%` and `float: left`).

> **Note:** In valid HTML structure, items like `<h2>` should be inside a `<li>` if they are part of the list. In your snippet, the `<h2>Backend</h2>` appears between `</li>` and `<li>`, which is not ideal semantically. (It will often still display, but it’s not correct structure.)

---

## Headings and labels

### `<h2>Frontend</h2>` / `<h2>Backend</h2>`

Section headings. `<h2>` is a second-level heading used to label major sections.

---

## Skill line label

### `<p data-value="80">HTML5</p>`

A paragraph used here as a label row (skill name).

* **`data-value="80"`**: a custom HTML *data attribute*.

  * `data-*` attributes are designed to store extra information on an element.
  * Your CSS can read it using `attr(data-value)`.
  * Your JavaScript can read it using `element.dataset.value`.

In the CSS we likely have something like:

```css
p[data-value]:after {
  content: attr(data-value) '%';
}
```

That means the `80` becomes visible as text (e.g., `80%`) without you manually typing it.

---

## Progress bars

### `<progress class="html5" value="80" max="100">80%</progress>`

A native HTML **progress bar** element (a determinate progress indicator).

* **`class="html5"`**: assigns a CSS class so you can style this specific bar (color/gradient/stripes).
* **`value="80"`**: the current progress amount (numerator).
* **`max="100"`**: the maximum value (denominator).
  So `80 / 100` = 80%.
* **Fallback text (`80%`)**: text inside `<progress>...</progress>` is shown only in browsers that don’t support the progress element (or for accessibility/fallback).

### About your `class="node.js"`

In this line:

```html
<progress class="node.js" value="35" max="100">35%</progress>
```

* `class="node.js"` is **not the same** as `class="node-js"`.
* In CSS, a dot has special meaning (class selector), and your stylesheet already uses `.node-js` (with a hyphen).
* Use:

```html
<progress class="node-js" value="35" max="100">35%</progress>
```

---

## Summary of “custom data”

* `data-value="..."` is **not a tag**, it’s a **custom attribute** following the `data-*` convention.
* It’s used so CSS/JS can read the value and display/use it (like showing “80%” automatically).
