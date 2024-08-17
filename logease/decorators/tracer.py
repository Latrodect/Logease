import time
from functools import wraps

from logease.modules.logger import Logger

logger = Logger()

def function_tracer(level="INFO", format_string="{func_name} called with args: {args}"):
    """
    A decorator that logs the function call details, including its arguments and return value.
    This decorator wraps the provided function and logs the following information:
    - The name of the function being called.
    - The arguments (`args` and `kwargs`) passed to the function.
    - The value returned by the function or any exceptions raised.
    - The execution time of the function.
    - The module and file name where the function is defined.
    The logging is done using the Logger instance configured in the logease package.

    Args:
        level (str): The log level for logging function call details.
        format_string (str): A format string for logging messages.

    Returns:
        function: The wrapped function with added logging functionality.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            file_name = func.__code__.co_filename
            start_time = time.time()
            log_message = format_string.format(
                func_name=func.__name__,
                args=args,
                kwargs=kwargs
            )
            logger.info(f"{file_name} {log_message}")
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                execution_time = end_time - start_time
                logger.info(f"{func.__name__} returned {result} (Execution time: {execution_time:.4f}s)")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} raised an exception: {e}")
                raise

        return wrapper

    return decorator

def class_tracer(method):
    """
    A decorator that logs the details of class method calls, including arguments and return values.

    This decorator wraps a class method and logs:
    - The name of the method being called.
    - The arguments (`args` and `kwargs`) passed to the method.
    - The value returned by the method or any exceptions raised.

    Args:
        method (function): The class method to be decorated.

    Returns:
        function: The wrapped method with added logging functionality.

    Example:
        class MyClass:
            @class_tracer
            def my_method(self, a):
                return a + 1

        obj = MyClass()
        obj.my_method(5)
        # Logs:
        # [INFO] Calling method my_method with args (5,), kwargs {}
        # [INFO] Method my_method returned 6
    """
    def decorator(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            log_message = f"Calling method {method.__name__} with args {args}, kwargs: {kwargs}:"
            logger.info(log_message)
            try:
                result = method(self, *args, **kwargs)
                logger.log(f"Method {method.__name__} returned {result}")
                return result
            except Exception as e:
                logger.error(f"Method {method.__name__} raised an exception: {e}")
                raise
        return wrapper
    return decorator

def constructor_tracer(cls):
    """
    A decorator that logs details when an instance of the class is created.

    This decorator wraps the class constructor and logs:
    - The name of the class being instantiated.
    - The arguments (`args` and `kwargs`) passed to the constructor.
    - A message indicating that the instance has been created.

    Args:
        cls (type): The class to be decorated.

    Returns:
        type: A wrapped class with added logging functionality.

    Example:
        @constructor_tracer
        class MyClass:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        obj = MyClass(2, 3)
        # Logs:
        # [INFO] Creating instance of MyClass with args (2, 3), kwargs {}
        # [INFO] Instance of MyClass created
    """
    class Wrapped(cls):
        def __init__(self, *args, **kwargs):
            log_message = f"Creating instance of {cls.__name__} with args: {args}, kwargs: {kwargs}"
            logger.info(log_message)
            super().__init__(*args, **kwargs)
            logger.info(f"Instance of {cls.__name__} created")
    return Wrapped

def class_method_tracer(level="INFO"):
    """
    A decorator that logs details of class method calls, including arguments, return values, and any exceptions raised.

    This decorator wraps a class method and logs:
    - The name of the class method being called.
    - The arguments (`args` and `kwargs`) passed to the method.
    - The value returned by the method or any exceptions raised.

    Args:
        level (str): The log level to use for logging class method details. Default is "INFO".

    Returns:
        function: The wrapped class method with added logging functionality.

    Example:
        class MyClass:
            @class_method_tracer(level="DEBUG")
            def class_method(cls, a):
                return a * 2

        MyClass.class_method(10)
        # Logs:
        # [DEBUG] Calling class method class_method with args (10,), kwargs {}
        # [DEBUG] Class method class_method returned 20
    """
    def decorator(method):
        @wraps(method)
        def wrapper(cls, *args, **kwargs):
            log_message = f"Calling class method {method.__name__} with args: {args}, kwargs: {kwargs}"
            logger.log(log_message, level)
            try:
                result = method(cls, *args, **kwargs)
                logger.log(f"Class method {method.__name__} returned {result}", level)
                return result
            except Exception as e:
                logger.log(f"Class method {method.__name__} raised an exception: {e}", "ERROR")
                raise
        return wrapper
    return decorator

def property_getter_tracer(property_name, level="INFO"):
    """
    A decorator that logs details of property getter calls, including the property value.

    This decorator wraps a property getter method and logs:
    - The name of the property being accessed.
    - The value of the property being returned.

    Args:
        property_name (str): The name of the property being accessed.
        level (str): The log level to use for logging property access. Default is "INFO".

    Returns:
        function: The wrapped property getter with added logging functionality.

    Example:
        class MyClass:
            @property
            @property_getter_tracer("x", level="DEBUG")
            def x(self):
                return self._x

            @x.setter
            def x(self, value):
                self._x = value

        obj = MyClass()
        obj.x = 10
        print(obj.x)
        # Logs:
        # [DEBUG] Getting x
        # [DEBUG] x = 10
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            logger.log(f"Getting {property_name}", level)
            result = func(self, *args, **kwargs)
            logger.log(f"{property_name} = {result}", level)
            return result
        return wrapper
    return decorator
