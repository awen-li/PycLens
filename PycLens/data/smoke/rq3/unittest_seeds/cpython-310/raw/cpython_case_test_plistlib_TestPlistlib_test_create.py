# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_create

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pl = self._create()
    self.assertEqual(pl['aString'], 'Doodah')
    self.assertEqual(pl['aDict']['aFalseValue'], False)
