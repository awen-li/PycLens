# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_surrogates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in ('a\ud800b\udfff', 'a\udfffb\ud800', 'a\ud800b\udfffa', 'a\udfffb\ud800a'):
        self.assertTrue(s.islower())
        self.assertFalse(s.isupper())
        self.assertFalse(s.istitle())
    for s in ('A\ud800B\udfff', 'A\udfffB\ud800', 'A\ud800B\udfffA', 'A\udfffB\ud800A'):
        self.assertFalse(s.islower())
        self.assertTrue(s.isupper())
        self.assertTrue(s.istitle())
    for meth_name in ('islower', 'isupper', 'istitle'):
        meth = getattr(str, meth_name)
        for s in ('\ud800', '\udfff', '\ud800\ud800', '\udfff\udfff'):
            self.assertFalse(meth(s), '%a.%s() is False' % (s, meth_name))
    for meth_name in ('isalpha', 'isalnum', 'isdigit', 'isspace', 'isdecimal', 'isnumeric', 'isidentifier', 'isprintable'):
        meth = getattr(str, meth_name)
        for s in ('\ud800', '\udfff', '\ud800\ud800', '\udfff\udfff', 'a\ud800b\udfff', 'a\udfffb\ud800', 'a\ud800b\udfffa', 'a\udfffb\ud800a'):
            self.assertFalse(meth(s), '%a.%s() is False' % (s, meth_name))
