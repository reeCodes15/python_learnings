Python Interview Prep


https://www.simplilearn.com/tutorials/python-tutorial/python-interview-questions   (33-48 dropped for now)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. What can be the keys of a dictionary in Python?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

any hashable object can be the key of a dictionary.

Any hashable object is immutable. As an example, the code below is correct as this tuple and all of its elements are hashable.
Please be aware that sets, dictionaries, and lists are not hashable, therefore cannot be the keys of a dictionary.

my_d = {
    (12, "job", (1, 2, 3)): 123
}

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2. What is CPython?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Python is an interpreted language. Its code is first interpreted by another program (interpreter) and then compiled into something called bytecode. Bytecode is made out of bytes that represent the machine’s instructions. CPython is the implementation of Python whose bytecode is in the C programming language.

On the other hand, we have Jython which bytecode is in Java or other Python implementations.

We also have something called Cython, which is the compiled language used to create CPython extensions. The Cython language is a
 superset of Python that supports several C programming language features.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
3. What is LEGB in Python?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When the Python interpreter is trying to look up a name, it uses the LEGB rule to resolve the names (variable, function, and other object names). 
It first checks for the existence of names in L, E, G, and B scopes in the order below:

Local Scope: The area within a function body or a lambda expression.
Enclosing Scope: Assume we have a function called outer which has a nested function. Enclosing scope (or nonlocal scope) is
 the area within the body of outer function.
Global Scope: The names in this scope are visible to all code in one Python script (in one file having a .py extension).
Built-in Scope: The names that exist in this scope are loaded when we run a Python shell/script. Keywords such as in, and, 
or, def, class and expressions like __main__, __file__ are some examples.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
4. What are the usages of nonlocal and global keywords in Python?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This interview question has a direct relationship with the previous one. The code sample below illustrates the usage of these two keywords:

variable = "hello 1" # This variable is declared in the Global scope

def fun():
    global variable # Without this we would not be able to change the variable value
    variable = "hello 2"
    
fun()
print(variable) # "hello 2"
………………………………………………………………..
def outer():
    variable = "hello 1" # This variable is declared in a Local scope
    

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
5. What is GIL and why is it important?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GIL, or Global Interpreter Lock, is a construct/tool that makes sure that only one thread at a time can execute a Python program. In other words, this lock belongs to the Python interpreter and it uses it to lock a thread.

For example, thread T1 acquires GIL and does its job. While the Python interpreter is using GIL to lock T1, all other threads have to wait
 After T1 finishes, it releases GIL and passes it to another thread T2 that needs it. The reason for the GIL presence is to make CPython 
 thread-safe and not allow some threads to interfere with one another.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
6. How does Python handle memory management?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Before answering senior Python interview questions like this one, you must be aware that we are talking about the CPython implementation. 
Other Python implementations may have different rules and requirements for memory management.

Assume you have a Python script and you want to execute it. When you execute this file, the Python interpreter occupies some “area” of the RAM.
 This “area” itself is divided into two categories: the stack and the private heap.

Now assume that in this script we have declared a string object a = “hello”. When we execute this script, the CPython memory management 
system creates an object of type string on the private heap. This object contains three fields:

Type: This is a string (note that Python is a dynamically typed programming language, so it will understand your object type to store).
Value: This is “hello”.
Reference count: It shows the number of times that a has been referenced. For now, it is 1.
Now on the stack, the reference to a (that is stored on the private heap) is stored. There exists a tool called a garbage collector. 
The garbage collector’s job is to delete the objects (on the private heap) that are no longer referenced, meaning, it deletes the 
objects whose reference count reached zero. This way the garbage collector frees up some memory space for the Python interpreter.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
7. Where should we use Python's multithreading, multiprocessing, and asyncio libraries?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
To answer this question, we need some background knowledge. We divide the operations that we want our Python code to do into two categories:

CPU-bound operations such as parsing, image processing, string manipulation, and algorithms involving heavy calculations. 
We can use parallelism for these types of operations. Basically, parallel programming is when we create different processes to divide a job among them and they all do the job simultaneously. Each process has its own GIL, Python interpreter, memory space, and state information. In Python, we use the multiprocessing library to achieve parallelism.

IO-bound operations such as sending HTTP requests, querying data from databases, sending emails, and opening a file. We use concurrency for these operations. In Python, we can handle these operations using multithreading and asyncio libraries. Note that parallelism requires more resources than concurrency.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
8. How does importing in Python work?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
To answer this senior Python developer interview question, assume we have a directory called dir, inside which we have a Python script. 
When you import a module in this Python script, the Python interpreter tries to find your imported module in this order:

It searches among other Python scripts inside the dir directory.
Then it goes over the list of the directories that are set using the PYTHONPATH environment variable.
Last, it searches through the default directories where Python files were installed. 
For example, 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python311\\Lib'






--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
9. What is a closure in Python?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A closure is an inner/nested function that keeps the data regarding its enclosing scope even after the closure is called.
 To illustrate your answer to this interview question, you can provide this scenario for using closures for lazy evaluation:

import math

def multiply():
    l = []
    def closure(num):
        l.append(num)
        return math.prod(l)
        
    return closure
    
current_mult = multiply()
print(current_mult(2)) # 2

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
10. How do you write scalable code in Python?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This is one of the most impactful and advanced senior Python interview questions. Scalability means creating services and microservice
s that can handle millions of users (large loads) without going down. This is a challenge that must be handled properly and writing scalable
 code is one way to make our service scalable.

Please be aware that we have to take into account many other components of creating a scalable project, such as systems design, DBMS,
 and infrastructure.

Below you can find some concepts of writing scalable code for Python Core to include in your answer to this interview question.

Use efficient data structures. For example, the time complexity of in operator is different depending on what iterable it has been used on.

On list/tuple 🡪 O(n) time complexity.
On dictionary/set 🡪 O(1) is the average case and O(n) is the worst case.
In the examples above, n is the length of the iterable.

Use parallelism. Dividing and running a CPU-bound operation using different processes can be a solution to boost the speed.

Design a distributed system. In a distributed system there are different machines that communicate with each other to do a job.
 Using libraries like Apache Spark or Ray can be a good approach for scalability.

Use caching. Assume there is an image that requires heavy processing and this image must be sent to many users. 
To address such requirements, we can process this image only once and cache/store the processed version in a variable. This way whenever we want this processed image, we can just make use of that variable and avoid processing the image again.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CHATGPT
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1- What is the Global Interpreter Lock (GIL) in Python?
Answer: The GIL is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecode at once.


2- Explain the differences between Python 2 and Python 3.
Answer: Python 3 introduced several syntax and feature changes, including print function, division behavior, Unicode support, and more.

3- What is a virtual environment in Python?
Answer: A virtual environment is an isolated Python environment that allows you to install and manage dependencies for a 
project independently of the system-wide Python installation.


