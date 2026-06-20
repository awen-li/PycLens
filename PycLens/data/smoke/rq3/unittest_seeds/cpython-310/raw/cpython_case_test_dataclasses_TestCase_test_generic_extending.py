# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_generic_extending

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    S = TypeVar('S')
    T = TypeVar('T')

    @dataclass
    class Base(Generic[T, S]):
        x: T
        y: S

    @dataclass
    class DataDerived(Base[int, T]):
        new_field: str
    Alias = DataDerived[str]
    c = Alias(0, 'test1', 'test2')
    self.assertEqual(astuple(c), (0, 'test1', 'test2'))

    class NonDataDerived(Base[int, T]):

        def new_method(self):
            return self.y
    Alias = NonDataDerived[float]
    c = Alias(10, 1.0)
    self.assertEqual(c.new_method(), 1.0)
