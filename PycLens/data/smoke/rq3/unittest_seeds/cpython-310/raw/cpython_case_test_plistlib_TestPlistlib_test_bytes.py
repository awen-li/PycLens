# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pl = self._create()
    data = plistlib.dumps(pl)
    pl2 = plistlib.loads(data)
    self.assertEqual(dict(pl), dict(pl2))
    data2 = plistlib.dumps(pl2)
    self.assertEqual(data, data2)
