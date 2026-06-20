# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_funcdef

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f1():
        pass
    f1()
    f1(*())
    f1(*(), **{})

    def f2(one_argument):
        pass

    def f3(two, arguments):
        pass
    self.assertEqual(f2.__code__.co_varnames, ('one_argument',))
    self.assertEqual(f3.__code__.co_varnames, ('two', 'arguments'))

    def a1(one_arg):
        pass

    def a2(two, args):
        pass

    def v0(*rest):
        pass

    def v1(a, *rest):
        pass

    def v2(a, b, *rest):
        pass
    f1()
    f2(1)
    f2(1)
    f3(1, 2)
    f3(1, 2)
    v0()
    v0(1)
    v0(1)
    v0(1, 2)
    v0(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    v1(1)
    v1(1)
    v1(1, 2)
    v1(1, 2, 3)
    v1(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    v2(1, 2)
    v2(1, 2, 3)
    v2(1, 2, 3, 4)
    v2(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

    def d01(a=1):
        pass
    d01()
    d01(1)
    d01(*(1,))
    d01(*([] or [2]))
    d01(*(() or ()), *({} and ()), **() or {})
    d01(**{'a': 2})
    d01(**{'a': 2} or {})

    def d11(a, b=1):
        pass
    d11(1)
    d11(1, 2)
    d11(1, **{'b': 2})

    def d21(a, b, c=1):
        pass
    d21(1, 2)
    d21(1, 2, 3)
    d21(*(1, 2, 3))
    d21(1, *(2, 3))
    d21(1, 2, *(3,))
    d21(1, 2, **{'c': 3})

    def d02(a=1, b=2):
        pass
    d02()
    d02(1)
    d02(1, 2)
    d02(*(1, 2))
    d02(1, *(2,))
    d02(1, **{'b': 2})
    d02(**{'a': 1, 'b': 2})

    def d12(a, b=1, c=2):
        pass
    d12(1)
    d12(1, 2)
    d12(1, 2, 3)

    def d22(a, b, c=1, d=2):
        pass
    d22(1, 2)
    d22(1, 2, 3)
    d22(1, 2, 3, 4)

    def d01v(a=1, *rest):
        pass
    d01v()
    d01v(1)
    d01v(1, 2)
    d01v(*(1, 2, 3, 4))
    d01v(*(1,))
    d01v(**{'a': 2})

    def d11v(a, b=1, *rest):
        pass
    d11v(1)
    d11v(1, 2)
    d11v(1, 2, 3)

    def d21v(a, b, c=1, *rest):
        pass
    d21v(1, 2)
    d21v(1, 2, 3)
    d21v(1, 2, 3, 4)
    d21v(*(1, 2, 3, 4))
    d21v(1, 2, **{'c': 3})

    def d02v(a=1, b=2, *rest):
        pass
    d02v()
    d02v(1)
    d02v(1, 2)
    d02v(1, 2, 3)
    d02v(1, *(2, 3, 4))
    d02v(**{'a': 1, 'b': 2})

    def d12v(a, b=1, c=2, *rest):
        pass
    d12v(1)
    d12v(1, 2)
    d12v(1, 2, 3)
    d12v(1, 2, 3, 4)
    d12v(*(1, 2, 3, 4))
    d12v(1, 2, *(3, 4, 5))
    d12v(1, *(2,), **{'c': 3})

    def d22v(a, b, c=1, d=2, *rest):
        pass
    d22v(1, 2)
    d22v(1, 2, 3)
    d22v(1, 2, 3, 4)
    d22v(1, 2, 3, 4, 5)
    d22v(*(1, 2, 3, 4))
    d22v(1, 2, *(3, 4, 5))
    d22v(1, *(2, 3), **{'d': 4})
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', BytesWarning)
        try:
            str('x', **{b'foo': 1})
        except TypeError:
            pass
        else:
            self.fail('Bytes should not work as keyword argument names')

    def pos0key1(*, key):
        return key
    pos0key1(key=100)

    def pos2key2(p1, p2, *, k1, k2=100):
        return (p1, p2, k1, k2)
    pos2key2(1, 2, k1=100)
    pos2key2(1, 2, k1=100, k2=200)
    pos2key2(1, 2, k2=100, k1=200)

    def pos2key2dict(p1, p2, *, k1=100, k2, **kwarg):
        return (p1, p2, k1, k2, kwarg)
    pos2key2dict(1, 2, k2=100, tokwarg1=100, tokwarg2=200)
    pos2key2dict(1, 2, tokwarg1=100, tokwarg2=200, k2=100)
    self.assertRaises(SyntaxError, eval, 'def f(*): pass')
    self.assertRaises(SyntaxError, eval, 'def f(*,): pass')
    self.assertRaises(SyntaxError, eval, 'def f(*, **kwds): pass')

    def f(*args, **kwargs):
        return (args, kwargs)
    self.assertEqual(f(1, *[3, 4], x=2, y=5), ((1, 3, 4), {'x': 2, 'y': 5}))
    self.assertEqual(f(1, *(2, 3), 4), ((1, 2, 3, 4), {}))
    self.assertRaises(SyntaxError, eval, 'f(1, x=2, *(3,4), x=5)')
    self.assertEqual(f(**{'eggs': 'scrambled', 'spam': 'fried'}), ((), {'eggs': 'scrambled', 'spam': 'fried'}))
    self.assertEqual(f(spam='fried', **{'eggs': 'scrambled'}), ((), {'eggs': 'scrambled', 'spam': 'fried'}))
    check_syntax_error(self, 'f(*g(1=2))')
    check_syntax_error(self, 'f(**g(1=2))')

    def f(x) -> list:
        pass
    self.assertEqual(f.__annotations__, {'return': list})

    def f(x: int):
        pass
    self.assertEqual(f.__annotations__, {'x': int})

    def f(x: int, /):
        pass
    self.assertEqual(f.__annotations__, {'x': int})

    def f(x: int=34, /):
        pass
    self.assertEqual(f.__annotations__, {'x': int})

    def f(*x: str):
        pass
    self.assertEqual(f.__annotations__, {'x': str})

    def f(**x: float):
        pass
    self.assertEqual(f.__annotations__, {'x': float})

    def f(x, y: 1 + 2):
        pass
    self.assertEqual(f.__annotations__, {'y': 3})

    def f(x, y: 1 + 2, /):
        pass
    self.assertEqual(f.__annotations__, {'y': 3})

    def f(a, b: 1, c: 2, d):
        pass
    self.assertEqual(f.__annotations__, {'b': 1, 'c': 2})

    def f(a, b: 1, /, c: 2, d):
        pass
    self.assertEqual(f.__annotations__, {'b': 1, 'c': 2})

    def f(a, b: 1, c: 2, d, e: 3=4, f=5, *g: 6):
        pass
    self.assertEqual(f.__annotations__, {'b': 1, 'c': 2, 'e': 3, 'g': 6})

    def f(a, b: 1, c: 2, d, e: 3=4, f=5, *g: 6, h: 7, i=8, j: 9=10, **k: 11) -> 12:
        pass
    self.assertEqual(f.__annotations__, {'b': 1, 'c': 2, 'e': 3, 'g': 6, 'h': 7, 'j': 9, 'k': 11, 'return': 12})

    def f(a, b: 1, c: 2, d, e: 3=4, f: int=5, /, *g: 6, h: 7, i=8, j: 9=10, **k: 11) -> 12:
        pass
    self.assertEqual(f.__annotations__, {'b': 1, 'c': 2, 'e': 3, 'f': int, 'g': 6, 'h': 7, 'j': 9, 'k': 11, 'return': 12})

    class Spam:

        def f(self, *, __kw: 1):
            pass

    class Ham(Spam):
        pass
    self.assertEqual(Spam.f.__annotations__, {'_Spam__kw': 1})
    self.assertEqual(Ham.f.__annotations__, {'_Spam__kw': 1})

    def null(x):
        return x

    @null
    def f(x) -> list:
        pass
    self.assertEqual(f.__annotations__, {'return': list})

    @False or null
    def f(x):
        pass

    @(d := null)
    def f(x):
        pass

    @lambda f: null(f)
    def f(x):
        pass

    @[..., null, ...][1]
    def f(x):
        pass

    @null(null)(null)
    def f(x):
        pass

    @[null][0].__call__.__call__
    def f(x):
        pass
    closure = 1

    def f():
        return closure

    def f(x=1):
        return closure

    def f(*, k=1):
        return closure

    def f() -> int:
        return closure

    def f(a):
        pass

    def f(*args):
        pass

    def f(**kwds):
        pass

    def f(a, *args):
        pass

    def f(a, **kwds):
        pass

    def f(*args, b):
        pass

    def f(*, b):
        pass

    def f(*args, **kwds):
        pass

    def f(a, *args, b):
        pass

    def f(a, *, b):
        pass

    def f(a, *args, **kwds):
        pass

    def f(*args, b, **kwds):
        pass

    def f(*, b, **kwds):
        pass

    def f(a, *args, b, **kwds):
        pass

    def f(a, *, b, **kwds):
        pass
