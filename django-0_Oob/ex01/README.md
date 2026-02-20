## Concepts Learned in This Code

This code introduces fundamental **object-oriented programming (OOP)** concepts in Python through a simple and realistic scenario.

### Classes and Objects
Two classes are defined: `Intern` and `Coffee`.  
A class represents a blueprint, while an object is an instance created from that blueprint.  
For example, `Intern()` and `Coffee()` create concrete objects based on their respective classes.

### Constructors (`__init__`)
Both classes implement a constructor using the `__init__` method.
- The `Intern` constructor optionally receives a name. If no name is provided, a default message is assigned.
- The `Coffee` constructor exists even though it performs no action, showing that object creation can be explicit even when no initialization logic is required.

### String Representation (`__str__`)
The `__str__` method defines how an object is displayed when printed.
- `Intern.__str__()` returns the intern’s name.
- `Coffee.__str__()` returns a fixed sentence describing the coffee.

This allows objects to be printed in a human-readable way.

### Encapsulation of Behavior
Each class owns its behavior:
- An `Intern` can make coffee using `make_coffee()`.
- An `Intern` cannot perform arbitrary work, enforced by the `work()` method.

This separation keeps responsibilities clear and aligned with object-oriented design.

### Exception Raising
The `work()` method deliberately raises an `Exception` to signal that the intern is not allowed to perform that action.
This demonstrates how exceptions are used to represent invalid operations rather than returning error values.

### Exception Handling (`try / except`)
The main program captures the exception raised by `work()` using a `try / except` block.
This shows how error handling is managed outside the class, keeping the class logic clean and focused.

### Default Values and Conditional Logic
The `Intern` class demonstrates how default values are assigned when optional parameters are omitted.
This pattern ensures safe object creation even when incomplete information is provided.

### Method Interaction Between Objects
The `make_coffee()` method returns a new `Coffee` object, illustrating how objects can create and interact with other objects.

---

#### Overall, this code demonstrates:
- Object creation and representation
- Method responsibilities
- Controlled error signaling using exceptions
- Clean separation between behavior and error handling

These concepts form the foundation of robust object-oriented programming in Python.

