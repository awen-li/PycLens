# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: LengthTransparency_test_repeat_with_negative_times

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(operator.length_hint(repeat(None, -1)), 0)
    self.assertEqual(operator.length_hint(repeat(None, -2)), 0)
    self.assertEqual(operator.length_hint(repeat(None, times=-1)), 0)
    self.assertEqual(operator.length_hint(repeat(None, times=-2)), 0)