4- How does memory management work in Python?
Answer: Python uses a private heap space for memory management. The memory manager handles allocation and deallocation,
 and the garbage collector manages reference counting and cyclic garbage collection.


5- Explain the use of decorators in Python.
Answer: Decorators are a powerful feature that allows the modification of functions or methods using the @decorator syntax. 
They are often used for tasks like logging, timing, and access control.


6- What are generators in Python?
Answer: Generators are functions that allow you to iterate over a potentially large set of data without loading the entire
 dataset into memory at once. They use the yield statement to produce a sequence of values.


7- Describe the difference between __str__ and __repr__ methods.
Answer: __str__ is called by the str() built-in function and should return a user-friendly string representation. 
__repr__ is called by the repr() built-in function and should return an unambiguous string representation for developers.


8- What is the purpose of the if __name__ == "__main__": statement in Python scripts?
Answer: It allows a script to be used both as an importable module and as a standalone script. Code within this
 block only runs if the script is executed directly, not when imported as a module.


9- How does exception handling work in Python?
Answer: Exceptions are raised when an error occurs in a Python program. The try, except, else, 
and finally blocks provide a structured way to handle and respond to these errors.


10 - Explain the concept of duck typing in Python.
Answer: Duck typing is a programming concept where the type or class of an object is less important than the methods it defines. If an object walks like a duck and quacks like a duck, then it's a duck, regardless of its actual type.



11 - What is the Global Interpreter Lock (GIL) in Python, and how does it impact multi-threaded programs?
Answer: The GIL is a mutex that allows only one thread to execute Python bytecode at a time. 
This can impact the performance of multi-threaded programs as only one thread can execute Python instructions simultaneously.


12- Explain the purpose of the __init__ method in Python classes.
Answer: __init__ is a special method in Python classes used for initializing object attributes. 
It is called automatically when an object is created from the class.


13 - How does Python's garbage collection work, and when does it occur?
Answer: Python's garbage collector uses a combination of reference counting and a cyclic garbage collector. 
It automatically identifies and reclaims memory occupied by objects with no references.


14 - Describe the purpose of the *args and **kwargs syntax in function definitions.
Answer: *args allows a function to accept a variable number of positional arguments, while **kwargs allows it to 
accept a variable number of keyword arguments.


15 - What is the purpose of the with statement in Python?
Answer: The with statement is used for resource management. It ensures that a certain block of code is executed with a 
particular context, and resources are properly acquired and released.


16 - Explain the difference between shallow copy and deep copy in Python.
Answer: Shallow copy creates a new object but does not create new objects for nested elements. Deep copy creates a completely independent copy, including copies of all nested objects.


17 - How does Python's asyncio library facilitate asynchronous programming?
Answer: asyncio provides a framework for writing asynchronous code using coroutines, allowing non-blocking I/O operations and efficient multitasking.


18 - What is the purpose of the __slots__ attribute in a Python class?
Answer: __slots__ is used to explicitly declare the attributes a class can have, limiting the attribute names and reducing memory usage.


19 - Explain the Global, Local, and Enclosing scope in Python.
Answer: Global scope refers to the outermost scope, local scope is within a function, and enclosing scope is for nested functions. 
Python follows the LEGB (Local, Enclosing, Global, Built-in) scope resolution rule.


20 - How does Python handle default arguments in function definitions?
Answer: Default arguments are specified in the function definition, and if a value is not provided during the function call,
 the default value is used.



--------------------------------------------------------------------------------------------------------------------
THREADING AND MULTITHREADING
--------------------------------------------------------------------------------------------------------------------

Multithreading in Python refers to the concurrent execution of multiple threads within the same process. Threads are lightweight sub-processes that enable programs to perform multiple tasks simultaneously, making efficient use of available resources. 

Here's an overview of multithreading in Python:

Threading Module:

Python's threading module provides a high-level interface for working with threads.

It allows you to create and manage threads using classes like Thread and functions like Thread.start() and Thread.join().

Creating Threads:
You can create a new thread by instantiating the Thread class and passing a target function to execute concurrently.
The target function typically encapsulates the task that the thread will perform.

Example:

import threading

def worker():
    print("Thread is executing")

thread = threading.Thread(target=worker)
thread.start()

Thread Synchronization:
When multiple threads access shared resources concurrently, it can lead to data corruption or race conditions.
Thread synchronization mechanisms such as locks, semaphores, and conditions are used to coordinate access to shared resources and prevent conflicts.


Example using Lock:


import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        counter += 1

threads = []
for _ in range(10):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Counter:", counter)

Global Interpreter Lock (GIL):
In Python, the Global Interpreter Lock (GIL) ensures that only one thread executes Python bytecode at a time, effectively serializing execution of threads.
As a result, multithreading in Python may not fully utilize multiple CPU cores for CPU-bound tasks.
However, multithreading is still useful for I/O-bound tasks where threads spend a significant amount of time waiting for I/O operations to complete.

Threading vs. Multiprocessing:

Python's threading module is suitable for I/O-bound tasks and concurrent I/O operations, such as network requests or file I/O. For CPU-bound tasks that require significant computation, the multiprocessing module is often preferred, as it bypasses the GIL and allows true parallel execution using separate processes.

Overall, multithreading in Python allows for concurrent execution of tasks, making programs more responsive and efficient, especially for I/O-bound operations. However, it's essential to be mindful of thread safety and synchronization when working with shared resources in a multithreaded environment.

 
--------------------------------------------------------------------------------------------------------------------
GO VS PYTHON IN CONCURRENCY
--------------------------------------------------------------------------------------------------------------------


Concurrency support in Go and Python differs in several key aspects, including concurrency models, language constructs, and performance 
characteristics. Here's a comparison of Go and Python concurrency support:

Concurrency Model:

Go: Go uses a CSP (Communicating Sequential Processes) concurrency model, inspired by the CSP language developed by Tony Hoare. Goroutines 
communicate via channels, which provide a safe and efficient way to share memory by communicating.
Python: Python supports both thread-based concurrency using the threading module and process-based concurrency using the multiprocessing module. 
Python's threading module uses threads and locks for synchronization, while the multiprocessing module spawns separate processes.
Goroutines vs. Threads:

Go: Goroutines are lightweight user-space threads managed by the Go runtime. They have minimal overhead and can be created and scheduled efficiently.
 Goroutines are multiplexed onto a smaller number of operating system threads by the Go runtime.
Python: Threads in Python are managed by the operating system and are typically heavier than Goroutines. Python threads are subject to the Global 
Interpreter Lock (GIL), limiting true parallelism in CPU-bound tasks.
Channels vs. Locks:

Go: Goroutines communicate via channels, which provide a type-safe way to send and receive data between concurrent operations. Channels encourage 
communication through data sharing rather than shared memory and help prevent race conditions.
Python: Python's threading module relies on locks (mutexes) and other synchronization primitives for coordinating access to shared resources among
 threads. While locks can prevent race conditions, they can also lead to deadlocks and performance bottlenecks if not used carefully.
