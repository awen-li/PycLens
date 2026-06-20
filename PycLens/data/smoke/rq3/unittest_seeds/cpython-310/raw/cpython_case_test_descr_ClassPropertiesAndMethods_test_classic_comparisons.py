# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_classic_comparisons

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class classic:
        pass
    for base in (classic, int, object):

        class C(base):

            def __init__(self, value):
                self.value = int(value)

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
