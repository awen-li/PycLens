# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_callable_objects

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo:

        def __call__(self, a):
            pass
    self.assertEqual(self.signature(Foo()), ((('a', ..., ..., 'positional_or_keyword'),), ...))

    class Spam:
        pass
    with self.assertRaisesRegex(TypeError, 'is not a callable object'):
        inspect.signature(Spam())

    class Bar(Spam, Foo):
        pass
    self.assertEqual(self.signature(Bar()), ((('a', ..., ..., 'positional_or_keyword'),), ...))

    class Wrapped:
        pass
    Wrapped.__wrapped__ = lambda a: None
    self.assertEqual(self.signature(Wrapped), ((('a', ..., ..., 'positional_or_keyword'),), ...))
    Wrapped.__wrapped__ = Wrapped
    with self.assertRaisesRegex(ValueError, 'wrapper loop'):
        self.signature(Wrapped)
