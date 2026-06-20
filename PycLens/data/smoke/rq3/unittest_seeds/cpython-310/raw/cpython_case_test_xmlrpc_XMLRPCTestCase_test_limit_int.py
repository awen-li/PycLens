# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_limit_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check = self.check_loads
    maxdigits = 5000
    with support.adjust_int_max_str_digits(maxdigits):
        s = '1' * (maxdigits + 1)
        with self.assertRaises(ValueError):
            check(f'<int>{s}</int>', None)
        with self.assertRaises(ValueError):
            check(f'<biginteger>{s}</biginteger>', None)
