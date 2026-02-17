# Formularie exercise

That exercise consisting in to write a form to make the javascript run without problems during the click event using the button.

## HTML: what each tag/attribute is doing here

### `<!DOCTYPE html>`

Tells the browser this document uses **HTML5**, so it renders in standards mode.

### `<html lang="en">`

Root element of the page.
`lang="en"` declares the document language as English (helps accessibility tools and search engines).

### `<head> ... </head>`

Metadata/configuration for the page (not visible content).

#### `<meta charset="utf-8">`

Sets character encoding to UTF-8 (supports accents, symbols, etc.).

#### `<meta name="viewport" content="width=device-width, initial-scale=1.0">`

Makes the layout adapt to mobile screens:

* `width=device-width`: uses the device’s real width
* `initial-scale=1.0`: initial zoom level

#### `<meta name="author" content="Fernando Ruan">`

Author metadata (informational).

#### `<script src="./popup.js" defer></script>`

Loads your JavaScript file.

* `defer` means: download now, **execute after HTML is parsed** (so DOM elements exist when your JS runs).

#### `<title>Form</title>`

Text shown in the browser tab.

#### `<style> ... </style>`

Inline CSS for this page.

---

### `<body> ... </body>`

The visible page content.

### `<form id="contactForm" action="#" method="post">`

Creates a form container.

* `id="contactForm"`: unique identifier (useful for JS/CSS selection)
* `action="#"`: where the form would submit (here it points to the same page)
* `method="post"`: HTTP method if submitting to a server

### `<label for="firstname"> ... </label>`

Text label describing a field.
`for="firstname"` connects the label to `<input id="firstname">` (clicking the label focuses the input; improves accessibility).

### `<br>`

Line break (forces a new line). You’re using it for layout spacing.

### `<strong> ... </strong>`

Makes text semantically “strong importance” (usually bold).

### `<input ...>`

Creates a form input field.

#### Common attributes you use:

* `id="..."`: unique identifier in the page (CSS/JS target)
* `name="..."`: key name sent when the form submits
* `type="..."`: input type behavior/validation
* `placeholder="..."`: hint text shown when empty
* `required`: browser will block submission if empty/invalid

#### Your inputs:

* `type="text"`: plain text
* `type="tel"`: phone-style input (mobile keyboards may change)
* `type="number"`: numeric input with up/down controls

  * `min="0"` / `max="120"`: allowed range
* `type="email"`: requires email format
* `type="radio"`: choose **one** option within the same `name` group

  * All `name="gender"` radios form a group: only one can be selected.
  * Putting `required` on **one** radio in the group is enough to require a selection.
* `type="checkbox"`: independent on/off option

  * If checked, it submits `student=true` (because `value="true"`)

### `<button type="submit" onclick="displayFormContents()">Send</button>`

A submit button.

* `type="submit"` triggers form submission (and browser validation).
* `onclick="displayFormContents()"` calls your JS function when clicked.

**Note:** if your goal is “only run JS when the form is valid”, the cleaner pattern is to handle the form’s `submit` event and call `event.preventDefault()` inside JS only when you want to stop the actual submission.

---

## CSS: what each rule is doing

### `body { ... }`

```css
body {
  flex-direction: column;
  display: flex;
  text-align: center;
  align-items: center;
  background-color: #0A1F44;
}
```

* `display: flex;` turns the body into a flex container.
* `flex-direction: column;` stacks children vertically (top to bottom).
* `align-items: center;` centers children **horizontally** within the page.
* `text-align: center;` centers inline text content (labels, etc.).
* `background-color: #0A1F44;` sets a dark blue background.

### `form { ... }`

```css
form {
  border: 3px solid #000;
  width: 300px;
  background-color: #F4F4F4;
  margin-top: 20px;
}
```

* `border: 3px solid #000;` thick black border.
* `width: 300px;` fixed form width.
* `background-color: #F4F4F4;` light gray form background.
* `margin-top: 20px;` pushes the form down from the top.

### `input { ... }`

```css
input {
  text-align: center;
  border: 1px solid #000;
  width: 200px;
}
```

Applies to **all inputs** by default:

* `text-align: center;` centers typed text inside inputs.
* `border: 1px solid #000;` thin black border.
* `width: 200px;` default width (overridden for some inputs below).

### `#age { width: 100px; }`

```css
#age { width: 100px; }
```

Overrides the default input width only for the input with `id="age"`.

### `#email { width: 250px; }`

```css
#email { width: 250px; }
```

Makes the email field wider than other default inputs.

### `#gender_male, #gender_female, #gender_other, #student { width: 20px; }`

```css
#gender_male, #gender_female, #gender_other, #student {
  width: 20px;
}
```

Targets those specific radio/checkbox inputs and makes them small.

---
