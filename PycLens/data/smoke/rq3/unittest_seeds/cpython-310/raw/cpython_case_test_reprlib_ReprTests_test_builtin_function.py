# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: ReprTests_test_builtin_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(repr(hash), '<built-in function hash>')
    self.assertTrue(repr(''.split).startswith('<built-in method split of str object at 0x'))
