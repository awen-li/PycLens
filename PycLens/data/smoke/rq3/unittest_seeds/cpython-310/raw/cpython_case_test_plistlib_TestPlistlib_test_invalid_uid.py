# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_invalid_uid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        UID('not an int')
    with self.assertRaises(ValueError):
        UID(2 ** 64)
    with self.assertRaises(ValueError):
        UID(-19)
