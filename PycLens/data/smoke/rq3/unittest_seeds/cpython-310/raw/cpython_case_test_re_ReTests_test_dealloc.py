# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_dealloc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _sre
    long_overflow = 2 ** 128
    self.assertRaises(TypeError, re.finditer, 'a', {})
    with self.assertRaises(OverflowError):
        _sre.compile('abc', 0, [long_overflow], 0, {}, ())
    with self.assertRaises(TypeError):
        _sre.compile({}, 0, [], 0, [], [])
