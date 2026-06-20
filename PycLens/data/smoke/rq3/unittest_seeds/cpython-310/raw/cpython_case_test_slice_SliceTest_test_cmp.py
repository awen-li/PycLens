# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_slice.py
# case: SliceTest_test_cmp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s1 = slice(1, 2, 3)
    s2 = slice(1, 2, 3)
    s3 = slice(1, 2, 4)
    self.assertEqual(s1, s2)
    self.assertNotEqual(s1, s3)
    self.assertNotEqual(s1, None)
    self.assertNotEqual(s1, (1, 2, 3))
    self.assertNotEqual(s1, '')

    class Exc(Exception):
        pass

    class BadCmp(object):

        def __eq__(self, other):
            raise Exc
    s1 = slice(BadCmp())
    s2 = slice(BadCmp())
    self.assertEqual(s1, s1)
    self.assertRaises(Exc, lambda : s1 == s2)
    s1 = slice(1, BadCmp())
    s2 = slice(1, BadCmp())
    self.assertEqual(s1, s1)
    self.assertRaises(Exc, lambda : s1 == s2)
    s1 = slice(1, 2, BadCmp())
    s2 = slice(1, 2, BadCmp())
    self.assertEqual(s1, s1)
    self.assertRaises(Exc, lambda : s1 == s2)
