
### Logease

**Logease** is a lightweight Python library designed to simplify and enhance logging by eliminating the need for traditional loggers. With  **Logease** , you can effortlessly integrate logging into your applications using decorators and modules. The library leverages the Singleton pattern to ensure that your logging system is efficient, centralized, and easy to manage.

---

#### Key Features:

* **Singleton Logger** : Initialize your logger once and use it throughout your application.
* **Decorator Support** : Easily add logging to your functions with the `@log_wrapper` decorator.
* **Modular Design** : Use the `Logger` module to customize and extend logging capabilities as needed.
* **Minimalist Approach** : Focus on your code, not the logging implementation.

---

**Logease** aims to streamline the logging process, making it more intuitive and less intrusive. Say goodbye to the clutter of traditional loggers and embrace a cleaner, more modern approach with  **Logease** .


## Usage

### Basic Example

```
from logease.decorators import log_wrapper
from logease.modules import Logger

# Initialize the logger (singleton pattern)
logger = Logger()

@log_wrapper
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
logger = Logger(level="DEBUG", format="%(asctime)s - %(levelname)s - %(message)s")

logger.debug("This is a debug message")

```


### Using the Decorator

The `@log_wrapper` decorator automatically logs the entry, exit, and execution time of functions:

```
from logease.decorators import log_wrapper

@log_wrapper
def complex_calculation(x, y):
    # Complex calculations here
    return x + y

result = complex_calculation(10, 20)

```


## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.