Performance:

Go: Go's lightweight Goroutines and efficient scheduler make it well-suited for concurrent and parallel programming. Go's concurrency model 
allows for scalable and efficient utilization of CPU cores, particularly for I/O-bound and CPU-bound tasks.
Python: Python's GIL limits the scalability of multithreading for CPU-bound tasks. While Python's threading module is suitable for I/O-bound
 tasks, such as network I/O or file I/O, it may not fully utilize multiple CPU cores due to the GIL.


--------------------------------------------------------------------------------------------------------------------
NAMESPACE
--------------------------------------------------------------------------------------------------------------------

In Python, namespaces refer to containers or scopes where names (variables, functions, classes, etc.) are created and stored. 
Namespaces help organize and manage the identifiers used in a Python program to avoid conflicts and provide a systematic way to access different elements.

There are several types of namespaces in Python:

Built-in Namespace: This namespace contains all the built-in names provided by the Python interpreter. These names are always available without the need for any import statements. Examples include built-in functions like print(), len(), and built-in types like int, str, list, etc.

Global Namespace: The global namespace refers to the scope at the top level of a Python module or script. Names defined at this level are accessible throughout the entire module or script.

Local Namespace: Each function or method call in Python creates its own local namespace. This namespace contains the names defined within the function or method and is accessible only within that function or method.

Module Namespace: Every Python module has its own namespace, which serves as the global namespace for all the code within that module.

Class Namespace: Each class in Python defines its own namespace, which contains attributes and methods specific to that class.

Enclosing Scope: Assume we have a function called outer which has a nested function. Enclosing scope (or nonlocal scope) is
 the area within the body of outer function.

Namespaces are crucial for resolving names during variable lookup. When you reference a name in Python, the interpreter searches for that name in the local namespace first, then in the enclosing (non-local) namespaces (like the module or class namespace), and finally in the built-in namespace.

Understanding namespaces is essential for managing variable scope, avoiding naming conflicts, and writing clear and maintainable Python code.



--------------------------------------------------------------------------------------------------------------------
MEMORY MANAGEMENT in PYTHON
--------------------------------------------------------------------------------------------------------------------
Python has a private heap space that stores all the objects. The Python memory manager regulates various aspects of this heap, such as sharing, caching, segmentation, and allocation. The user has no control over the heap; only the Python interpreter has access.


In Python, memory cleanup is managed automatically by the Python interpreter's memory management system, which includes a component called the garbage collector. Python uses a technique called reference counting along with a cycle-detecting garbage collector to reclaim memory occupied by objects that are no longer in use.

Here's a brief overview of how memory cleanup works in Python:

Reference Counting: Python objects have a reference count associated with them. Every time an object is referenced, its reference count is incremented. When a reference to an object goes out of scope or is explicitly deleted, the reference count is decremented. When the reference count reaches zero, meaning there are no more references to the object, the memory occupied by that object is deallocated.

Garbage Collection: In addition to reference counting, Python also has a garbage collector that is responsible for cleaning up cyclic references, which are situations where two or more objects reference each other in a circular manner. This can prevent objects from being garbage collected even when their reference count drops to zero. The garbage collector periodically runs to identify and collect such cyclic references, freeing up the memory they occupy.

Automatic Memory Management: Python handles memory management automatically, so developers typically don't need to explicitly deallocate memory or perform manual memory cleanup. Objects are automatically garbage collected when they are no longer reachable, meaning there are no references to them from the main program or any active data structures.

It's worth noting that while Python's automatic memory management system is convenient, it's important to be mindful of memory usage, especially in long-running applications or when dealing with large datasets, to avoid memory leaks or excessive memory consumption. Properly managing object references and using appropriate data structures can help optimize memory usage in Python programs.


----------------------------------------------------------------------------------------------------------------------------------------
NUMPY OVER LISTS
----------------------------------------------------------------------------------------------------------------------------------------
A NumPy array is a central data structure in the NumPy library, which is a powerful Python library used for numerical computing. NumPy arrays are similar to Python lists but offer several advantages, especially for numerical computations. Here are some key characteristics of NumPy arrays:

USAGE:
import numpy as np

# Create a 1D NumPy array from a Python list
arr1d = np.array([1, 2, 3, 4, 5])

# Create a 2D NumPy array (matrix) from a nested Python list
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr1d)
print(arr2d)

What Advantage Does the Numpy Array Have over a Nested List?

NumPy arrays offer several advantages over nested Python lists:

A - Performance: 
NumPy arrays are implemented in C and optimized for performance, whereas nested lists are implemented in Python and are generally slower for numerical computations. NumPy's array operations are vectorized, meaning they operate on entire arrays at once, which can significantly speed up computations compared to iterating over nested lists.

B - Memory Efficiency: 
NumPy arrays are more memory efficient than nested lists. NumPy arrays store data in contiguous memory blocks, whereas nested lists store references to objects scattered across memory. This leads to less overhead and better cache locality with NumPy arrays, resulting in more efficient memory usage.

C - Convenience: 
NumPy provides a wide range of mathematical functions and operations specifically designed for array manipulation. These functions are optimized for performance and are easy to use with NumPy arrays. In contrast, performing similar operations on nested lists requires writing custom code or using nested loops, which can be less efficient and more error-prone.

D - Broadcasting: 
NumPy arrays support broadcasting, which allows for arithmetic operations between arrays of different shapes. This can greatly simplify code and eliminate the need for explicit looping or reshaping of arrays.

E - Integration with Libraries:
NumPy arrays seamlessly integrate with many scientific computing libraries and tools, such as SciPy, pandas, and Matplotlib. This makes NumPy arrays a natural choice for numerical computations and data analysis tasks in Python.

Overall, NumPy arrays are a powerful and efficient data structure for numerical computations in Python, offering superior performance, memory efficiency, and convenience compared to nested lists.


7. Are Arguments in Python Passed by Value or by Reference?
Arguments are passed in python by a reference. This means that any changes made within a function are reflected in the original object.


8 -How Would You Generate Random Numbers in Python?
To generate random numbers in Python, you must first import the random module. 

The random() function generates a random float value between 0 & 1.

> random.random()

The randrange() function generates a random number within a given range.

Syntax: randrange(beginning, end, step)

Example - > random.randrange(1,10,2)

----------------------------------------------------------------------------------------------------------------------------------------
LIST INSIDE A TUPLE
----------------------------------------------------------------------------------------------------------------------------------------



In Python, the immutability of a tuple refers to the tuple itself, not its elements. This means that once a tuple is created, you cannot change, add, or remove its elements. However, if the elements of a tuple are mutable objects (such as lists), you can modify those objects.

For example:

my_tuple = ([1, 2, 3], 4, 5)

In this case, my_tuple contains a list [1, 2, 3] as its first element. Although you cannot change the tuple itself, you can modify the list inside the tuple:

my_tuple[0][0] = 100

