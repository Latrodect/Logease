import time
import json
import traceback
from functools import wraps

from logease.modules.logger import Logger

logger = Logger()

def input_output_tracer(level="INFO", format_string="{func_name} called with args: {args}"):
    """
    A decorator that logs the function name, its arguments, and its return value.

    Parameters:
        level (str): The logging level (default is "INFO").
        format_string (str): The format string for the log message (default is "{func_name} called with args: {args}").

    Example:
        @input_output_tracer(level="DEBUG", format_string="{func_name} called with args: {args} and returned: {return_value}")
        def add(a, b):
            return a + b
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            logger.info(
                format_string.format(
                    func_name=func.__name__, args=args, return_value=result
                )
            )
            return result
        return wrapper
    return decorator


def execution_time_tracer(level="INFO", format_string="{func_name} took {elapsed_time:.4f} seconds"):
    """
    A decorator that logs the execution time of the function.

    Parameters:
        level (str): The logging level (default is "INFO").
        format_string (str): The format string for the log message (default is "{func_name} took {elapsed_time:.4f} seconds").

    Example:
        @execution_time_tracer(level="DEBUG")
        def slow_function(a, b):
            time.sleep(2)
            return a + b
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed_time = time.time() - start_time
            logger.info(
                format_string.format(func_name=func.__name__, elapsed_time=elapsed_time)
            )
            return result
        return wrapper
    return decorator


def exception_tracer(level="ERROR", format_string="{func_name} failed with exception: {exception}"):
    """
    A decorator that logs any exception raised by the function.

    Parameters:
        level (str): The logging level (default is "ERROR").
        format_string (str): The format string for the log message (default is "{func_name} failed with exception: {exception}").

    Example:
        @exception_tracer(level="ERROR")
        def risky_function(x):
            return 1 / x
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(format_string.format(func_name=func.__name__, exception=e))
                raise
        return wrapper
    return decorator


def param_type_tracer(level="DEBUG", format_string="{func_name} called with args: {args} (types: {types})"):
    """
    A decorator that logs the function name, its arguments, and the types of the arguments.

    Parameters:
        level (str): The logging level (default is "DEBUG").
        format_string (str): The format string for the log message (default is "{func_name} called with args: {args} (types: {types})").

    Example:
        @param_type_tracer(level="DEBUG")
        def print_params(a, b):
            print(a, b)
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            types = [type(arg).__name__ for arg in args]
            logger.info(
                format_string.format(func_name=func.__name__, args=args, types=types)
            )
            return func(*args, **kwargs)
        return wrapper
    return decorator


def detailed_tracer(
    level="INFO",
    format_string="{func_name} executed with args: {args}, kwargs: {kwargs}, returned: {return_value}, exception: {exception}"
):
    """
    A decorator that logs detailed information about function execution, including arguments, keyword arguments, return value, and exceptions.

    Parameters:
        level (str): The logging level (default is "INFO").
        format_string (str): The format string for the log message (default is "{func_name} executed with args: {args}, kwargs: {kwargs}, returned: {return_value}, exception: {exception}").

    Example:
        @detailed_tracer(level="DEBUG")
        def complex_function(a, b):
            return a / b
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logger.info(
                    format_string.format(
                        func_name=func.__name__,
                        args=args,
                        kwargs=kwargs,
                        return_value=result,
                        exception=None,
                    )
                )
                return result
            except Exception as e:
                logger.error(
                    format_string.format(
                        func_name=func.__name__,
                        args=args,
                        kwargs=kwargs,
                        return_value=None,
                        exception=traceback.format_exc(),
                    )
                )
                raise
        return wrapper
    return decorator


def as_json_tracer(level="INFO", format_string="{log_data}"):
    """
    A decorator that logs the function execution details in JSON format.

    Parameters:
        level (str): The logging level (default is "INFO").
        format_string (str): The format string for the log message (default is "{log_data}").

    Example:
        @as_json_tracer(level="DEBUG")
        def example_function(a, b):
            return a + b
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            log_data = json.dumps(
                {
                    "func_name": func.__name__,
                    "args": args,
                    "kwargs": kwargs,
                    "return_value": result,
                },
                default=str,
            )
            logger.info(format_string.format(log_data=log_data))
            return result
        return wrapper
    return decorator
