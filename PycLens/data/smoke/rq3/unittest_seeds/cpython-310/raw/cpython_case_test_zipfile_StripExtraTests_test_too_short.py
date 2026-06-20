# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StripExtraTests_test_too_short

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(b'', zipfile._strip_extra(b'', (self.ZIP64_EXTRA,)))
    self.assertEqual(b'z', zipfile._strip_extra(b'z', (self.ZIP64_EXTRA,)))
    self.assertEqual(b'zz', zipfile._strip_extra(b'zz', (self.ZIP64_EXTRA,)))
    self.assertEqual(b'zzz', zipfile._strip_extra(b'zzz', (self.ZIP64_EXTRA,)))
