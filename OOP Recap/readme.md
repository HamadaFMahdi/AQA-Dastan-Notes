## Basics
### 4 pillars:
* 1. Abstraction
* 2. Encapsulation
* 3. Inhertiance
* 4. Polymorphism

### Classes:
* A `class` is a representation of an entity.
* Each `class` has `attributes` and `methods`.
* `__init__` is the contructor.
    * Creates an instance/object of class.
    * An instance/object is a specific occurence of class.
* `self` is the current instance we are dealing with.
* E.g.
```python
noir = Cat('Noir', 'Black')
noir.eat('Fish')
# can be written as eat(noir, 'Fish')
# I.E. noir is self.
```

### Encapsulation:
* Gives you **control** over your classes.

* Private is denoted by `__`
    * Cannot be accessed from outside of the class
    * Cannot be inherited.
* Protected is denoted by `_`
    * Cannot be accessed from outside of the class
    * Can be inherited.
* We can access these from outside using `getters` and `setters`. These allow us to write custom logic e.g. adding auth, boundaries etc.

### Inheritance:
* When a child class inherits attributes and methods (that are not private) from the parent class.

### Polymorphism:
* Gives us **predictability**
* We can treat child classes like the parent class.
* We call the same method name but the underlying implementation differs.
* When we change the method in the child class, this is called **overriding**.
* **Overloading** is when a method does more than one thing based on a parameter's value changing.

### Super!!
* The `Super` function allows you to access the parent class' attributes and methods.
* Usually useful if:
    * you want to add functionality to a parent method.
    * you want to add attributes to the constructor.