print(my_tuple)  # Output: ([100, 2, 3], 4, 5)

However, you cannot reassign the entire tuple or change its length:

# This will raise an error
my_tuple[0] = [1, 2, 3, 4]

# This will also raise an error
my_tuple.append(6)
So, in summary, while you cannot directly modify the elements of a tuple (because it's immutable), if those elements are mutable objects, you can modify their internal state.

----------------------------------------------------------------------------------------------------------------------------------------
APPEND vs EXTEND:
----------------------------------------------------------------------------------------------------------------------------------------
- append() adds an element to the end of the list

- extend() adds elements from an iterable to the end of the list

----------------------------------------------------------------------------------------------------------------------------------------
WEBSOCKETS vs SOCKETIO
----------------------------------------------------------------------------------------------------------------------------------------

Socket.IO and WebSockets are both technologies used for real-time communication between a client (typically a web browser) and a server. They have some similarities but also some differences:

WebSockets:

Protocol: WebSockets provide a protocol that enables full-duplex communication channels over a single TCP connection. It offers a persistent connection between the client and server, allowing real-time data transfer in both directions.
Efficiency: WebSockets are generally more lightweight and efficient compared to other methods of real-time communication, such as long-polling or HTTP polling.
Standardized Protocol: WebSockets follow a standardized protocol defined by the WebSocket API, making it easier to implement and ensuring interoperability between different WebSocket libraries and frameworks.
Low-Level: WebSockets provide a low-level API for sending and receiving messages. Developers have control over the raw data sent over the WebSocket connection.
Browser Support: WebSockets are supported by most modern web browsers and are widely used in web applications for real-time features such as chat applications, live updates, and online gaming.
Socket.IO:

WebSocket Abstraction: Socket.IO is a library that provides an abstraction layer over WebSockets, along with fallback mechanisms such as long-polling or HTTP streaming for browsers that do not support WebSockets.
Additional Features: Socket.IO offers additional features beyond basic WebSocket functionality, such as room support, broadcasting, and automatic reconnection. It also supports various transports (WebSocket, HTTP long-polling, etc.) for maximum compatibility.
Real-Time Applications: Socket.IO is commonly used for building real-time web applications, including chat applications, collaborative editing tools, and real-time analytics dashboards.
Ecosystem: Socket.IO has a large and active ecosystem with support for various programming languages and frameworks, making it easy to integrate with different server-side technologies.
In summary, WebSockets provide a standardized protocol for real-time communication, while Socket.IO is a library built on top of WebSockets, providing additional features and fallback mechanisms for broader compatibility. The choice between them depends on the specific requirements of your project, such as browser support, desired features, and ease of implementation.


--------------------------------------------------------------------------------------------------------------------
*args vs **kwargs
--------------------------------------------------------------------------------------------------------------------

A-)     *args:

*args is used to pass a variable number of positional arguments to a function.
It allows you to accept any number of positional arguments in the function definition.
*args collects additional positional arguments into a tuple within the function.
You can name it anything, but *args is a common convention.

Usage: def fun(*args):

Example:
def sum_values(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_values(1, 2, 3))  # Output: 6


B-)     **kwargs:


**kwargs is used to pass a variable number of keyword arguments to a function.
It allows you to accept any number of keyword arguments in the function definition.
**kwargs collects additional keyword arguments into a dictionary within the function, where the keys are the argument names and the values are the corresponding argument values.
You can name it anything, but **kwargs is a common convention.

Usage: def fun(**kwargs):

Example:

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="John", age=30, city="New York")  
# Output:
# name: John
# age: 30
# city: New York
These constructs are particularly useful when you want to create functions that are flexible and can handle a varying number of arguments or keyword arguments. They are commonly used in situations where you want to create higher-order functions or wrapper functions that delegate work to other functions without knowing the specific arguments they will receive.

--------------------------------------------------------------------------------------------------------------------
Functions are first-class objects in Python
--------------------------------------------------------------------------------------------------------------------

The statement "Functions are first-class objects in Python" means that functions in Python are treated as first-class citizens or entities, just like any other data type such as integers, strings, or lists. This concept is a fundamental aspect of many programming languages, including Python, and it brings several implications:

Functions can be assigned to variables: You can assign a function to a variable, just like you can assign an integer or a string to a variable. For example:


USAGE:

def greet():
    return "Hello"

hello_function = greet
print(hello_function())  # Output: Hello



Functions can be passed as arguments: You can pass a function as an argument to another function. This allows for higher-order functions, which are functions that operate on other functions. 

For example:

USAGE:

def apply(func, value):
    return func(value)

def double(x):
    return x * 2

print(apply(double, 5))  # Output: 10


Functions can be returned from other functions: Functions can return other functions as return values. This enables the creation of factory functions or functions that generate other functions. For example:

USAGE:

def create_adder(n):
    def adder(x):
        return x + n
    return adder

add_5 = create_adder(5)
print(add_5(3))  # Output: 8
Functions can be stored in data structures: Functions can be stored in data structures such as lists, dictionaries, or tuples. This allows for dynamic manipulation of functions at runtime. For example:

USAGE:

def say_hello():
    print("Hello")

def say_goodbye():
    print("Goodbye")

function_list = [say_hello, say_goodbye]
for func in function_list:
    func()  # Output: Hello, Goodbye
In summary, treating functions as first-class objects in Python allows for more flexibility and expressive power in programming.
It enables functional programming paradigms, promotes code reusability, and facilitates the creation of more modular and maintainable code.



--------------------------------------------------------------------------------------------------------------------
DECORATORS
--------------------------------------------------------------------------------------------------------------------

Decorators are a powerful feature in Python that allow you to modify or extend the behavior of functions or methods without changing their implementation. Decorators are often used for adding functionality such as logging, authentication, or performance measurement to functions or methods.

In Python, a decorator is a function that takes another function as an argument, adds some functionality to it, and returns a new function. Decorators are typically used by placing the decorator's name prefixed with an @ symbol above the function or method definition.

Here's a simple example of a decorator:

USAGE:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

Output:
Something is happening before the function is called.
Hello!
Something is happening after the function is called.

In this example:

We define a decorator function my_decorator that takes another function func as an argument and defines a new function wrapper that adds some functionality before and after calling func.
We decorate the say_hello function by placing @my_decorator above its definition. This tells Python to apply the my_decorator function to the say_hello function.
When we call say_hello(), it actually calls the wrapper function created by the decorator, which in turn calls the original say_hello function along with the additional functionality.


----------------------------------------------------------------------------------------------------------------------------------------
.py and .pyc files
----------------------------------------------------------------------------------------------------------------------------------------

The .py and .pyc files are both related to Python code, but they serve different purposes:

.py File (Python Source Code):

- The .py extension is used for Python source code files.
- These files contain human-readable Python code written by developers.
- Python source code files are plain text files that can be opened and edited with any text editor or integrated development environment (IDE).
- When you write Python code in a .py file and execute it, the Python interpreter reads and executes the code directly.



