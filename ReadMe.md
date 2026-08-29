# 🐍 Python OOP Learning Journey

This repository documents my practical journey of learning and applying **Object-Oriented Programming (OOP) with Python**.

The goal is not only to understand OOP concepts theoretically, but to apply them through coding exercises, debugging, refactoring, and progressively building real-world systems.

---

## 🎯 Learning Objectives

Through this repository, I am developing a strong understanding of:

* Object-Oriented Programming principles
* Object modeling and system design
* Reusable and maintainable Python code
* Encapsulation and controlled access to data
* Inheritance and class hierarchies
* Polymorphism and dynamic behavior
* Abstraction and interfaces
* Composition and object relationships
* Python special/dunder methods
* Responsibility assignment between objects
* Clean and maintainable OOP design

---

## 📚 Topics Covered

### 1. Classes & Objects

* Defining classes
* Creating objects
* Instance attributes
* Class attributes
* Instance methods
* Understanding `self`

### 2. Constructors

* `__init__()`
* Initializing object state
* Default parameters
* Constructor behavior

### 3. Encapsulation

* Public attributes
* Protected attributes (`_attribute`)
* Private attributes (`__attribute`)
* Name mangling
* Getters and setters
* Controlled state modification

### 4. Properties

* `@property`
* Property setters
* Attribute validation
* Read-only properties
* Controlled access to internal state

### 5. Inheritance

* Parent/base classes
* Child/derived classes
* Method inheritance
* Constructor inheritance
* `super()`
* Method overriding

### 6. Polymorphism

* Method overriding
* Common interfaces
* Different implementations
* Polymorphic behavior
* Duck typing

### 7. Abstraction

* Abstract classes
* Abstract methods
* `ABC`
* `@abstractmethod`
* Defining implementation contracts

### 8. Composition

* Objects containing other objects
* HAS-A relationships
* Object collaboration
* Responsibility distribution between classes

### 9. Python Dunder Methods

* `__init__`
* `__str__`
* `__eq__`
* `__repr__`
* Other special methods

---

## 🚀 Practical Application

The concepts in this repository are being applied through a progressively developed **Library Management System**.

Current domain model:

```text
Library
   │
   ├── Book
   │
   ├── User
   │
   └── Loan
          │
          ├── User
          └── Book
```

### Current Components

**Book**

* Book information and attributes
* Attribute validation
* Availability state
* Borrowing and returning
* `__str__`
* `__eq__`

**User**

* User information
* Attribute validation
* Encapsulated attributes
* `__str__`

**Loan**

* Associates a `User` with a `Book`
* Tracks borrowing date
* Automatically calculates due date
* Uses object composition
* Validates associated objects

**Library**

* Maintains a collection of `Book` objects
* Adding books
* Removing books
* Finding books
* Listing books

---

## 🧠 OOP Principles in Practice

The project demonstrates several important object-oriented relationships:

### IS-A relationship

Used with inheritance:

```text
Dog IS-A Animal
```

### HAS-A relationship

Used with composition:

```text
Library HAS-A collection of Books

Loan HAS-A User
Loan HAS-A Book
```

### Object Collaboration

Different objects work together rather than placing all responsibilities inside one class.

```text
User
  │
  ↓
Loan
  │
  ↓
Book
  │
  ↓
Library
```

---

## 🔄 Book State Management

The `Book` class manages its availability state through controlled operations.

```text
AVAILABLE
    │
    │ borrow()
    ▼
BORROWED
    │
    │ return_book()
    ▼
AVAILABLE
```

This demonstrates how an object can combine **state, behavior, validation, and controlled state transitions**.

---

## 📈 Learning Progress

### Fundamentals

* [x] Classes
* [x] Objects
* [x] Constructors
* [x] Instance attributes
* [x] Class attributes
* [x] Instance methods
* [x] `self`

### Encapsulation

* [x] Public attributes
* [x] Protected attributes
* [x] Private attributes
* [x] Name mangling
* [x] Properties
* [x] Getters and setters
* [x] Attribute validation
* [x] Controlled state transitions

### OOP Principles

* [x] Encapsulation
* [x] Inheritance
* [x] Method overriding
* [x] Polymorphism
* [x] Abstraction
* [x] Composition
* [x] Object collaboration

### Python OOP

* [x] `__init__`
* [x] `__str__`
* [x] `__eq__`
* [ ] `__repr__`
* [ ] Additional dunder methods

### Software Design

* [x] Responsibility assignment
* [x] HAS-A relationships
* [x] Basic domain modeling
* [ ] SOLID principles
* [ ] Dependency injection
* [ ] Design patterns
* [ ] Clean architecture
* [ ] Unit testing

---

## 🛠️ Tools

* Python 3
* Git
* GitHub
* VS Code

---

## 🧩 Learning Approach

The learning process follows:

```text
Learn
  ↓
Implement
  ↓
Test
  ↓
Break
  ↓
Debug
  ↓
Understand
  ↓
Refactor
```

The objective is to develop the ability to **design software using objects and relationships**, rather than simply memorizing OOP syntax.

---


## 👨‍💻 Author

**David**

Computer Engineering Student | AI & Intelligent Systems Enthusiast

Interested in:

**Artificial Intelligence • Machine Learning • LLMs • Intelligent Systems • Automation • Software Engineering • Web Development**
