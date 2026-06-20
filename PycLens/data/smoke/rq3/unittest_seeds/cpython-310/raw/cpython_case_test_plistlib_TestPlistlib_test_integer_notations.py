# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_integer_notations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pl = b'<plist><integer>456</integer></plist>'
    value = plistlib.loads(pl)
    self.assertEqual(value, 456)
    pl = b'<plist><integer>0xa</integer></plist>'
    value = plistlib.loads(pl)
    self.assertEqual(value, 10)
    pl = b'<plist><integer>0123</integer></plist>'
    value = plistlib.loads(pl)
    self.assertEqual(value, 123)
