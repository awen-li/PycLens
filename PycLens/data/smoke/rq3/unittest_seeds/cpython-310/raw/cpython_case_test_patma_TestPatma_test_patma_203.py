# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_203

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Parent:
        __match_args__ = ('a', 'b')

    class Child(Parent):
        __match_args__ = ('c', 'd')
    c = Child()
    c.a = 0
    c.b = 1
    match c:
        case Parent(x, b=y):
            z = 0
    self.assertIs(x, c.a)
    self.assertIs(y, c.b)
    self.assertEqual(z, 0)
