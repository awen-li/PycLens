# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_hashable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    S = inspect.Signature
    P = inspect.Parameter

    def foo(a):
        pass
    foo_sig = inspect.signature(foo)
    manual_sig = S(parameters=[P('a', P.POSITIONAL_OR_KEYWORD)])
    self.assertEqual(hash(foo_sig), hash(manual_sig))
    self.assertNotEqual(hash(foo_sig), hash(manual_sig.replace(return_annotation='spam')))

    def bar(a) -> 1:
        pass
    self.assertNotEqual(hash(foo_sig), hash(inspect.signature(bar)))

    def foo(a={}):
        pass
    with self.assertRaisesRegex(TypeError, 'unhashable type'):
        hash(inspect.signature(foo))

    def foo(a) -> {}:
        pass
    with self.assertRaisesRegex(TypeError, 'unhashable type'):
        hash(inspect.signature(foo))
