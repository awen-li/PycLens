# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_staticmethods_in_c

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import xxsubtype as spam
    a = (1, 2, 3)
    d = {'abc': 123}
    (x, a1, d1) = spam.spamlist.staticmeth(*a, **d)
    self.assertEqual(x, None)
    self.assertEqual(a, a1)
    self.assertEqual(d, d1)
    (x, a1, d2) = spam.spamlist().staticmeth(*a, **d)
    self.assertEqual(x, None)
    self.assertEqual(a, a1)
    self.assertEqual(d, d1)
