# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_new_no_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(Generic[T]):
        pass
    with self.assertRaises(TypeError):
        A('foo')

    class B:

        def __new__(cls):
            obj = super().__new__(cls)
            obj.from_b = 'b'
            return obj

    class C(A, B):

        def __init__(self, arg):
            self.arg = arg

        def __new__(cls, arg):
            obj = super().__new__(cls)
            obj.from_c = 'c'
            return obj
    c = C('foo')
    self.assertEqual(c.arg, 'foo')
    self.assertEqual(c.from_b, 'b')
    self.assertEqual(c.from_c, 'c')
