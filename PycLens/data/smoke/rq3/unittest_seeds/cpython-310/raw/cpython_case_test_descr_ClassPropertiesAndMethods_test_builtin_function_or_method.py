# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_builtin_function_or_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = []
    self.assertTrue(l.append == l.append)
    self.assertFalse(l.append != l.append)
    self.assertFalse(l.append == [].append)
    self.assertTrue(l.append != [].append)
    self.assertFalse(l.append == l.pop)
    self.assertTrue(l.append != l.pop)
    self.assertNotOrderable(l.append, l.append)
    self.assertEqual(l.append.__name__, 'append')
    self.assertIs(l.append.__self__, l)
    self.assertEqual(l.append.__doc__, list.append.__doc__)
    hash(l.append)
