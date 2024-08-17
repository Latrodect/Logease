
# Logease

**Logease** is a lightweight Python library designed to simplify and enhance logging by eliminating the need for traditional loggers. With  **Logease** , you can effortlessly integrate logging into your applications using decorators and modules. The library leverages the Singleton pattern to ensure that your logging system is efficient, centralized, and easy to manage.

---

#### Key Features:

* **Singleton Logger** : Initialize your logger once and use it throughout your application.
* **Decorator Support** : Easily add logging to your functions and methods with various decorators.
* **Modular Design** : Use the `Logger` module to customize and extend logging capabilities as needed.
* **Detailed Logging** : Provides detailed logging options including function calls, execution times, exceptions, and parameter types.
* **JSON Logging** : Log details in JSON format for structured data.

---

**Logease** aims to streamline the logging process, making it more intuitive and less intrusive. Say goodbye to the clutter of traditional loggers and embrace a cleaner, more modern approach with  **Logease** .

## Installation

To install  **Logease** , use pip:

`pip install logease`


## Usage

### Basic Example

Initialize the logger and use it with a decorated function:

```
from logease.decorators import function_tracer
from logease.modules import Logger

@function_tracer()
def example_function(param):
    # Function logic here
    return f"Received {param}"

if __name__ == "__main__":
    logger.info("Starting application...")
    result = example_function("Logease")
    logger.info(f"Result: {result}")
    logger.info("Application finished.")


```


### Customizing the Logger

You can customize the logger by passing configurations to the `Logger` module:

```
from logease.modules import Logger

# Custom logger with specific settings
logger = Logger(level="DEBUG")

logger.debug("This is a debug message")

```


### Using Decorators

**Logease** provides several decorators for detailed logging:

* **`@input_output_tracer`** : Logs function calls with arguments and return values.
* **`@execution_time_tracer`** : Logs the execution time of functions.
* **`@exception_tracer`** : Logs any exceptions raised by functions.
* **`@param_type_tracer`** : Logs the types of function parameters.
* **`@detailed_tracer`** : Logs detailed function execution information including arguments, keyword arguments, return values, and exceptions.
* **`@as_json_tracer`** : Logs function execution details in JSON format.

Examples:

```
from logease.decorators import input_output_tracer, execution_time_tracer, exception_tracer

@input_output_tracer()
def add(a, b):
    return a + b

@execution_time_tracer()
def slow_function(a, b):
    time.sleep(2)
    return a + b

@exception_tracer()
def risky_function(x):
    return 1 / x

```


### Using with Classes

**Logease** also supports class-level logging:

```
from logease.decorators import class_method_tracer, constructor_tracer, property_getter_tracer

@constructor_tracer
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @class_method_tracer()
    def class_method(cls, a):
        return a * 2

    @property
    @property_getter_tracer("x")
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

```


## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.
