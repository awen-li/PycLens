# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_dataclasses_qualnames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(order=True, unsafe_hash=True, frozen=True)
    class A:
        x: int
        y: int
    self.assertEqual(A.__init__.__name__, '__init__')
    for function in ('__eq__', '__lt__', '__le__', '__gt__', '__ge__', '__hash__', '__init__', '__repr__', '__setattr__', '__delattr__'):
        self.assertEqual(getattr(A, function).__qualname__, f'TestCase.test_dataclasses_qualnames.<locals>.A.{function}')
    with self.assertRaisesRegex(TypeError, 'A\\.__init__\\(\\) missing'):
        A()
