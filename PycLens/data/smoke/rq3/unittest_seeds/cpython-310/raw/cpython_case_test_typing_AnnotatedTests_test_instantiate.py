# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: AnnotatedTests_test_instantiate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        classvar = 4

        def __init__(self, x):
            self.x = x

        def __eq__(self, other):
            if not isinstance(other, C):
                return NotImplemented
            return other.x == self.x
    A = Annotated[C, 'a decoration']
    a = A(5)
    c = C(5)
    self.assertEqual(a, c)
    self.assertEqual(a.x, c.x)
    self.assertEqual(a.classvar, c.classvar)
