# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestRepr_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class B:
        x: int

    @dataclass
    class C(B):
        y: int = 10
    o = C(4)
    self.assertEqual(repr(o), 'TestRepr.test_repr.<locals>.C(x=4, y=10)')

    @dataclass
    class D(C):
        x: int = 20
    self.assertEqual(repr(D()), 'TestRepr.test_repr.<locals>.D(x=20, y=10)')

    @dataclass
    class C:

        @dataclass
        class D:
            i: int

        @dataclass
        class E:
            pass
    self.assertEqual(repr(C.D(0)), 'TestRepr.test_repr.<locals>.C.D(i=0)')
    self.assertEqual(repr(C.E()), 'TestRepr.test_repr.<locals>.C.E()')
