# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_29444

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = bytearray(b'abcdefgh')
    m = re.search(b'[a-h]+', s)
    m2 = re.search(b'[e-h]+', s)
    self.assertEqual(m.group(), b'abcdefgh')
    self.assertEqual(m2.group(), b'efgh')
    s[:] = b'xyz'
    self.assertEqual(m.group(), b'xyz')
    self.assertEqual(m2.group(), b'')
