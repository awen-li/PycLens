# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestAbstract_test_maintain_abc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(abc.ABC):

        @abc.abstractmethod
        def foo(self):
            pass

    @dataclass
    class Date(A):
        year: int
        month: 'Month'
        day: 'int'
    self.assertTrue(inspect.isabstract(Date))
    msg = 'class Date with abstract method foo'
    self.assertRaisesRegex(TypeError, msg, Date)
