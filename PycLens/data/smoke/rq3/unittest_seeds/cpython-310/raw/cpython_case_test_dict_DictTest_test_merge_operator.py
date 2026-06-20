# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_merge_operator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = {0: 0, 1: 1, 2: 1}
    b = {1: 1, 2: 2, 3: 3}
    c = a.copy()
    c |= b
    self.assertEqual(a | b, {0: 0, 1: 1, 2: 2, 3: 3})
    self.assertEqual(c, {0: 0, 1: 1, 2: 2, 3: 3})
    c = b.copy()
    c |= a
    self.assertEqual(b | a, {1: 1, 2: 1, 3: 3, 0: 0})
    self.assertEqual(c, {1: 1, 2: 1, 3: 3, 0: 0})
    c = a.copy()
    c |= [(1, 1), (2, 2), (3, 3)]
    self.assertEqual(c, {0: 0, 1: 1, 2: 2, 3: 3})
    self.assertIs(a.__or__(None), NotImplemented)
    self.assertIs(a.__or__(()), NotImplemented)
    self.assertIs(a.__or__('BAD'), NotImplemented)
    self.assertIs(a.__or__(''), NotImplemented)
    self.assertRaises(TypeError, a.__ior__, None)
    self.assertEqual(a.__ior__(()), {0: 0, 1: 1, 2: 1})
    self.assertRaises(ValueError, a.__ior__, 'BAD')
    self.assertEqual(a.__ior__(''), {0: 0, 1: 1, 2: 1})
