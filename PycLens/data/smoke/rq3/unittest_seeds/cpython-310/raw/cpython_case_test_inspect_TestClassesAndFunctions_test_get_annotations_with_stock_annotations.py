# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_get_annotations_with_stock_annotations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo(a: int, b: str):
        pass
    self.assertEqual(inspect.get_annotations(foo), {'a': int, 'b': str})
    foo.__annotations__ = {'a': 'foo', 'b': 'str'}
    self.assertEqual(inspect.get_annotations(foo), {'a': 'foo', 'b': 'str'})
    self.assertEqual(inspect.get_annotations(foo, eval_str=True, locals=locals()), {'a': foo, 'b': str})
    self.assertEqual(inspect.get_annotations(foo, eval_str=True, globals=locals()), {'a': foo, 'b': str})
    isa = inspect_stock_annotations
    self.assertEqual(inspect.get_annotations(isa), {'a': int, 'b': str})
    self.assertEqual(inspect.get_annotations(isa.MyClass), {'a': int, 'b': str})
    self.assertEqual(inspect.get_annotations(isa.function), {'a': int, 'b': str, 'return': isa.MyClass})
    self.assertEqual(inspect.get_annotations(isa.function2), {'a': int, 'b': 'str', 'c': isa.MyClass, 'return': isa.MyClass})
    self.assertEqual(inspect.get_annotations(isa.function3), {'a': 'int', 'b': 'str', 'c': 'MyClass'})
    self.assertEqual(inspect.get_annotations(inspect), {})
    self.assertEqual(inspect.get_annotations(isa.UnannotatedClass), {})
    self.assertEqual(inspect.get_annotations(isa.unannotated_function), {})
    self.assertEqual(inspect.get_annotations(isa, eval_str=True), {'a': int, 'b': str})
    self.assertEqual(inspect.get_annotations(isa.MyClass, eval_str=True), {'a': int, 'b': str})
    self.assertEqual(inspect.get_annotations(isa.function, eval_str=True), {'a': int, 'b': str, 'return': isa.MyClass})
    self.assertEqual(inspect.get_annotations(isa.function2, eval_str=True), {'a': int, 'b': str, 'c': isa.MyClass, 'return': isa.MyClass})
    self.assertEqual(inspect.get_annotations(isa.function3, eval_str=True), {'a': int, 'b': str, 'c': isa.MyClass})
    self.assertEqual(inspect.get_annotations(inspect, eval_str=True), {})
    self.assertEqual(inspect.get_annotations(isa.UnannotatedClass, eval_str=True), {})
    self.assertEqual(inspect.get_annotations(isa.unannotated_function, eval_str=True), {})
    self.assertEqual(inspect.get_annotations(isa, eval_str=False), {'a': int, 'b': str})
    self.assertEqual(inspect.get_annotations(isa.MyClass, eval_str=False), {'a': int, 'b': str})
    self.assertEqual(inspect.get_annotations(isa.function, eval_str=False), {'a': int, 'b': str, 'return': isa.MyClass})
    self.assertEqual(inspect.get_annotations(isa.function2, eval_str=False), {'a': int, 'b': 'str', 'c': isa.MyClass, 'return': isa.MyClass})
    self.assertEqual(inspect.get_annotations(isa.function3, eval_str=False), {'a': 'int', 'b': 'str', 'c': 'MyClass'})
    self.assertEqual(inspect.get_annotations(inspect, eval_str=False), {})
    self.assertEqual(inspect.get_annotations(isa.UnannotatedClass, eval_str=False), {})
    self.assertEqual(inspect.get_annotations(isa.unannotated_function, eval_str=False), {})

    def times_three(fn):

        @functools.wraps(fn)
        def wrapper(a, b):
            return fn(a * 3, b * 3)
        return wrapper
    wrapped = times_three(isa.function)
    self.assertEqual(wrapped(1, 'x'), isa.MyClass(3, 'xxx'))
    self.assertIsNot(wrapped.__globals__, isa.function.__globals__)
    self.assertEqual(inspect.get_annotations(wrapped), {'a': int, 'b': str, 'return': isa.MyClass})
    self.assertEqual(inspect.get_annotations(wrapped, eval_str=True), {'a': int, 'b': str, 'return': isa.MyClass})
    self.assertEqual(inspect.get_annotations(wrapped, eval_str=False), {'a': int, 'b': str, 'return': isa.MyClass})
