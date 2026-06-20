# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iterlen.py
# case: TestLengthHintExceptions_test_issue1242657

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(RuntimeError, list, BadLen())
    self.assertRaises(RuntimeError, list, BadLengthHint())
    self.assertRaises(RuntimeError, [].extend, BadLen())
    self.assertRaises(RuntimeError, [].extend, BadLengthHint())
    b = bytearray(range(10))
    self.assertRaises(RuntimeError, b.extend, BadLen())
    self.assertRaises(RuntimeError, b.extend, BadLengthHint())
