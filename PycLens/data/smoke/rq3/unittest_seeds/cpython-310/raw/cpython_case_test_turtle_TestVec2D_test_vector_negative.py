# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestVec2D_test_vector_negative

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    vec = Vec2D(10, -10)
    expected = (-10, 10)
    self.assertVectorsAlmostEqual(-vec, expected)
