# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_divmod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(divmod(12, 7), (1, 5))
    self.assertEqual(divmod(-12, 7), (-2, 2))
    self.assertEqual(divmod(12, -7), (-2, -2))
    self.assertEqual(divmod(-12, -7), (1, -5))
    self.assertEqual(divmod(-sys.maxsize - 1, -1), (sys.maxsize + 1, 0))
    for (num, denom, exp_result) in [(3.25, 1.0, (3.0, 0.25)), (-3.25, 1.0, (-4.0, 0.75)), (3.25, -1.0, (-4.0, -0.75)), (-3.25, -1.0, (3.0, -0.25))]:
        result = divmod(num, denom)
        self.assertAlmostEqual(result[0], exp_result[0])
        self.assertAlmostEqual(result[1], exp_result[1])
    self.assertRaises(TypeError, divmod)
