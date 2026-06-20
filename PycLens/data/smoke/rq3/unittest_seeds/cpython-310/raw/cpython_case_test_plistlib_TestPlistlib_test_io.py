# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_io

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pl = self._create()
    with open(os_helper.TESTFN, 'wb') as fp:
        plistlib.dump(pl, fp)
    with open(os_helper.TESTFN, 'rb') as fp:
        pl2 = plistlib.load(fp)
    self.assertEqual(dict(pl), dict(pl2))
    self.assertRaises(AttributeError, plistlib.dump, pl, 'filename')
    self.assertRaises(AttributeError, plistlib.load, 'filename')
