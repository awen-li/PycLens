# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: FnmatchTestCase_test_mix_bytes_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, fnmatch, 'test', b'*')
    self.assertRaises(TypeError, fnmatch, b'test', '*')
    self.assertRaises(TypeError, fnmatchcase, 'test', b'*')
    self.assertRaises(TypeError, fnmatchcase, b'test', '*')
