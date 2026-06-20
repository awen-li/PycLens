# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_partial

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from functools import partial
    Parameter = inspect.Parameter

    def test():
        pass
    self.assertEqual(self.signature(partial(test)), ((), ...))
    with self.assertRaisesRegex(ValueError, 'has incorrect arguments'):
        inspect.signature(partial(test, 1))
    with self.assertRaisesRegex(ValueError, 'has incorrect arguments'):
        inspect.signature(partial(test, a=1))

    def test(a, b, *, c, d):
        pass
    self.assertEqual(self.signature(partial(test)), ((('a', ..., ..., 'positional_or_keyword'), ('b', ..., ..., 'positional_or_keyword'), ('c', ..., ..., 'keyword_only'), ('d', ..., ..., 'keyword_only')), ...))
    self.assertEqual(self.signature(partial(test, 1)), ((('b', ..., ..., 'positional_or_keyword'), ('c', ..., ..., 'keyword_only'), ('d', ..., ..., 'keyword_only')), ...))
    self.assertEqual(self.signature(partial(test, 1, c=2)), ((('b', ..., ..., 'positional_or_keyword'), ('c', 2, ..., 'keyword_only'), ('d', ..., ..., 'keyword_only')), ...))
    self.assertEqual(self.signature(partial(test, b=1, c=2)), ((('a', ..., ..., 'positional_or_keyword'), ('b', 1, ..., 'keyword_only'), ('c', 2, ..., 'keyword_only'), ('d', ..., ..., 'keyword_only')), ...))
    self.assertEqual(self.signature(partial(test, 0, b=1, c=2)), ((('b', 1, ..., 'keyword_only'), ('c', 2, ..., 'keyword_only'), ('d', ..., ..., 'keyword_only')), ...))
    self.assertEqual(self.signature(partial(test, a=1)), ((('a', 1, ..., 'keyword_only'), ('b', ..., ..., 'keyword_only'), ('c', ..., ..., 'keyword_only'), ('d', ..., ..., 'keyword_only')), ...))

    def test(a, *args, b, **kwargs):
        pass
    self.assertEqual(self.signature(partial(test, 1)), ((('args', ..., ..., 'var_positional'), ('b', ..., ..., 'keyword_only'), ('kwargs', ..., ..., 'var_keyword')), ...))
    self.assertEqual(self.signature(partial(test, a=1)), ((('a', 1, ..., 'keyword_only'), ('b', ..., ..., 'keyword_only'), ('kwargs', ..., ..., 'var_keyword')), ...))
    self.assertEqual(self.signature(partial(test, 1, 2, 3)), ((('args', ..., ..., 'var_positional'), ('b', ..., ..., 'keyword_only'), ('kwargs', ..., ..., 'var_keyword')), ...))
    self.assertEqual(self.signature(partial(test, 1, 2, 3, test=True)), ((('args', ..., ..., 'var_positional'), ('b', ..., ..., 'keyword_only'), ('kwargs', ..., ..., 'var_keyword')), ...))
    self.assertEqual(self.signature(partial(test, 1, 2, 3, test=1, b=0)), ((('args', ..., ..., 'var_positional'), ('b', 0, ..., 'keyword_only'), ('kwargs', ..., ..., 'var_keyword')), ...))
    self.assertEqual(self.signature(partial(test, b=0)), ((('a', ..., ..., 'positional_or_keyword'), ('args', ..., ..., 'var_positional'), ('b', 0, ..., 'keyword_only'), ('kwargs', ..., ..., 'var_keyword')), ...))
    self.assertEqual(self.signature(partial(test, b=0, test=1)), ((('a', ..., ..., 'positional_or_keyword'), ('args', ..., ..., 'var_positional'), ('b', 0, ..., 'keyword_only'), ('kwargs', ..., ..., 'var_keyword')), ...))

    def test(a, b, c: int) -> 42:
        pass
    sig = test.__signature__ = inspect.signature(test)
    self.assertEqual(self.signature(partial(partial(test, 1))), ((('b', ..., ..., 'positional_or_keyword'), ('c', ..., int, 'positional_or_keyword')), 42))
    self.assertEqual(self.signature(partial(partial(test, 1), 2)), ((('c', ..., int, 'positional_or_keyword'),), 42))
    psig = inspect.signature(partial(partial(test, 1), 2))

    def foo(a):
        return a
    _foo = partial(partial(foo, a=10), a=20)
    self.assertEqual(self.signature(_foo), ((('a', 20, ..., 'keyword_only'),), ...))
    self.assertEqual(_foo(), 20)

    def foo(a, b, c):
        return (a, b, c)
    _foo = partial(partial(foo, 1, b=20), b=30)
    self.assertEqual(self.signature(_foo), ((('b', 30, ..., 'keyword_only'), ('c', ..., ..., 'keyword_only')), ...))
    self.assertEqual(_foo(c=10), (1, 30, 10))

    def foo(a, b, c, *, d):
        return (a, b, c, d)
    _foo = partial(partial(foo, d=20, c=20), b=10, d=30)
    self.assertEqual(self.signature(_foo), ((('a', ..., ..., 'positional_or_keyword'), ('b', 10, ..., 'keyword_only'), ('c', 20, ..., 'keyword_only'), ('d', 30, ..., 'keyword_only')), ...))
    ba = inspect.signature(_foo).bind(a=200, b=11)
    self.assertEqual(_foo(*ba.args, **ba.kwargs), (200, 11, 20, 30))

    def foo(a=1, b=2, c=3):
        return (a, b, c)
    _foo = partial(foo, c=13)
    ba = inspect.signature(_foo).bind(a=11)
    self.assertEqual(_foo(*ba.args, **ba.kwargs), (11, 2, 13))
    ba = inspect.signature(_foo).bind(11, 12)
    self.assertEqual(_foo(*ba.args, **ba.kwargs), (11, 12, 13))
    ba = inspect.signature(_foo).bind(11, b=12)
    self.assertEqual(_foo(*ba.args, **ba.kwargs), (11, 12, 13))
    ba = inspect.signature(_foo).bind(b=12)
    self.assertEqual(_foo(*ba.args, **ba.kwargs), (1, 12, 13))
    _foo = partial(_foo, b=10, c=20)
    ba = inspect.signature(_foo).bind(12)
    self.assertEqual(_foo(*ba.args, **ba.kwargs), (12, 10, 20))

    def foo(a, b, c, d, **kwargs):
        pass
    sig = inspect.signature(foo)
    params = sig.parameters.copy()
    params['a'] = params['a'].replace(kind=Parameter.POSITIONAL_ONLY)
    params['b'] = params['b'].replace(kind=Parameter.POSITIONAL_ONLY)
    foo.__signature__ = inspect.Signature(params.values())
    sig = inspect.signature(foo)
    self.assertEqual(str(sig), '(a, b, /, c, d, **kwargs)')
    self.assertEqual(self.signature(partial(foo, 1)), ((('b', ..., ..., 'positional_only'), ('c', ..., ..., 'positional_or_keyword'), ('d', ..., ..., 'positional_or_keyword'), ('kwargs', ..., ..., 'var_keyword')), ...))
    self.assertEqual(self.signature(partial(foo, 1, 2)), ((('c', ..., ..., 'positional_or_keyword'), ('d', ..., ..., 'positional_or_keyword'), ('kwargs', ..., ..., 'var_keyword')), ...))
    self.assertEqual(self.signature(partial(foo, 1, 2, 3)), ((('d', ..., ..., 'positional_or_keyword'), ('kwargs', ..., ..., 'var_keyword')), ...))
    self.assertEqual(self.signature(partial(foo, 1, 2, c=3)), ((('c', 3, ..., 'keyword_only'), ('d', ..., ..., 'keyword_only'), ('kwargs', ..., ..., 'var_keyword')), ...))
    self.assertEqual(self.signature(partial(foo, 1, c=3)), ((('b', ..., ..., 'positional_only'), ('c', 3, ..., 'keyword_only'), ('d', ..., ..., 'keyword_only'), ('kwargs', ..., ..., 'var_keyword')), ...))
