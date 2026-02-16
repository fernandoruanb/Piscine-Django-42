# Simple CV Project (HTML & Basic CSS)

![CV / Resume Icon](https://cdn.pixabay.com/photo/2021/02/02/12/22/cv-5973796_1280.png)

## Introduction

In this project, I built a simple curriculum vitae (CV) using **semantic HTML** and **basic CSS**.

The goal is to practice clean structure and readability while respecting the separation between **content (HTML)** and **presentation (CSS)**. The page includes essential CV information (name, skills, and career path) and uses common HTML elements such as headings, links, lists, and a table to organize the content.
## HTML Document Setup (DOCTYPE + `<head>`)

The line `<!DOCTYPE html>` declares that this file is an **HTML5 document**.  
By explicitly defining the document type, we avoid compatibility issues and force the browser to render the page in **standards mode**, preventing unexpected layout or interpretation problems.

```html
<!DOCTYPE html>
```
# Analyzing the cv.html tags
```html
<html lang="en">
```
Defines the main language of the page as English. This helps accessibility tools (screen readers) and search engines.
# The **head** Section

The **head** contains the metadata and configuration of the page.
This content is not displayed directly to the user, but it defines how the browser should interpret and present the document.
```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="author" content="Fernando Ruan">
  <title>My Beautiful CV</title>
  <style>
    ...
  </style>
</head>
```
# Meta tags used

**meta charset="utf-8"**
Defines the character encoding as UTF-8, allowing the document to correctly display accents and special characters.

**meta name="viewport" content="width=device-width, initial-scale=1.0"**
Makes the page responsive on mobile devices by matching the layout width to the device width.

**meta name="author" content="Fernando Ruan"**
Specifies the author of the document.

# Page title

**\<title>My Beautiful CV</title\>**
Sets the title shown in the browser tab and used by bookmarks.

## Page Content (the `<body>`)

The `<body>` contains everything that is **visually displayed to the user**.  
In this CV project, the body is organized with semantic sections to keep the document clean, readable, and structured.

---

### 1) `<header>` + `<nav>` (External Links)

```html
<header>
  <nav>
    <a href="...">GitHub</a>
    <a href="...">Linkedin</a>
  </nav>
</header>
````

* `<header>` represents the top section of the page.
* `<nav>` indicates a navigation area (here used to provide external links).
* `<a>` creates clickable hyperlinks to my GitHub and LinkedIn profiles.

This keeps important contact/professional links easy to find.

---

### 2) `<main>` (Main CV Content)

```html
<main>
  ...
</main>
```

`<main>` contains the **primary and unique content** of the page — the CV itself.
Inside `<main>`, the content is divided into logical blocks:

#### a) Main title and profile image

```html
<h1>My beautiful CV</h1>
<img src="..." width="200" height="200">
```

* `<h1>` is the main title of the document.
* `<img>` displays a profile illustration/image to make the page more personal and visually appealing.

---

### 3) Personal Data Table

```html
<table>
  <tr>...</tr>
  <tr>...</tr>
</table>
```

This table organizes basic personal information in a structured format:

* `<th>` defines table headers (labels)
* `<td>` defines table data (values)
* The **bottom-right cell** uses an inline style to apply a specific border color (`#424242`), following the project constraint.

---

### 4) CV Sections with `<section>`

Each CV topic is wrapped in a `<section>` to keep semantic organization:

#### a) Description

```html
<section>
  <h2>Description</h2>
  <p>...</p>
</section>
```

* `<h2>` is a subsection title.
* `<p>` holds the career summary and future goals.

#### b) Soft Skills (unordered list)

```html
<section>
  <h2>Soft Skills</h2>
  <ul>
    <li>...</li>
  </ul>
</section>
```

* `<ul>` represents a bullet list.
* `<li>` represents each item (skill).

#### c) Hard Skills (ordered list)

```html
<section>
  <h2>Hard Skills</h2>
  <ol>
    <li>...</li>
  </ol>
</section>
```

* `<ol>` represents a numbered list.
* `<li>` represents each item (technical skill).

---

### 5) Portfolio/Projects Table

```html
<section>
  <h2>Portfolio/Projects</h2>
  <table>...</table>
</section>
```

This second table summarizes projects with:

* Project name
* Short description
* Technologies used

Again, the **bottom-right table cell** receives the `#424242` border color to match the required constraint.

---

### 6) `<footer>` (End of Page)

```html
<footer>
  <p><strong>Made by Fernando Ruan</strong></p>
</footer>
```

* `<footer>` represents the final part of the page.
* `<strong>` is used to emphasize the author line semantically.

---

### Summary

The body is structured with semantic HTML to make the CV:

* Easy to read
* Well organized
* Valid and consistent
* Ready for basic styling using CSS


## CSS Styling Explanation (`<style>`)

This project uses basic CSS to control layout, alignment, tables, and lists while keeping the HTML semantic and readable.

---

### 1) Centering the whole page with Flexbox (`body`)

```css
body {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}
```

* `display: flex;` turns the `<body>` into a flex container, allowing easy alignment of its children (`header`, `main`, `footer`).
* `flex-direction: column;` stacks elements vertically (top to bottom).
* `align-items: center;` centers all direct children horizontally.
* `text-align: center;` centers inline content such as text and links.

Result: the CV content stays centered in the page.

---

### 2) Pushing the footer to the bottom (`footer`)

```css
footer {
  margin-top: auto;
}
```

* In a flex column layout, `margin-top: auto;` consumes remaining vertical space.
* This pushes the footer downward so it stays at the bottom when there is enough height in the page.

---

### 3) Keeping section lists aligned and readable (`main > section ul/ol`)

```css
main > section ul,
main > section ol {
  display: inline-block;
  text-align: left;
  margin: 0;
  padding-left: 1.5em;
  list-style-position: inside;
}
```

This targets lists inside sections (Soft Skills and Hard Skills):

* `display: inline-block;` keeps the list as a compact block that can still be centered by the surrounding layout.
* `text-align: left;` makes list items readable (not centered line-by-line).
* `margin: 0;` removes the default browser margin that can create uneven spacing.
* `padding-left: 1.5em;` adds a controlled indentation.
* `list-style-position: inside;` keeps bullets/numbers aligned inside the list block, improving visual consistency.

Result: lists remain centered as a block, but the text is aligned left inside the list.

---

### 4) Table layout: merged borders + centered table

```css
table {
  border-collapse: collapse;
  margin: 0 auto;
}
```

* `border-collapse: collapse;` merges the borders of adjacent cells so the table doesn’t show double borders.
* `margin: 0 auto;` centers the table horizontally.

---

### 5) Visible solid borders for the table and its cells

```css
table, th, td {
  border: 1px solid #000;
}
```

This ensures that:

* The table outline is visible.
* Each header cell (`th`) and data cell (`td`) has a solid border.

This is required by the project constraints.

---

### 6) Centering data inside table cells

```css
td {
  text-align: center;
}
```

* Centers text horizontally inside every `<td>`.

---

### 7) Overriding list alignment inside table cells (`td ul/ol`)

```css
td ul, td ol {
  text-align: left;
}
```

* Since `<td>` is centered, lists inside a cell would also inherit that centering.
* This rule overrides it and keeps list text left-aligned inside table cells.

Result: the "Languages" list looks clean inside the table.

---

### Summary

This CSS setup:

* Centers the entire CV layout with Flexbox
* Keeps the footer positioned at the bottom in the flex layout
* Styles tables with solid, collapsed borders
* Ensures lists are readable (left-aligned) while still being visually centered as blocks



