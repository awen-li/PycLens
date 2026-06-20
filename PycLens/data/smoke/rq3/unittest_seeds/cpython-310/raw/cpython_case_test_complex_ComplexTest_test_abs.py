# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_abs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nums = [complex(x / 3.0, y / 7.0) for x in range(-9, 9) for y in range(-9, 9)]
    for num in nums:
        self.assertAlmostEqual((num.real ** 2 + num.imag ** 2) ** 0.5, abs(num))
