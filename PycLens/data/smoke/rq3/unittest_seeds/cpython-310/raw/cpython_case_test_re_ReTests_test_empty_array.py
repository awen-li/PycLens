# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_empty_array

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import array
    for typecode in 'bBuhHiIlLfd':
        a = array.array(typecode)
        self.assertIsNone(re.compile(b'bla').match(a))
        self.assertEqual(re.compile(b'').match(a).groups(), ())
