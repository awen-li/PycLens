# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestParseNumber_test_parse_num_fail

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(_parse_num, ('', int), {}, ValueError, re.compile("invalid literal for int().*: '?'?"))
    self.assertRaises(_parse_num, ('0xOoops', int), {}, ValueError, re.compile("invalid literal for int().*: s?'?0xOoops'?"))
