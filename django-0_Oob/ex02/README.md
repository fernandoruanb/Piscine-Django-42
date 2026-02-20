
## Quick Review: What This Code Teaches

This script demonstrates core **Object-Oriented Programming (OOP)** concepts in Python using a hierarchy of hot drinks.

---

## 1) Inheritance (Base Class → Subclasses)

- `HotBeverage` is the **base class** (general model of a hot drink).
- `Coffee`, `Tea`, `Chocolate`, and `Cappucino` are **subclasses** that inherit from `HotBeverage`.

This means every subclass automatically gets the base behavior (methods/structure) unless it overrides something.

---

## 2) Constructor Reuse with `super().__init__()`

Each subclass calls:

```python
super().__init__()
````

This ensures the base class initializes common attributes first:

* `self.price`
* `self.name`

After that, the subclass **updates** only what changes.

Example:

* Base sets `price = 0.30`, `name = "hot beverage"`
* `Coffee` modifies to `price = 0.40`, `name = "coffee"`

This reduces duplication and centralizes shared initialization.

---

## 3) Method Overriding (Override)

The base class defines:

```python
def description(self):
    return "Just some hot water in a cup."
```

Some subclasses override `description()` with their own version:

* `Coffee.description()` returns a coffee-specific string
* `Chocolate.description()` returns a chocolate-specific string
* `Cappucino.description()` returns an Italian phrase

This is **override**: same method name, different implementation in the child class.

---

## 4) Polymorphism (Same Call, Different Behavior)

The program repeatedly does:

```python
desc = hotBeverage.description()
```

Even though the code calls the same method name (`description()`), the result changes depending on the object type:

* If `hotBeverage` is `HotBeverage`, it returns the base description.
* If it is `Coffee`, it returns the coffee description.
* If it is `Chocolate`, it returns the chocolate description.

This is **polymorphism**: one interface, multiple behaviors.

---

## 5) Dynamic Dispatch inside `__str__`

The base class implements:

```python
def __str__(self):
    return f"... description: {self.description()}"
```

Key point:

* `__str__` is defined only once in the base class.
* It calls `self.description()`.
* Python dynamically chooses the correct `description()` method (base or overridden).

So printing any beverage automatically prints the right description.

This is a clean OOP pattern:
**base class controls the format; subclasses customize the content.**

---

## 6) Testing Behavior Explicitly

The code prints each object and also calls `description()` directly:

* `print(hotBeverage)` tests `__str__` output.
* `hotBeverage.description()` tests the overridden method directly.

This confirms both:

* formatting works (`__str__`)
* polymorphism works (`description()`)

---

## Key Takeaways (Fast)

* **Inheritance**: subclasses reuse structure from a base class.
* **super()**: base initialization happens first, then subclasses modify.
* **Override**: subclasses replace a base method with their own behavior.
* **Polymorphism**: `description()` returns different values depending on the object type.
* **Best practice shown**: base `__str__` calls a method (`description()`) so subclasses can customize output without rewriting `__str__`.

This is a strong example of scalable design: shared logic stays in the base class, specialization stays in each subclass.

