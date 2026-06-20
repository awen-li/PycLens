# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_specials

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __getitem__(self, i):
            if 0 <= i < 10:
                return i
            raise IndexError
    c1 = C()
    c2 = C()
    self.assertFalse(not c1)
    self.assertNotEqual(id(c1), id(c2))
    hash(c1)
    hash(c2)
    self.assertEqual(c1, c1)
    self.assertTrue(c1 != c2)
    self.assertFalse(c1 != c1)
    self.assertFalse(c1 == c2)
    self.assertGreaterEqual(str(c1).find('C object at '), 0)
    self.assertEqual(str(c1), repr(c1))
    self.assertNotIn(-1, c1)
    for i in range(10):
        self.assertIn(i, c1)
    self.assertNotIn(10, c1)

    class D(object):

        def __getitem__(self, i):
            if 0 <= i < 10:
                return i
            raise IndexError
    d1 = D()
    d2 = D()
    self.assertFalse(not d1)
    self.assertNotEqual(id(d1), id(d2))
    hash(d1)
    hash(d2)
    self.assertEqual(d1, d1)
    self.assertNotEqual(d1, d2)
    self.assertFalse(d1 != d1)
    self.assertFalse(d1 == d2)
    self.assertGreaterEqual(str(d1).find('D object at '), 0)
    self.assertEqual(str(d1), repr(d1))
    self.assertNotIn(-1, d1)
    for i in range(10):
        self.assertIn(i, d1)
    self.assertNotIn(10, d1)

    class Proxy(object):

        def __init__(self, x):
            self.x = x

        def __bool__(self):
            return not not self.x

        def __hash__(self):
            return hash(self.x)

        def __eq__(self, other):
            return self.x == other

        def __ne__(self, other):
            return self.x != other

        def __ge__(self, other):
            return self.x >= other

        def __gt__(self, other):
            return self.x > other

        def __le__(self, other):
            return self.x <= other

        def __lt__(self, other):
            return self.x < other

        def __str__(self):
            return 'Proxy:%s' % self.x

        def __repr__(self):
            return 'Proxy(%r)' % self.x

        def __contains__(self, value):
            return value in self.x
    p0 = Proxy(0)
    p1 = Proxy(1)
    p_1 = Proxy(-1)
    self.assertFalse(p0)
    self.assertFalse(not p1)
    self.assertEqual(hash(p0), hash(0))
    self.assertEqual(p0, p0)
    self.assertNotEqual(p0, p1)
    self.assertFalse(p0 != p0)
    self.assertEqual(not p0, p1)
    self.assertTrue(p0 < p1)
    self.assertTrue(p0 <= p1)
    self.assertTrue(p1 > p0)
    self.assertTrue(p1 >= p0)
    self.assertEqual(str(p0), 'Proxy:0')
    self.assertEqual(repr(p0), 'Proxy(0)')
    p10 = Proxy(range(10))
    self.assertNotIn(-1, p10)
    for i in range(10):
        self.assertIn(i, p10)
    self.assertNotIn(10, p10)
