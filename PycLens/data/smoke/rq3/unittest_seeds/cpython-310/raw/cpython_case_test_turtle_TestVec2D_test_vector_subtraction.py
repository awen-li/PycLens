# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestVec2D_test_vector_subtraction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_cases = [(((0, 0), (1, 1)), (-1, -1)), (((10.625, 0.125), (10, 0)), (0.625, 0.125))]
    self._assert_arithmetic_cases(test_cases, lambda x, y: x - y)
