# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestAbstract_test_abc_implementation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Ordered(abc.ABC):

        @abc.abstractmethod
        def __lt__(self, other):
            pass

        @abc.abstractmethod
        def __le__(self, other):
            pass

    @dataclass(order=True)
    class Date(Ordered):
        year: int
        month: 'Month'
        day: 'int'
    self.assertFalse(inspect.isabstract(Date))
    self.assertGreater(Date(2020, 12, 25), Date(2020, 8, 31))
