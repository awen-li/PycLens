# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_special_unbound_method_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(list.__add__ == list.__add__)
    self.assertFalse(list.__add__ != list.__add__)
    self.assertFalse(list.__add__ == list.__mul__)
    self.assertTrue(list.__add__ != list.__mul__)
    self.assertNotOrderable(list.__add__, list.__add__)
    self.assertEqual(list.__add__.__name__, '__add__')
    self.assertIs(list.__add__.__objclass__, list)
    self.assertTrue(list.append == list.append)
    self.assertFalse(list.append != list.append)
    self.assertFalse(list.append == list.pop)
    self.assertTrue(list.append != list.pop)
    self.assertNotOrderable(list.append, list.append)
    self.assertEqual(list.append.__name__, 'append')
    self.assertIs(list.append.__objclass__, list)
