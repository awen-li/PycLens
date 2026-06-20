# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_init_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X(typing.Generic[T]):

        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            cls.attr = 42

    class Y(X):
        pass
    self.assertEqual(Y.attr, 42)
    with self.assertRaises(AttributeError):
        X.attr
    X.attr = 1
    Y.attr = 2

    class Z(Y):
        pass

    class W(X[int]):
        pass
    self.assertEqual(Y.attr, 2)
    self.assertEqual(Z.attr, 42)
    self.assertEqual(W.attr, 42)
