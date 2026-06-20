# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_rich_comparisons

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Z(complex):
        pass
    z = Z(1)
    self.assertEqual(z, 1 + 0j)
    self.assertEqual(1 + 0j, z)

    class ZZ(complex):

        def __eq__(self, other):
            try:
                return abs(self - other) <= 1e-06
            except:
                return NotImplemented
    zz = ZZ(1.0000003)
    self.assertEqual(zz, 1 + 0j)
    self.assertEqual(1 + 0j, zz)

    class classic:
        pass
    for base in (classic, int, object, list):

        class C(base):

            def __init__(self, value):
                self.value = int(value)

            def __cmp__(self_, other):
                self.fail("shouldn't call __cmp__")

            def __eq__(self, other):
                if isinstance(other, C):
                    return self.value == other.value
                if isinstance(other, int) or isinstance(other, int):
                    return self.value == other
                return NotImplemented

            def __ne__(self, other):
                if isinstance(other, C):
                    return self.value != other.value
                if isinstance(other, int) or isinstance(other, int):
                    return self.value != other
                return NotImplemented

            def __lt__(self, other):
                if isinstance(other, C):
                    return self.value < other.value
                if isinstance(other, int) or isinstance(other, int):
                    return self.value < other
                return NotImplemented

            def __le__(self, other):
                if isinstance(other, C):
                    return self.value <= other.value
                if isinstance(other, int) or isinstance(other, int):
                    return self.value <= other
                return NotImplemented

            def __gt__(self, other):
                if isinstance(other, C):
                    return self.value > other.value
                if isinstance(other, int) or isinstance(other, int):
                    return self.value > other
                return NotImplemented

            def __ge__(self, other):
                if isinstance(other, C):
                    return self.value >= other.value
                if isinstance(other, int) or isinstance(other, int):
                    return self.value >= other
                return NotImplemented
        c1 = C(1)
        c2 = C(2)
        c3 = C(3)
        self.assertEqual(c1, 1)
        c = {1: c1, 2: c2, 3: c3}
        for x in (1, 2, 3):
            for y in (1, 2, 3):
                for op in ('<', '<=', '==', '!=', '>', '>='):
                    self.assertEqual(eval('c[x] %s c[y]' % op), eval('x %s y' % op), 'x=%d, y=%d' % (x, y))
                    self.assertEqual(eval('c[x] %s y' % op), eval('x %s y' % op), 'x=%d, y=%d' % (x, y))
                    self.assertEqual(eval('x %s c[y]' % op), eval('x %s y' % op), 'x=%d, y=%d' % (x, y))
