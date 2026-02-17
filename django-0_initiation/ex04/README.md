# Importing scripts in the correct order

In that exercise, the objective is to import 4 files and executing them correctly to show a popup in the final.

```bash
cat file1.js file2.js file3.js file4.js 
function unicorn()
{
	puffin()
}

function cat()
{
	whale();
}

cat()
function whale()
{
	unicorn();
}
function puffin()
{
	alert("Exercice réussi!");
}
```

The secret here is only checking each file and import them in the correct order. For example, the last function
cannot have a clear dependence, then, it must be the first to be loaded. Next, the file1.js because that file calls
the puffin function, already loaded. Following that strategy, we can solve the dependences correctly.

We can solve it adding a javascript loader, but, in the rules of that exercise, we are forbidden to add another javascript or modify the original files.

# Script tag in HTML

We can put in the **\<head\>** tag the script

```html
	<script src="./file4.js" defer></script>
```

So, we import the js file and load it only after all HTML finished to be parsed, it because I put the attribute defer here.
