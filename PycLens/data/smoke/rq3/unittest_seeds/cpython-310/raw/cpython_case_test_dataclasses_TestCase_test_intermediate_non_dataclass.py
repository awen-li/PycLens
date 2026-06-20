# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_intermediate_non_dataclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class A:
        x: int

    class B(A):
        y: int

    @dataclass
    class C(B):
        z: int
    c = C(1, 3)
    self.assertEqual((c.x, c.z), (1, 3))
    with self.assertRaisesRegex(AttributeError, 'object has no attribute'):
        c.y

    class D(C):
        t: int
    d = D(4, 5)
    self.assertEqual((d.x, d.z), (4, 5))
