# Source Generated with Decompyle++
# File: cpython-311-f4ffcfa646c0.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    class Z(complex):
        pass

    z = Z(1)
    self.assertEqual(z, (1+0j))
    self.assertEqual((1+0j), z)
    
    class ZZ(complex):
        
        def __eq__(self, other):
            return abs(self - other) <= 1e-06
            if None:
                return 


    zz = ZZ(1)
    self.assertEqual(zz, (1+0j))
    self.assertEqual((1+0j), zz)
    
    class classic:
        pass

    for base in (classic, int, object, list):
        
        def C():
            '''__pybcsec_seed__.<locals>.C'''
            
            def __init__(self, value):
                self.value = int(value)

            
            def __cmp__(self_, other):
                self.fail("shouldn't call __cmp__")

            
            def __eq__(self, other):
                if isinstance(other, C):
                    return self.value == other.value
                if None(other, int) or isinstance(other, int):
                    return self.value == other

            
            def __ne__(self, other):
                if isinstance(other, C):
                    return self.value != other.value
                if None(other, int) or isinstance(other, int):
                    return self.value != other

            
            def __lt__(self, other):
                if isinstance(other, C):
                    return self.value < other.value
                if None(other, int) or isinstance(other, int):
                    return self.value < other

            
            def __le__(self, other):
                if isinstance(other, C):
                    return self.value <= other.value
                if None(other, int) or isinstance(other, int):
                    return self.value <= other

            
            def __gt__(self, other):
                if isinstance(other, C):
                    return self.value > other.value
                if None(other, int) or isinstance(other, int):
                    return self.value > other

            
            def __ge__(self, other):
                if isinstance(other, C):
                    return self.value >= other.value
                if None(other, int) or isinstance(other, int):
                    return self.value >= other


        C = None(C, 'C', base)
        c1 = C(1)
        c2 = C(2)
        c3 = C(3)
        self.assertEqual(c1, 1)
        c = {
            1: c1,
            2: c2,
            3: c3 }
        for x in (1, 2, 3):
            for y in (1, 2, 3):
                for op in ('<', '<=', '==', '!=', '>', '>='):
                    self.assertEqual(eval('c[x] %s c[y]' % op), eval('x %s y' % op), 'x=%d, y=%d' % (x, y))
                    self.assertEqual(eval('c[x] %s y' % op), eval('x %s y' % op), 'x=%d, y=%d' % (x, y))
                    self.assertEqual(eval('x %s c[y]' % op), eval('x %s y' % op), 'x=%d, y=%d' % (x, y))

# WARNING: Decompyle incomplete
