# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_invalidarray

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in ['<key>key inside an array</key>', '<key>key inside an array2</key><real>3</real>', '<true/><key>key inside an array3</key>']:
        self.assertRaises(ValueError, plistlib.loads, ('<plist><array>%s</array></plist>' % i).encode())
