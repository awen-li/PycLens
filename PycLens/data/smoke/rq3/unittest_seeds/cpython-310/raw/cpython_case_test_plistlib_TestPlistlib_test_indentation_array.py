# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_indentation_array

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [[[[[[[[{'test': b'aaaaaa'}]]]]]]]]
    self.assertEqual(plistlib.loads(plistlib.dumps(data)), data)
