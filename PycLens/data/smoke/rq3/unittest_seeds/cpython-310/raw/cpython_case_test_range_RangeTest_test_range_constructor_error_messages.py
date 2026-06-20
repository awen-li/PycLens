# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_range_constructor_error_messages

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(TypeError, 'range expected at least 1 argument, got 0'):
        range()
    with self.assertRaisesRegex(TypeError, 'range expected at most 3 arguments, got 6'):
        range(1, 2, 3, 4, 5, 6)
