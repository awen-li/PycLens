# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestMultipleArgs_test_nargs_with_positional_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseOK(['foo', '-p', '1', '2.5', '-4.3', 'xyz'], {'point': (1.0, 2.5, -4.3)}, ['foo', 'xyz'])
