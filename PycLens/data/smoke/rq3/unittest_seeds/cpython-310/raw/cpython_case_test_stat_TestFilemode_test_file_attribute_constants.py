# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_stat.py
# case: TestFilemode_test_file_attribute_constants

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (key, value) in sorted(self.file_attributes.items()):
        self.assertTrue(hasattr(self.statmod, key), key)
        modvalue = getattr(self.statmod, key)
        self.assertEqual(value, modvalue, key)
