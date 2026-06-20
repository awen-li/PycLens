# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestParseNumber_test_parse_num_ok

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(_parse_num('0', int), 0)
    self.assertEqual(_parse_num('0x10', int), 16)
    self.assertEqual(_parse_num('0XA', int), 10)
    self.assertEqual(_parse_num('010', int), 8)
    self.assertEqual(_parse_num('0b11', int), 3)
    self.assertEqual(_parse_num('0b', int), 0)
