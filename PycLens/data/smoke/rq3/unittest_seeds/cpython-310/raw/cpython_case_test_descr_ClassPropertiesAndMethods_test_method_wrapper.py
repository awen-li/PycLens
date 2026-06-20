# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_method_wrapper

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = []
    self.assertTrue(l.__add__ == l.__add__)
    self.assertFalse(l.__add__ != l.__add__)
    self.assertFalse(l.__add__ == [].__add__)
    self.assertTrue(l.__add__ != [].__add__)
    self.assertFalse(l.__add__ == l.__mul__)
    self.assertTrue(l.__add__ != l.__mul__)
    self.assertNotOrderable(l.__add__, l.__add__)
    self.assertEqual(l.__add__.__name__, '__add__')
    self.assertIs(l.__add__.__self__, l)
    self.assertIs(l.__add__.__objclass__, list)
    self.assertEqual(l.__add__.__doc__, list.__add__.__doc__)
    hash(l.__add__)
