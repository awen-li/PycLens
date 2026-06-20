# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestVec2D_test_rotate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cases = [(((0, 0), 0), (0, 0)), (((0, 1), 90), (-1, 0)), (((0, 1), -90), (1, 0)), (((1, 0), 180), (-1, 0)), (((1, 0), 360), (1, 0))]
    for case in cases:
        with self.subTest(case=case):
            ((vec, rot), expected) = case
            vec = Vec2D(*vec)
            got = vec.rotate(rot)
            self.assertVectorsAlmostEqual(got, expected)
