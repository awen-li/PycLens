# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_load_extension_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check = self.check_loads
    check('<nil/>', None)
    check('<ex:nil/>', None)
    check('<i1>205</i1>', 205)
    check('<i2>20561</i2>', 20561)
    check('<i8>9876543210</i8>', 9876543210)
    check('<biginteger>98765432100123456789</biginteger>', 98765432100123456789)
    check('<float>93.78125</float>', 93.78125)
    check('<bigdecimal>9876543210.0123456789</bigdecimal>', decimal.Decimal('9876543210.0123456789'))