.pyc File (Python Compiled Bytecode):

- The .pyc extension is used for Python compiled bytecode files.
- When Python executes a .py file, it compiles the source code into bytecode, which is a low-level representation of the Python code.
- The compiled bytecode is stored in .pyc files for future use.
- .pyc files are binary files that contain the bytecode representation of the corresponding .py source code file.
- Using .pyc files can speed up the execution of Python code because the bytecode can be executed directly without needing to recompile the source code.
- If a .pyc file is present and its modification time matches the corresponding .py file, Python will use the .pyc file instead of recompiling the source code.
- .pyc files are platform-independent, meaning they can be shared and executed on different platforms without needing to recompile the source code.

In summary, .py files contain human-readable Python source code, while .pyc files contain compiled bytecode generated from the source code. The Python interpreter can execute both .py and .pyc files, but using .pyc files can improve performance by avoiding the need to recompile the source code every time it is executed.

---------------------------------------------------------------------------------------------------------------------
NumPy:
---------------------------------------------------------------------------------------------------------------------

NumPy is a Python library used for working with arrays.

NumPy is a fundamental package for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.


Here's a more detailed explanation of its key features:

Arrays: NumPy's core feature is the ndarray, an N-dimensional array object that represents a collection of elements of the same type. These arrays can be created from Python lists or other sequences and support a variety of operations, including indexing, slicing, and reshaping.

Mathematical Functions: NumPy provides a comprehensive set of mathematical functions for performing arithmetic, trigonometric, exponential, logarithmic, and other mathematical operations on arrays. These functions are optimized for performance and can operate on entire arrays element-wise.

Linear Algebra: NumPy includes a rich set of functions for linear algebra operations, such as matrix multiplication, matrix inversion, eigenvalue computation, singular value decomposition, and more. These functions are essential for tasks like solving systems of linear equations and performing principal component analysis (PCA).

Random Number Generation: NumPy's random module provides functions for generating arrays of random numbers following various probability distributions. This is useful for tasks like simulation, modeling, and statistical analysis.

Memory Efficiency: NumPy arrays are memory efficient and allow for efficient storage and manipulation of large datasets. They also support various data types, including integers, floats, and complex numbers, allowing for versatile data representation.


---------------------------------------------------------------------------------------------------------------------
Pandas:
---------------------------------------------------------------------------------------------------------------------
Pandas is a Python library built on top of NumPy that provides high-level data structures and data manipulation tools for data analysis. It's particularly well-suited for working with structured or tabular data, such as time series data, CSV files, Excel spreadsheets, SQL databases, and more. Here's a detailed explanation of its features:

DataFrame: Pandas introduces the DataFrame data structure, which is a two-dimensional labeled data structure with columns of potentially different types. It resembles a spreadsheet or SQL table and allows for intuitive manipulation and analysis of data. Each column in a DataFrame is a Pandas Series, which shares many similarities with NumPy arrays.

Series: Pandas also provides the Series data structure, which is a one-dimensional labeled array capable of holding any data type (integers, strings, floats, Python objects, etc.). Series are used to represent a single column or row of data within a DataFrame.

Data Manipulation: Pandas offers powerful tools for data manipulation, including methods for filtering, selecting, sorting, grouping, merging, and reshaping data. It allows you to perform complex data transformations with just a few lines of code, making it ideal for data cleaning and preprocessing tasks.

Missing Data Handling: Pandas provides robust support for handling missing or NaN (Not a Number) values in data. It includes methods for detecting, removing, or filling missing data, making it easier to work with real-world datasets that may contain incomplete or inconsistent information.

Time Series Functionality: Pandas includes functionality for working with time series data, including date/time indexing, resampling, frequency conversion, and date/time arithmetic. This makes it a valuable tool for analyzing temporal data such as stock prices, weather data, and sensor readings.

Integration with Other Libraries: Pandas integrates seamlessly with other Python libraries for data analysis and visualization, such as NumPy, Matplotlib, SciPy, and scikit-learn. This allows for a comprehensive data analysis workflow where data can be easily manipulated, analyzed, and visualized using a combination of tools.

In summary, NumPy provides the foundation for numerical computing in Python, while Pandas builds on top of NumPy to offer powerful data analysis and manipulation tools, particularly for structured data. Together, they form the backbone of the Python data science ecosystem, enabling users to perform a wide range of tasks related to data analysis, manipulation, and visualization.

---------------------------------------------------------------------------------------------------------------------
list vs tuple vs set vs dictionary 
---------------------------------------------------------------------------------------------------------------------


A-] Use Cases:

List: Ordered collection of items where duplicates are allowed. Suitable for scenarios where you need to maintain the order of elements and allow duplicates.
Tuple: Similar to lists but immutable. Used when the collection of elements shouldn't change. Commonly used for fixed collections like coordinates, database records, etc.
Set: Unordered collection of unique elements. Useful when you need to perform operations like union, intersection, or difference on collections. Also handy for removing duplicates from a sequence.
Dictionary: Collection of key-value pairs. Suitable for scenarios where you need to store and retrieve data based on some unique identifier (the key). Commonly used for mappings.


B-] Speed, Performance, Memory:

List vs. Tuple: Lists are generally faster for mutable operations due to their dynamic resizing capability, but tuples offer better performance for immutable operations since they're fixed in size and can be optimized by the interpreter.
List vs. Set: Lists generally have slower lookup times compared to sets, especially for large datasets, because sets use hash tables for fast lookups. However, sets consume more memory than lists.
List vs. Dictionary: Lists are ordered and accessed by index, whereas dictionaries are accessed by keys. Retrieval by key in a dictionary is faster (on average) than searching by value in a list.


C-] Mutability vs. Immutability:

Mutable: Lists and dictionaries are mutable; their elements can be changed after creation.
Immutable: Tuples and sets are immutable; once created, their elements cannot be changed. However, note that while the elements of a tuple cannot be changed, if the elements are mutable (like lists), their internal state can be modified.
Immutability: Immutability works by ensuring that once an object is created, its state cannot be changed. In Python, immutable objects like tuples achieve this by not providing methods to modify their elements after creation.

Ways to Access Elements:
List and Tuple: Accessed by index. Lists and tuples support indexing and slicing operations.
Set: Elements are not accessed by index since sets are unordered. You can check for membership (in operator).
Dictionary: Accessed by keys. You provide the key to access the corresponding value.


Let's compare the ways to iterate over elements for lists, tuples, sets, and dictionaries in Python:

