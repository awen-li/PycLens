# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestVec2D_test_vector_multiply

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    vec1 = Vec2D(10, 10)
    vec2 = Vec2D(0.5, 3)
    answer = vec1 * vec2
    expected = 35
    self.assertAlmostEqual(answer, expected)
    vec = Vec2D(0.5, 3)
    expected = Vec2D(5, 30)
    self.assertVectorsAlmostEqual(vec * 10, expected)
    self.assertVectorsAlmostEqual(10 * vec, expected)
    self.assertVectorsAlmostEqual(vec * 10.0, expected)
    self.assertVectorsAlmostEqual(10.0 * vec, expected)
    M = Multiplier()
    self.assertEqual(vec * M, Vec2D(f'{vec[0]}*M', f'{vec[1]}*M'))
    self.assertEqual(M * vec, f'M*{vec}')
