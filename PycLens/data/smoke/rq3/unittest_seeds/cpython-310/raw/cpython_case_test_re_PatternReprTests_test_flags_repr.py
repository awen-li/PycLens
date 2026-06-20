# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: PatternReprTests_test_flags_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(re.I), 're.IGNORECASE')
    self.assertEqual(repr(re.I | re.S | re.X), 're.IGNORECASE|re.DOTALL|re.VERBOSE')
    self.assertEqual(repr(re.I | re.S | re.X | 1 << 20), 're.IGNORECASE|re.DOTALL|re.VERBOSE|0x100000')
    self.assertEqual(repr(~re.I), '~re.IGNORECASE')
    self.assertEqual(repr(~(re.I | re.S | re.X)), '~(re.IGNORECASE|re.DOTALL|re.VERBOSE)')
    self.assertEqual(repr(~(re.I | re.S | re.X | 1 << 20)), '~(re.IGNORECASE|re.DOTALL|re.VERBOSE|0x100000)')
