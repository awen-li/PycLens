# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compare.py
# case: ComparisonTest_test_ne_high_priority

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    calls = []

    class Left:

        def __eq__(*args):
            calls.append('Left.__eq__')
            return NotImplemented

    class Right:

        def __eq__(*args):
            calls.append('Right.__eq__')
            return NotImplemented

        def __ne__(*args):
            calls.append('Right.__ne__')
            return NotImplemented
    Left() != Right()
    self.assertSequenceEqual(calls, ['Left.__eq__', 'Right.__ne__'])
