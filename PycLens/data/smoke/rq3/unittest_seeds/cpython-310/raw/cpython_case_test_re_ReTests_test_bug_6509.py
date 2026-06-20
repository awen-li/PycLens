# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_6509

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pat = re.compile('a(\\w)')
    self.assertEqual(pat.sub('b\\1', 'ac'), 'bc')
    pat = re.compile('a(.)')
    self.assertEqual(pat.sub('b\\1', 'aሴ'), 'bሴ')
    pat = re.compile('..')
    self.assertEqual(pat.sub(lambda m: 'str', 'a5'), 'str')
    pat = re.compile(b'a(\\w)')
    self.assertEqual(pat.sub(b'b\\1', b'ac'), b'bc')
    pat = re.compile(b'a(.)')
    self.assertEqual(pat.sub(b'b\\1', b'a\xcd'), b'b\xcd')
    pat = re.compile(b'..')
    self.assertEqual(pat.sub(lambda m: b'bytes', b'a5'), b'bytes')
