# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ImplementationTest_test_immutable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        re.Match.foo = 1
    with self.assertRaises(TypeError):
        re.Pattern.foo = 1
    with self.assertRaises(TypeError):
        pat = re.compile('')
        tp = type(pat.scanner(''))
        tp.foo = 1
