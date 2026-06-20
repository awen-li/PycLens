# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StripExtraTests_test_multiples

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = struct.Struct('<HH')
    a = s.pack(self.ZIP64_EXTRA, 1) + b'a'
    b = s.pack(2, 2) + b'bb'
    self.assertEqual(b'', zipfile._strip_extra(a + a, (self.ZIP64_EXTRA,)))
    self.assertEqual(b'', zipfile._strip_extra(a + a + a, (self.ZIP64_EXTRA,)))
    self.assertEqual(b'z', zipfile._strip_extra(a + a + b'z', (self.ZIP64_EXTRA,)))
    self.assertEqual(b + b'z', zipfile._strip_extra(a + a + b + b'z', (self.ZIP64_EXTRA,)))
    self.assertEqual(b, zipfile._strip_extra(a + a + b, (self.ZIP64_EXTRA,)))
    self.assertEqual(b, zipfile._strip_extra(a + b + a, (self.ZIP64_EXTRA,)))
    self.assertEqual(b, zipfile._strip_extra(b + a + a, (self.ZIP64_EXTRA,)))
