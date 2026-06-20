# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: MiscTest_test_array_is_sequence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(array.array('B'), collections.abc.MutableSequence)
    self.assertIsInstance(array.array('B'), collections.abc.Reversible)