Lists:
Iteration Method: Iterating over a list is typically done using a for loop or list comprehensions.
Example:
python
Copy code
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
Tuples:
Iteration Method: Similar to lists, iterating over a tuple is done using a for loop or list comprehensions.
Example:
python
Copy code
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item)
Sets:
Iteration Method: Sets can be iterated over using a for loop. Since sets are unordered, the order of elements during iteration is not guaranteed to match the insertion order.
Example:
python
Copy code
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)
Dictionaries:
Iteration Method: Dictionaries can be iterated over using a for loop to iterate over keys, values, or key-value pairs. You can use methods like keys(), values(), or items() to specify the type of iteration.
Example:
python
Copy code
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Iterate over keys
for key in my_dict:
    print(key)

# Iterate over values
for value in my_dict.values():
    print(value)

# Iterate over key-value pairs
for key, value in my_dict.items():
    print(key, value)
    
Comparison:
Iterating over lists and tuples is straightforward and similar.
Sets are also straightforward to iterate over, but remember that they are unordered collections, so the order of elements during iteration may not match the insertion order.
Iterating over dictionaries provides flexibility to iterate over keys, values, or key-value pairs based on specific requirements.

In summary, the choice of which data structure to use for iteration depends on the specific needs of your program, such as the type of elements you need to iterate over and the desired iteration behavior (e.g., maintaining order or accessing key-value pairs). Lists and tuples are suitable for ordered collections, sets are suitable for unique unordered collections, and dictionaries are suitable for key-value mappings.




----------------------------------------------------------------------------------------------------------------
SOLID PRINCIPLES:
----------------------------------------------------------------------------------------------------------------

SOLID is an acronym for five design principles intended to make software designs more understandable, flexible, and maintainable

Single Responsibility Principle (SRP):
This principle states that a class should have only one reason to change, meaning that a class should have only one responsibility or job. If a class has multiple responsibilities, changes to one responsibility may necessitate changes to other parts of the class, leading to a lack of cohesion and increased complexity.

Open/Closed Principle (OCP):
The Open/Closed Principle suggests that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. In other words, you should be able to extend the behavior of a module without modifying its source code. This is typically achieved through the use of abstraction and polymorphism.

Liskov Substitution Principle (LSP):
The Liskov Substitution Principle states that objects of a superclass should be replaceable with objects of its subclass without affecting the correctness of the program. In other words, derived classes should be substitutable for their base classes without altering the desirable properties of the program. This principle ensures that inheritance is used correctly and that subclasses adhere to the contract established by the superclass.

Interface Segregation Principle (ISP):
The Interface Segregation Principle advocates for designing interfaces that are specific to the needs of the clients that use them. It suggests that no client should be forced to depend on methods it does not use. Instead of creating large interfaces with many methods, interfaces should be segregated into smaller, more focused ones, tailored to the requirements of the clients.

Dependency Inversion Principle (DIP):
The Dependency Inversion Principle suggests that high-level modules should not depend on low-level modules; both should depend on abstractions. Additionally, abstractions should not depend on details; rather, details should depend on abstractions. By relying on abstractions, rather than concrete implementations, the system becomes more flexible and easier to maintain.

These SOLID principles serve as guidelines to produce cleaner, more modular, and maintainable code. They promote good software design practices, enhance code readability, facilitate code reuse, and make systems easier to test and extend. Adhering to these principles can lead to more robust, flexible, and scalable software architectures.


----------------------------------------------------------------------------------------------------------------
ITERATORS AND GENERATORS:
----------------------------------------------------------------------------------------------------------------

In Python, iterators and generators are two powerful constructs that facilitate the handling of sequences of data. They both allow you to iterate over a sequence, but they have different implementations and use cases.


Iterators:
An iterator is an object that enables you to traverse a container, like a list or a dictionary, and access its elements one by one. It provides two essential methods:


__iter__(): Returns the iterator object itself. This method is called when the iterator is initialized.
__next__(): Returns the next element in the container. This method raises a StopIteration exception when there are no more elements to return.


list iterator example - 
list1 = [1,2,3]
iterator_list1 = iter(list1)
print(next(list1))    //1
print(next(list1))    //2
exception if next > len(list1)


Here's an example of an iterator:
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

my_iter = MyIterator([1, 2, 3, 4])
for item in my_iter:
    print(item)




Generators:
Generators are a simpler way to create iterators in Python. They are functions that use the yield keyword to return values one at a time. When a generator function is called, it returns a generator object that can be iterated over. Generators preserve the state of the function between calls, making it easy to pause and resume iteration.

Here's an example of a generator function:
def my_generator(data):
    for item in data:
        yield item

gen = my_generator([1, 2, 3, 4])
for item in gen:
    print(item)
Generators are particularly useful when dealing with large datasets or when you don't want to load an entire sequence into memory at once. They provide a memory-efficient way to iterate over large collections.

Key Differences:
Implementation: Iterators are implemented as classes with __iter__() and __next__() methods, while generators are implemented as functions with one or more yield statements.

Memory Usage: Generators are more memory-efficient than iterators because they yield values on the fly, whereas iterators may hold the entire sequence in memory.

Syntax: Generators use a more concise syntax with the yield keyword, while iterators require more boilerplate code to define the class and methods.

In summary, both iterators and generators enable you to iterate over sequences of data in Python, but generators provide a simpler and more memory-efficient way to achieve this, especially for large datasets.

----------------------------------------------------------------------------------------------------------------
CONTEXT MANAGERS 
----------------------------------------------------------------------------------------------------------------


In Python, a context manager is an object that enables you to manage resources, such as opening and closing files, acquiring and releasing locks, or managing database transactions, in a controlled and predictable manner. Context managers are typically used with the with statement, which ensures that resources are properly cleaned up after they are no longer needed, even if an exception occurs during their use.

Context managers can be implemented in two ways in Python:

Class-based Context Managers:
A class-based context manager is implemented by defining a class with __enter__() and __exit__() methods. The __enter__() method is called when entering the with block, and it returns the resource that will be managed. The __exit__() method is called when exiting the with block, and it is responsible for cleaning up the resource, even in the presence of exceptions.

Here's a simple example of a class-based context manager for opening and closing a file:


class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

# Example usage of the FileContextManager
with FileContextManager('example.txt', 'w') as file:
    file.write('Hello, world!')


Decorator-based Context Managers:
A decorator-based context manager is implemented using the contextlib module's contextmanager decorator. This approach is more concise and is often used when defining simple context managers.

Here's the same example using the contextmanager decorator:

from contextlib import contextmanager
@contextmanager
def open_file(filename, mode):
    file = None
    try:
        file = open(filename, mode)
        yield file
    finally:
        if file:
            file.close()

# Example usage of the open_file context manager
with open_file('example.txt', 'w') as file:
    file.write('Hello, world!')


Both class-based and decorator-based context managers achieve the same goal of managing resources efficiently and ensuring proper cleanup. The choice between the two approaches depends on the complexity of the context manager and personal preference. Context managers are an essential feature of Python for resource management, especially in scenarios where resources need to be properly cleaned up to avoid resource leaks and ensure the reliability of the code.


----------------------------------------------------------------------------------------------------------------
LAMDA FUNCTIONS
----------------------------------------------------------------------------------------------------------------

