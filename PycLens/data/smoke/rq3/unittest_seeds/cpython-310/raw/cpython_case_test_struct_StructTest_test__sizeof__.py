# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test__sizeof__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for code in integer_codes:
        self.check_sizeof(code, 1)
    self.check_sizeof('BHILfdspP', 9)
    self.check_sizeof('B' * 1234, 1234)
    self.check_sizeof('fd', 2)
    self.check_sizeof('xxxxxxxxxxxxxx', 0)
    self.check_sizeof('100H', 1)
    self.check_sizeof('187s', 1)
    self.check_sizeof('20p', 1)
    self.check_sizeof('0s', 1)
    self.check_sizeof('0c', 0)
