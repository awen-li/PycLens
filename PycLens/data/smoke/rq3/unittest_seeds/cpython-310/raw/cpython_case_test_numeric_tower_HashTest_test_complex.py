# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_numeric_tower.py
# case: HashTest_test_complex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_values = [0.0, -0.0, 1.0, -1.0, 0.40625, -5136.5, float('inf'), float('-inf')]
    for zero in (-0.0, 0.0):
        for value in test_values:
            self.check_equal_hash(value, complex(value, zero))
