# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestBoundArguments_test_signature_bound_arguments_apply_defaults

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo(a, b=1, *args, c: 1={}, **kw):
        pass
    sig = inspect.signature(foo)
    ba = sig.bind(20)
    ba.apply_defaults()
    self.assertEqual(list(ba.arguments.items()), [('a', 20), ('b', 1), ('args', ()), ('c', {}), ('kw', {})])
    ba = sig.bind(10, 20, 30, d=1)
    ba.apply_defaults()
    self.assertEqual(list(ba.arguments.items()), [('a', 10), ('b', 20), ('args', (30,)), ('c', {}), ('kw', {'d': 1})])

    def foo(a, b):
        pass
    sig = inspect.signature(foo)
    ba = sig.bind_partial(20)
    ba.apply_defaults()
    self.assertEqual(list(ba.arguments.items()), [('a', 20)])

    def foo():
        pass
    sig = inspect.signature(foo)
    ba = sig.bind()
    ba.apply_defaults()
    self.assertEqual(list(ba.arguments.items()), [])

    def foo(a='spam'):
        pass
    sig = inspect.signature(foo)
    ba = sig.bind()
    ba.apply_defaults()
    self.assertEqual(list(ba.arguments.items()), [('a', 'spam')])
