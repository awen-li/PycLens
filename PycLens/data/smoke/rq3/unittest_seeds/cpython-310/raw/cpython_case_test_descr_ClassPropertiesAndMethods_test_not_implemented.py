# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_not_implemented

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import operator

    def specialmethod(self, other):
        return NotImplemented

    def check(expr, x, y):
        try:
            exec(expr, {'x': x, 'y': y, 'operator': operator})
        except TypeError:
            pass
        else:
            self.fail('no TypeError from %r' % (expr,))
    N1 = sys.maxsize + 1
    N2 = sys.maxsize
    for (name, expr, iexpr) in [('__add__', 'x + y', 'x += y'), ('__sub__', 'x - y', 'x -= y'), ('__mul__', 'x * y', 'x *= y'), ('__matmul__', 'x @ y', 'x @= y'), ('__truediv__', 'x / y', 'x /= y'), ('__floordiv__', 'x // y', 'x //= y'), ('__mod__', 'x % y', 'x %= y'), ('__divmod__', 'divmod(x, y)', None), ('__pow__', 'x ** y', 'x **= y'), ('__lshift__', 'x << y', 'x <<= y'), ('__rshift__', 'x >> y', 'x >>= y'), ('__and__', 'x & y', 'x &= y'), ('__or__', 'x | y', 'x |= y'), ('__xor__', 'x ^ y', 'x ^= y')]:
        rname = '__r' + name[2:]
        A = type('A', (), {name: specialmethod})
        a = A()
        check(expr, a, a)
        check(expr, a, N1)
        check(expr, a, N2)
        if iexpr:
            check(iexpr, a, a)
            check(iexpr, a, N1)
            check(iexpr, a, N2)
            iname = '__i' + name[2:]
            C = type('C', (), {iname: specialmethod})
            c = C()
            check(iexpr, c, a)
            check(iexpr, c, N1)
            check(iexpr, c, N2)
