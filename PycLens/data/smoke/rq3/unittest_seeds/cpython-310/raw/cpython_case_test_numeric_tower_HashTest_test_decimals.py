# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_numeric_tower.py
# case: HashTest_test_decimals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zeros = ['0', '-0', '0.0', '-0.0e10', '000e-10']
    for zero in zeros:
        self.check_equal_hash(D(zero), D(0))
    self.check_equal_hash(D('1.00'), D(1))
    self.check_equal_hash(D('1.00000'), D(1))
    self.check_equal_hash(D('-1.00'), D(-1))
    self.check_equal_hash(D('-1.00000'), D(-1))
    self.check_equal_hash(D('123e2'), D(12300))
    self.check_equal_hash(D('1230e1'), D(12300))
    self.check_equal_hash(D('12300'), D(12300))
    self.check_equal_hash(D('12300.0'), D(12300))
    self.check_equal_hash(D('12300.00'), D(12300))
    self.check_equal_hash(D('12300.000'), D(12300))