Lambda functions, also known as anonymous functions, are small, inline functions in Python that are defined using the lambda keyword. They are typically used for simple operations where defining a named function is unnecessary or cumbersome.


lambda arguments: expression

lambda ==> keyword for defining lambda function
arguments ==> any number of input paraemters
expression ==> single expression allowed which evaluates the input parameters

test = lambda x,y:x+y
print(test(2,3))

Lambda functions can have multiple arguments, but they can only have one expression. This expression is evaluated and returned when the lambda function is called with its arguments.


Lambda functions are commonly used in conjunction with built-in functions like map(), filter(), and sorted() to perform operations on iterables like lists, tuples, or dictionaries. For example:

python
Copy code
# Using lambda function with map()
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Using lambda function with filter()
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

# Using lambda function with sorted()
names = ['Alice', 'Bob', 'Charlie', 'David']
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)  # Output: ['Bob', 'Alice', 'David', 'Charlie']
Lambda functions are particularly useful in situations where you need a short, throwaway function, especially when passing a function as an argument to another function or when using functional programming paradigms in Python. However, it's essential to use them judiciously and consider readability and maintainability when deciding whether to use lambda functions or regular named functions.

----------------------------------------------------------------------------------------------------------------
POLYMORPHISM & INHERITANCE
----------------------------------------------------------------------------------------------------------------

Polymorphism is the ability of different objects to respond to the same message or method call in different ways. It allows objects of different classes to be treated as objects of a common superclass, providing a unified interface for different types of objects.

There are two main types of polymorphism:

Compile-time Polymorphism (Method Overloading):
Method overloading allows multiple methods in a class to have the same name but different parameters. Python does not support method overloading in the traditional sense because it does not perform static type checking. However, you can achieve similar behavior by using default parameter values or variable-length argument lists.

In Python, method overloading is not supported in the traditional sense as in statically-typed languages like Java or C++. However, you can achieve similar behavior through various techniques such as using default parameter values or variable-length argument lists. Let's illustrate both approaches with Python snippets.

Approach 1: Using Default Parameter Values
In this approach, you can define a method with default parameter values and provide multiple method signatures based on the number and types of parameters. When calling the method, Python dynamically dispatches the call based on the arguments provided.


class Calculator:
    def add(self, a, b=0):
        return a + b
    
    def multiply(self, a, b=1):
        return a * b

# Usage
calc = Calculator()

print(calc.add(2, 3))        # Output: 5
print(calc.add(2))            # Output: 2 (default value for b is used)
print(calc.multiply(3, 4))    # Output: 12
print(calc.multiply(3))       # Output: 3 (default value for b is used)
In this example, the add() method is overloaded to accept either one or two arguments, while the multiply() method is overloaded to accept either one or two arguments as well. Default parameter values are used to define multiple method signatures.

Approach 2: Using Variable-Length Argument Lists
Python allows you to define functions that accept a variable number of arguments using *args and **kwargs syntax. You can use this feature to simulate method overloading by defining a single method that can handle different numbers and types of arguments.


class Calculator:
    def add(self, *args):
        return sum(args)
    
    def multiply(self, *args):
        result = 1
        for arg in args:
            result *= arg
        return result

# Usage
calc = Calculator()

print(calc.add(2, 3))            # Output: 5
print(calc.add(2, 3, 4))         # Output: 9
print(calc.multiply(3, 4))       # Output: 12
print(calc.multiply(3, 4, 5))    # Output: 60
In this example, both the add() and multiply() methods accept a variable number of arguments using *args. They can handle different numbers of arguments and perform the respective operations.

While these approaches provide flexibility similar to method overloading, it's essential to use them judiciously and consider readability and maintainability when deciding whether to use them.



Run-time Polymorphism (Method Overriding):
Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. This allows objects of the subclass to replace the behavior of the method inherited from the superclass with their own implementation. Method overriding enables dynamic binding, where the appropriate method implementation is selected at runtime based on the actual object type.



OPERATOR OVERLOADING

Operator overloading in Python refers to the ability to define custom behavior for built-in operators such as +, -, *, /, ==, <, >, etc. This allows objects of a user-defined class to use these operators, enabling more natural and intuitive syntax for operations involving those objects.

Python provides special methods, often called magic methods or dunder (double underscore) methods, for operator overloading. These methods are called automatically when certain operators are used with objects of a class.

Here's a brief overview of some commonly used dunder methods for operator overloading:

__add__(self, other): Defines behavior for the addition operator +.
__sub__(self, other): Defines behavior for the subtraction operator -.
__mul__(self, other): Defines behavior for the multiplication operator *.
__truediv__(self, other): Defines behavior for the division operator /.
__eq__(self, other): Defines behavior for the equality operator ==.
__lt__(self, other): Defines behavior for the less than operator <.
__gt__(self, other): Defines behavior for the greater than operator >.
__str__(self): Defines behavior for converting objects to strings using str().
__repr__(self): Defines behavior for converting objects to strings for representation using repr().
__len__(self): Defines behavior for the len() function.

Here's an example demonstrating operator overloading in Python:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Usage
p1 = Point(1, 2)
p2 = Point(3, 4)

# Using the '+' operator to add two Point objects
result = p1 + p2
print(result)  # Output: (4, 6)
In this example, we define a Point class with an __add__ method, which defines the behavior for the addition operator +. When we use the + operator with two Point objects (p1 and p2), Python internally calls the __add__ method of the Point class, which adds the corresponding x and y coordinates of the two points and returns a new Point object with the result.

Operator overloading is a powerful feature in Python that allows you to write expressive and concise code by defining custom behavior for operators in your classes. However, it's essential to use it judiciously and follow the principle of least astonishment to ensure that your code remains readable and maintainable.




Inheritance:

Inheritance is a mechanism in OOP that allows a class (subclass or derived class) to inherit properties and behavior (methods and attributes) from another class (superclass or base class). The subclass can extend or modify the functionality of the superclass while retaining its existing features.

Key concepts related to inheritance include:

Superclass (Base Class):
The class whose properties and behavior are inherited by another class. It serves as a template for creating subclasses.

Subclass (Derived Class):
The class that inherits properties and behavior from a superclass. It can extend or override the functionality of the superclass.

Inheritance Hierarchy:
Inheritance can be hierarchical, with multiple levels of subclasses inheriting from their respective superclasses. This forms a tree-like structure, where each subclass inherits from its direct superclass and indirectly from all of its ancestors.

Method Overriding:
Subclasses can override methods inherited from their superclass to provide specialized behavior. This allows for customization and flexibility in the behavior of objects.

In Python, inheritance is achieved by specifying the superclass(es) in parentheses after the subclass name in the class definition. For example:

python
Copy code
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Dog barks")

class Cat(Animal):  # Cat inherits from Animal
    def speak(self):
        print("Cat meows")

# Example usage
dog = Dog()
dog.speak()  # Output: Dog barks

