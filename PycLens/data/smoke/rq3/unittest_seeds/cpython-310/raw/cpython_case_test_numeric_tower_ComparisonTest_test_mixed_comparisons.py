# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_numeric_tower.py
# case: ComparisonTest_test_mixed_comparisons

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_values = [float('-inf'), D('-1e425000000'), -1e+308, F(-22, 7), -3.14, -2, 0.0, 1e-320, True, F('1.2'), D('1.3'), float('1.4'), F(275807, 195025), D('1.414213562373095048801688724'), F(114243, 80782), F(473596569, 84615), 7e+200, D('infinity')]
    for (i, first) in enumerate(test_values):
        for second in test_values[i + 1:]:
            self.assertLess(first, second)
            self.assertLessEqual(first, second)
            self.assertGreater(second, first)
            self.assertGreaterEqual(second, first)
