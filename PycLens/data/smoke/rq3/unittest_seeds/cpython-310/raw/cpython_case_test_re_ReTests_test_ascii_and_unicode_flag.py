# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_ascii_and_unicode_flag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for flags in (0, re.UNICODE):
        pat = re.compile('À', flags | re.IGNORECASE)
        self.assertTrue(pat.match('à'))
        pat = re.compile('\\w', flags)
        self.assertTrue(pat.match('à'))
    pat = re.compile('À', re.ASCII | re.IGNORECASE)
    self.assertIsNone(pat.match('à'))
    pat = re.compile('(?a)À', re.IGNORECASE)
    self.assertIsNone(pat.match('à'))
    pat = re.compile('\\w', re.ASCII)
    self.assertIsNone(pat.match('à'))
    pat = re.compile('(?a)\\w')
    self.assertIsNone(pat.match('à'))
    for flags in (0, re.ASCII):
        pat = re.compile(b'\xc0', flags | re.IGNORECASE)
        self.assertIsNone(pat.match(b'\xe0'))
        pat = re.compile(b'\\w', flags)
        self.assertIsNone(pat.match(b'\xe0'))
    self.assertRaises(ValueError, re.compile, b'\\w', re.UNICODE)
    self.assertRaises(re.error, re.compile, b'(?u)\\w')
    self.assertRaises(ValueError, re.compile, '\\w', re.UNICODE | re.ASCII)
    self.assertRaises(ValueError, re.compile, '(?u)\\w', re.ASCII)
    self.assertRaises(ValueError, re.compile, '(?a)\\w', re.UNICODE)
    self.assertRaises(re.error, re.compile, '(?au)\\w')
