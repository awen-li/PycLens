# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compare.py
# case: ComparisonTest_test_ne_low_priority

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    calls = []

    class Base:

        def __eq__(*args):
            calls.append('Base.__eq__')
            return NotImplemented

    class Derived(Base):

        def __eq__(*args):
            calls.append('Derived.__eq__')
            return NotImplemented

        def __ne__(*args):
            calls.append('Derived.__ne__')
            return NotImplemented
    Base() != Derived()
    self.assertSequenceEqual(calls, ['Derived.__ne__', 'Base.__eq__'])
