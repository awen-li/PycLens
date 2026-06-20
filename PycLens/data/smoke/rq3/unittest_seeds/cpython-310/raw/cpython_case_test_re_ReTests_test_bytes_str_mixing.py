# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bytes_str_mixing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pat = re.compile('.')
    bpat = re.compile(b'.')
    self.assertRaises(TypeError, pat.match, b'b')
    self.assertRaises(TypeError, bpat.match, 'b')
    self.assertRaises(TypeError, pat.sub, b'b', 'c')
    self.assertRaises(TypeError, pat.sub, 'b', b'c')
    self.assertRaises(TypeError, pat.sub, b'b', b'c')
    self.assertRaises(TypeError, bpat.sub, b'b', 'c')
    self.assertRaises(TypeError, bpat.sub, 'b', b'c')
    self.assertRaises(TypeError, bpat.sub, 'b', 'c')
