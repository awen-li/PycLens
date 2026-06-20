# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_invaliddict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in ['<key><true/>k</key><string>compound key</string>', '<key>single key</key>', '<string>missing key</string>', '<key>k1</key><string>v1</string><real>5.3</real><key>k1</key><key>k2</key><string>double key</string>']:
        self.assertRaises(ValueError, plistlib.loads, ('<plist><dict>%s</dict></plist>' % i).encode())
        self.assertRaises(ValueError, plistlib.loads, ('<plist><array><dict>%s</dict></array></plist>' % i).encode())
