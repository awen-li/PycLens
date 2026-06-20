# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: ReprTests_test_descriptors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(repr(dict.items), "<method 'items' of 'dict' objects>")

    class C:

        def foo(cls):
            pass
    x = staticmethod(C.foo)
    self.assertEqual(repr(x), f'<staticmethod({C.foo!r})>')
    x = classmethod(C.foo)
    self.assertEqual(repr(x), f'<classmethod({C.foo!r})>')
