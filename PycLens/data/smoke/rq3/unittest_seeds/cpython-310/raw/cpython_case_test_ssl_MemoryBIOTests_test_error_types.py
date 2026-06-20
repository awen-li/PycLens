# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: MemoryBIOTests_test_error_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bio = ssl.MemoryBIO()
    self.assertRaises(TypeError, bio.write, 'foo')
    self.assertRaises(TypeError, bio.write, None)
    self.assertRaises(TypeError, bio.write, True)
    self.assertRaises(TypeError, bio.write, 1)
