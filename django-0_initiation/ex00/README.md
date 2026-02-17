# Resolving (Translating) a bit.ly Link Using Sh

![Search box / HTTP WWW illustration](https://cdn.pixabay.com/photo/2012/02/16/12/09/search-13476_1280.jpg)

## Core Idea

The goal of this exercise is to **discover the original destination URL** behind a shortened link such as `https://bit.ly/...`.

Bitly works as a **database-driven URL shortener**:

- When a short link is created, Bitly stores a mapping like:

short_code -> original_target_url

- The short code does **not** mathematically contain the original URL.
- Therefore, we **cannot reverse it using pure mathematics**.
- We must **query the Bitly server**, because the mapping is stored in its database.

---

## How the Redirect Reveals the Real URL

When someone accesses:

https://bit.ly/ABC


The server responds with an HTTP redirect (usually `301` or `302`) and includes the real destination inside the HTTP header:

Location: https://real-destination.com/


So the solution is simple:

> We just need to read the `Location` header.

---

## Why Use `curl -I`

We only need the HTTP headers — not the page content.

- `curl -I` retrieves **only the headers**
- `-s` (silent) removes progress and extra output

So we use:

```sh
curl -sI URL | grep Location | cut -d ' ' -f 2
```

By this way, we can get our output. As we are using shellscript, we need to store it into a variable. In my
example, I put into a variable called "output"

```sh
output=$(curl -sI URL | grep Location | cut -d ' ' -f 2)
```

Finally, we can print the content using the sh builtin command "echo"

```sh
echo "$output"
```

# How to use

```sh
./myawesomescript.sh bit.ly/ABC
```
The example above is using an imaginary bit.ly URL only to be didatic

# Direct explanation

Bitly stores the mapping in a database, so the short link is not mathematically reversible.

The Bitly server reveals the real destination through an HTTP redirect.

The Location header contains the true URL.

curl -sI gets headers only, grep filters Location, and cut extracts the URL.

The final result can be stored in a variable and printed with echo.
