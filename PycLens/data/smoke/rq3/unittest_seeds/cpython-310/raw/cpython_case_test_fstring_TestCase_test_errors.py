# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertAllRaise(TypeError, 'unsupported', ["f'{(lambda: 0):x}'", "f'{(0,):x}'"])
    self.assertAllRaise(ValueError, 'Unknown format code', ["f'{1000:j}'", "f'{1000:j}'"])
