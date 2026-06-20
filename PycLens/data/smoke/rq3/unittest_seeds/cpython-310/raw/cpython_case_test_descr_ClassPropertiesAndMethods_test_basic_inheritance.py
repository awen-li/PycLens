# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_basic_inheritance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class hexint(int):

        def __repr__(self):
            return hex(self)

        def __add__(self, other):
            return hexint(int.__add__(self, other))
    self.assertEqual(repr(hexint(7) + 9), '0x10')
    self.assertEqual(repr(hexint(1000) + 7), '0x3ef')
    a = hexint(12345)
    self.assertEqual(a, 12345)
    self.assertEqual(int(a), 12345)
    self.assertIs(int(a).__class__, int)
    self.assertEqual(hash(a), hash(12345))
    self.assertIs((+a).__class__, int)
    self.assertIs((a >> 0).__class__, int)
    self.assertIs((a << 0).__class__, int)
    self.assertIs((hexint(0) << 12).__class__, int)
    self.assertIs((hexint(0) >> 12).__class__, int)

    class octlong(int):
        __slots__ = []

        def __str__(self):
            return oct(self)

        def __add__(self, other):
            return self.__class__(super(octlong, self).__add__(other))
        __radd__ = __add__
    self.assertEqual(str(octlong(3) + 5), '0o10')
    self.assertEqual(str(5 + octlong(3000)), '0o5675')
    a = octlong(12345)
    self.assertEqual(a, 12345)
    self.assertEqual(int(a), 12345)
    self.assertEqual(hash(a), hash(12345))
    self.assertIs(int(a).__class__, int)
    self.assertIs((+a).__class__, int)
    self.assertIs((-a).__class__, int)
    self.assertIs((-octlong(0)).__class__, int)
    self.assertIs((a >> 0).__class__, int)
    self.assertIs((a << 0).__class__, int)
    self.assertIs((a - 0).__class__, int)
    self.assertIs((a * 1).__class__, int)
    self.assertIs((a ** 1).__class__, int)
    self.assertIs((a // 1).__class__, int)
    self.assertIs((1 * a).__class__, int)
    self.assertIs((a | 0).__class__, int)
    self.assertIs((a ^ 0).__class__, int)
    self.assertIs((a & -1).__class__, int)
    self.assertIs((octlong(0) << 12).__class__, int)
    self.assertIs((octlong(0) >> 12).__class__, int)
    self.assertIs(abs(octlong(0)).__class__, int)

    class longclone(int):
        pass
    a = longclone(1)
    self.assertIs((a + 0).__class__, int)
    self.assertIs((0 + a).__class__, int)
    a = longclone(-1)
    self.assertEqual(a.__dict__, {})
    self.assertEqual(int(a), -1)

    class precfloat(float):
        __slots__ = ['prec']

        def __init__(self, value=0.0, prec=12):
            self.prec = int(prec)

        def __repr__(self):
            return '%.*g' % (self.prec, self)
    self.assertEqual(repr(precfloat(1.1)), '1.1')
    a = precfloat(12345)
    self.assertEqual(a, 12345.0)
    self.assertEqual(float(a), 12345.0)
    self.assertIs(float(a).__class__, float)
    self.assertEqual(hash(a), hash(12345.0))
    self.assertIs((+a).__class__, float)

    class madcomplex(complex):

        def __repr__(self):
            return '%.17gj%+.17g' % (self.imag, self.real)
    a = madcomplex(-3, 4)
    self.assertEqual(repr(a), '4j-3')
    base = complex(-3, 4)
    self.assertEqual(base.__class__, complex)
    self.assertEqual(a, base)
    self.assertEqual(complex(a), base)
    self.assertEqual(complex(a).__class__, complex)
    a = madcomplex(a)
    self.assertEqual(repr(a), '4j-3')
    self.assertEqual(a, base)
    self.assertEqual(complex(a), base)
    self.assertEqual(complex(a).__class__, complex)
    self.assertEqual(hash(a), hash(base))
    self.assertEqual((+a).__class__, complex)
    self.assertEqual((a + 0).__class__, complex)
    self.assertEqual(a + 0, base)
    self.assertEqual((a - 0).__class__, complex)
    self.assertEqual(a - 0, base)
    self.assertEqual((a * 1).__class__, complex)
    self.assertEqual(a * 1, base)
    self.assertEqual((a / 1).__class__, complex)
    self.assertEqual(a / 1, base)

    class madtuple(tuple):
        _rev = None

        def rev(self):
            if self._rev is not None:
                return self._rev
            L = list(self)
            L.reverse()
            self._rev = self.__class__(L)
            return self._rev
    a = madtuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
    self.assertEqual(a, (1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
    self.assertEqual(a.rev(), madtuple((0, 9, 8, 7, 6, 5, 4, 3, 2, 1)))
    self.assertEqual(a.rev().rev(), madtuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 0)))
    for i in range(512):
        t = madtuple(range(i))
        u = t.rev()
        v = u.rev()
        self.assertEqual(v, t)
    a = madtuple((1, 2, 3, 4, 5))
    self.assertEqual(tuple(a), (1, 2, 3, 4, 5))
    self.assertIs(tuple(a).__class__, tuple)
    self.assertEqual(hash(a), hash((1, 2, 3, 4, 5)))
    self.assertIs(a[:].__class__, tuple)
    self.assertIs((a * 1).__class__, tuple)
    self.assertIs((a * 0).__class__, tuple)
    self.assertIs((a + ()).__class__, tuple)
    a = madtuple(())
    self.assertEqual(tuple(a), ())
    self.assertIs(tuple(a).__class__, tuple)
    self.assertIs((a + a).__class__, tuple)
    self.assertIs((a * 0).__class__, tuple)
    self.assertIs((a * 1).__class__, tuple)
    self.assertIs((a * 2).__class__, tuple)
    self.assertIs(a[:].__class__, tuple)

    class madstring(str):
        _rev = None

        def rev(self):
            if self._rev is not None:
                return self._rev
            L = list(self)
            L.reverse()
            self._rev = self.__class__(''.join(L))
            return self._rev
    s = madstring('abcdefghijklmnopqrstuvwxyz')
    self.assertEqual(s, 'abcdefghijklmnopqrstuvwxyz')
    self.assertEqual(s.rev(), madstring('zyxwvutsrqponmlkjihgfedcba'))
    self.assertEqual(s.rev().rev(), madstring('abcdefghijklmnopqrstuvwxyz'))
    for i in range(256):
        s = madstring(''.join(map(chr, range(i))))
        t = s.rev()
        u = t.rev()
        self.assertEqual(u, s)
    s = madstring('12345')
    self.assertEqual(str(s), '12345')
    self.assertIs(str(s).__class__, str)
    base = '\x00' * 5
    s = madstring(base)
    self.assertEqual(s, base)
    self.assertEqual(str(s), base)
    self.assertIs(str(s).__class__, str)
    self.assertEqual(hash(s), hash(base))
    self.assertEqual({s: 1}[base], 1)
    self.assertEqual({base: 1}[s], 1)
    self.assertIs((s + '').__class__, str)
    self.assertEqual(s + '', base)
    self.assertIs(('' + s).__class__, str)
    self.assertEqual('' + s, base)
    self.assertIs((s * 0).__class__, str)
    self.assertEqual(s * 0, '')
    self.assertIs((s * 1).__class__, str)
    self.assertEqual(s * 1, base)
    self.assertIs((s * 2).__class__, str)
    self.assertEqual(s * 2, base + base)
    self.assertIs(s[:].__class__, str)
    self.assertEqual(s[:], base)
    self.assertIs(s[0:0].__class__, str)
    self.assertEqual(s[0:0], '')
    self.assertIs(s.strip().__class__, str)
    self.assertEqual(s.strip(), base)
    self.assertIs(s.lstrip().__class__, str)
    self.assertEqual(s.lstrip(), base)
    self.assertIs(s.rstrip().__class__, str)
    self.assertEqual(s.rstrip(), base)
    identitytab = {}
    self.assertIs(s.translate(identitytab).__class__, str)
    self.assertEqual(s.translate(identitytab), base)
    self.assertIs(s.replace('x', 'x').__class__, str)
    self.assertEqual(s.replace('x', 'x'), base)
    self.assertIs(s.ljust(len(s)).__class__, str)
    self.assertEqual(s.ljust(len(s)), base)
    self.assertIs(s.rjust(len(s)).__class__, str)
    self.assertEqual(s.rjust(len(s)), base)
    self.assertIs(s.center(len(s)).__class__, str)
    self.assertEqual(s.center(len(s)), base)
    self.assertIs(s.lower().__class__, str)
    self.assertEqual(s.lower(), base)

    class madunicode(str):
        _rev = None

        def rev(self):
            if self._rev is not None:
                return self._rev
            L = list(self)
            L.reverse()
            self._rev = self.__class__(''.join(L))
            return self._rev
    u = madunicode('ABCDEF')
    self.assertEqual(u, 'ABCDEF')
    self.assertEqual(u.rev(), madunicode('FEDCBA'))
    self.assertEqual(u.rev().rev(), madunicode('ABCDEF'))
    base = '12345'
    u = madunicode(base)
    self.assertEqual(str(u), base)
    self.assertIs(str(u).__class__, str)
    self.assertEqual(hash(u), hash(base))
    self.assertEqual({u: 1}[base], 1)
    self.assertEqual({base: 1}[u], 1)
    self.assertIs(u.strip().__class__, str)
    self.assertEqual(u.strip(), base)
    self.assertIs(u.lstrip().__class__, str)
    self.assertEqual(u.lstrip(), base)
    self.assertIs(u.rstrip().__class__, str)
    self.assertEqual(u.rstrip(), base)
    self.assertIs(u.replace('x', 'x').__class__, str)
    self.assertEqual(u.replace('x', 'x'), base)
    self.assertIs(u.replace('xy', 'xy').__class__, str)
    self.assertEqual(u.replace('xy', 'xy'), base)
    self.assertIs(u.center(len(u)).__class__, str)
    self.assertEqual(u.center(len(u)), base)
    self.assertIs(u.ljust(len(u)).__class__, str)
    self.assertEqual(u.ljust(len(u)), base)
    self.assertIs(u.rjust(len(u)).__class__, str)
    self.assertEqual(u.rjust(len(u)), base)
    self.assertIs(u.lower().__class__, str)
    self.assertEqual(u.lower(), base)
    self.assertIs(u.upper().__class__, str)
    self.assertEqual(u.upper(), base)
    self.assertIs(u.capitalize().__class__, str)
    self.assertEqual(u.capitalize(), base)
    self.assertIs(u.title().__class__, str)
    self.assertEqual(u.title(), base)
    self.assertIs((u + '').__class__, str)
    self.assertEqual(u + '', base)
    self.assertIs(('' + u).__class__, str)
    self.assertEqual('' + u, base)
    self.assertIs((u * 0).__class__, str)
    self.assertEqual(u * 0, '')
    self.assertIs((u * 1).__class__, str)
    self.assertEqual(u * 1, base)
    self.assertIs((u * 2).__class__, str)
    self.assertEqual(u * 2, base + base)
    self.assertIs(u[:].__class__, str)
    self.assertEqual(u[:], base)
    self.assertIs(u[0:0].__class__, str)
    self.assertEqual(u[0:0], '')

    class sublist(list):
        pass
    a = sublist(range(5))
    self.assertEqual(a, list(range(5)))
    a.append('hello')
    self.assertEqual(a, list(range(5)) + ['hello'])
    a[5] = 5
    self.assertEqual(a, list(range(6)))
    a.extend(range(6, 20))
    self.assertEqual(a, list(range(20)))
    a[-5:] = []
    self.assertEqual(a, list(range(15)))
    del a[10:15]
    self.assertEqual(len(a), 10)
    self.assertEqual(a, list(range(10)))
    self.assertEqual(list(a), list(range(10)))
    self.assertEqual(a[0], 0)
    self.assertEqual(a[9], 9)
    self.assertEqual(a[-10], 0)
    self.assertEqual(a[-1], 9)
    self.assertEqual(a[:5], list(range(5)))
