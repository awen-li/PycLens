# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: StrTest_test_unicode_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    char = '\udcba'
    s = char * size
    try:
        for f in (repr, ascii):
            r = f(s)
            self.assertEqual(len(r), 2 + (len(f(char)) - 2) * size)
            self.assertTrue(r.endswith("\\udcba'"), r[-10:])
            r = None
    finally:
        r = s = None
