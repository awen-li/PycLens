# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_new_with_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(Generic[T]):
        pass

    class B:

        def __new__(cls, arg):
            obj = super().__new__(cls)
            obj.arg = arg
            return obj

    class C(A, B):
        pass
    c = C('foo')
    self.assertEqual(c.arg, 'foo')
