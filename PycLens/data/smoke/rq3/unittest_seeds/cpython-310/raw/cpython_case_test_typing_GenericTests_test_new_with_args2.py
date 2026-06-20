# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_new_with_args2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def __init__(self, arg):
            self.from_a = arg
            super().__init__()

    class C(Generic[T], A):

        def __init__(self, arg):
            self.from_c = arg
            super().__init__(arg)
    c = C('foo')
    self.assertEqual(c.from_a, 'foo')
    self.assertEqual(c.from_c, 'foo')
