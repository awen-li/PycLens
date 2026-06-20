# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shelve.py
# case: TestCase_test_keyencoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {}
    key = 'PÃ¶p'
    shelve.Shelf(d)[key] = [1]
    self.assertIn(key.encode('utf-8'), d)
    shelve.Shelf(d, keyencoding='latin-1')[key] = [1]
    self.assertIn(key.encode('latin-1'), d)
    s = shelve.Shelf(d, keyencoding='ascii')
    self.assertRaises(UnicodeEncodeError, s.__setitem__, key, [1])
