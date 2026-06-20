# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestInit_test_inherit_from_protocol

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class P(Protocol):
        a: int

    @dataclass
    class C(P):
        a: int
    self.assertEqual(C(5).a, 5)

    @dataclass
    class D(P):

        def __init__(self, a):
            self.a = a * 2
    self.assertEqual(D(5).a, 10)