cat = Cat()
cat.speak()  # Output: Cat meows
In this example, both Dog and Cat classes inherit from the Animal class. Each subclass overrides the speak() method to provide its own implementation of animal sound. When speak() is called on instances of Dog and Cat, they respond differently based on their specific implementations, demonstrating polymorphism.

----------------------------------------------------------------------------------------------------------------
 Python interpreter and the Python Virtual Machine (PVM)
----------------------------------------------------------------------------------------------------------------


The Python interpreter and the Python Virtual Machine (PVM) are indeed two distinct components, although they work closely together to execute Python code.

Python Interpreter:
The Python interpreter is responsible for several tasks, including lexical analysis, parsing, bytecode generation, and dynamic execution of Python code. It processes the source code of Python programs, translates them into bytecode, and coordinates the execution of these bytecode instructions.
Python Virtual Machine (PVM):
The Python Virtual Machine (PVM) is the runtime environment where bytecode instructions are executed. It provides an abstraction layer between the Python code and the underlying hardware and operating system. The PVM interprets bytecode instructions and manages resources such as memory allocation, object lifecycle, and dynamic type checking during program execution.
While the Python interpreter handles the initial stages of code processing, such as parsing and bytecode generation, the PVM takes over during runtime to execute the generated bytecode. These two components work together seamlessly to provide the execution environment for Python programs.


----------------------------------------------------------------------------------------------------------------
OOP PYTHON private protected 
----------------------------------------------------------------------------------------------------------------


https://stackoverflow.com/questions/20261517/inheritance-of-private-and-protected-methods-in-python

Python has no privacy model, there are no access modifiers like in C++, C# or Java. There are no truly 'protected' or 'private' attributes.

Names with a leading double underscore and no trailing double underscore are mangled to protect them from clashes when inherited. Subclasses can define their own __private() method and these will not interfere with the same name on the parent class. Such names are considered class private; they are still accessible from outside the class but are far less likely to accidentally clash.

Mangling is done by prepending any such name with an extra underscore and the class name (regardless of how the name is used or if it exists), effectively giving them a namespace. In the Parent class, any __private identifier is replaced (at compilation time) by the name _Parent__private, while in the Child class the identifier is replaced by _Child__private, everywhere in the class definition.



class Parent(object):
    def _protected(self):
        pass

    def __private(self):
        pass


class Child(Parent):
    def foo(self):
        self._protected()

    def bar(self):
        self._Parent__private()


Private name mangling: When an identifier that textually occurs in a class definition begins with two or more underscore characters and does not end in two or more underscores, it is considered a private name of that class. Private names are transformed to a longer form before code is generated for them. The transformation inserts the class name, with leading underscores removed and a single underscore inserted, in front of the name. For example, the identifier __spam occurring in a class named Ham will be transformed to _Ham__spam. This transformation is independent of the syntactical context in which the identifier is used.


----------------------------------------------------------------------------------------------------------------
setup.py usage
----------------------------------------------------------------------------------------------------------------


setup.py is a script used in Python projects to define the metadata and configuration options for distributing a Python package. It typically contains information such as the package name, version, author, dependencies, and other details necessary for package installation and distribution.

The primary purposes of setup.py are:

Package Metadata: It defines metadata about the package such as its name, version, author, description, license, and other relevant information. This metadata helps users understand what the package does and who maintains it.

Dependencies: It specifies the dependencies required by the package to run correctly. Dependencies can be other Python packages that need to be installed for the package to work properly.

Installation: It provides instructions for installing the package using tools like pip or easy_install. This includes specifying the Python modules and packages that should be included in the distribution.

Distribution: It defines how the package should be distributed, including which files should be included in the distribution package and how it should be packaged (e.g., source distribution, built distribution, wheel).

Custom Commands: It allows for the definition of custom commands that can be run during the installation process. This can include tasks such as compiling source files, generating documentation, or running tests.

Here's a basic example of a setup.py script:


from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0.0",
    author="John Doe",
    author_email="john@example.com",
    description="A sample Python package",
    long_description="A longer description of the package",
    url="https://github.com/example/mypackage",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
This setup.py script defines a simple Python package called "mypackage" with version 1.0.0. It specifies the author, description, dependencies (numpy and requests), and other relevant information. When users want to install or distribute this package, they can use pip along with the setup.py script to handle the process.

----------------------------------------------------------------------------------------------------------------
pip vs pep
----------------------------------------------------------------------------------------------------------------

pip and PEP (Python Enhancement Proposal) serve different purposes in the Python ecosystem:

pip(Pip Installs Packages):

pip is a package manager for Python that allows users to install and manage Python packages from the Python Package Index (PyPI) or other package indexes. It simplifies the process of installing, upgrading, and uninstalling Python packages and their dependencies.
pip is a command-line tool that comes bundled with Python distributions since Python 3.4 and is widely used by Python developers and system administrators.


PEP (Python Enhancement Proposal):

PEPs are design documents that provide information to the Python community or describe a new feature for Python. They are the primary mechanism for proposing major changes to the Python language, its standard library, or other aspects of the Python ecosystem.
PEPs follow a specific format and are assigned unique numbers. They undergo review and discussion within the Python community before being accepted or rejected. Accepted PEPs become part of the official Python documentation and influence the evolution of the language.
PEPs cover a wide range of topics, including language syntax, standard library modules, development processes, and community guidelines.
In summary, pip is a package manager used for installing and managing Python packages, while PEPs are documents used to propose and discuss changes or enhancements to the Python language and ecosystem.




https://www.interviewkickstart.com/blog/interview-questions/python-scripting-interview-questions



When you import modules in Python, if there are conflicts where multiple modules define the same function name, Python uses a method called "namespace resolution" to determine which function to use.

Here's how it works:

Qualified Name Resolution: You can explicitly specify which function you want to use by prefixing the function name with the module name. For example:

python
Copy code
import my_module
import math

# Using function from my_module
my_module.function_name()

# Using function from math module
math.function_name()
Import Alias: You can import one or both modules with an alias to avoid naming conflicts. For example:

python
Copy code
import my_module as my
import math as m

# Using function from my_module
my.function_name()

# Using function from math module
m.function_name()
Selective Import: You can import specific functions from each module and use them directly, again avoiding naming conflicts. For example:

python
Copy code
from my_module import function_name as my_function
from math import function_name as math_function

# Using function from my_module
my_function()

# Using function from math module
math_function()
Last Import Wins: If you import both modules without aliasing and both define a function with the same name, the function defined in the module that was imported last will overwrite the previous definition. In this case, only the function from the last imported module will be accessible using its name. For example:

python
Copy code
from my_module import function_name
from math import function_name

# Only the function from math module is accessible
function_name()
To avoid confusion and maintain code clarity, it's generally recommended to use qualified names, import aliases, or selective imports when dealing with potential naming conflicts. This makes it clear which function you are using and helps prevent unexpected behavior due to name collisions.