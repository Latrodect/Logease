from logless.decorators.tracer import (
    function_tracer,
    class_method_tracer,
    property_getter_tracer,
    constructor_tracer,
)


@function_tracer(
    level="DEBUG", format_string="{func_name} is executing with args: {args}"
)
def add(a, b):
    return a + b


result = add(1, 2)


class MyClass:
    @class_method_tracer(level="DEBUG")
    def class_method(cls, a):
        return a * 2


result = MyClass.class_method(10)


class MyClassWithProperty:
    def __init__(self, x):
        self._x = x

    @property
    @property_getter_tracer("x", level="DEBUG")
    def x(self):
        return self._x


obj = MyClassWithProperty(10)
value = obj.x


@constructor_tracer
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


obj = MyClass(2, 3)
