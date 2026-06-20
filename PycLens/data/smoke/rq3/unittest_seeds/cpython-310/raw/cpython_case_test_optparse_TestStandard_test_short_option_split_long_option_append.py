# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestStandard_test_short_option_split_long_option_append

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseOK(['--foo=bar', '-b', '123', '--foo', 'baz'], {'a': None, 'boo': 123, 'foo': ['bar', 'baz']}, [])
