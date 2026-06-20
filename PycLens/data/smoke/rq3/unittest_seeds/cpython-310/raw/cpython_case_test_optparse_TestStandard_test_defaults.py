# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestStandard_test_defaults

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (options, args) = self.parser.parse_args([])
    defaults = self.parser.get_default_values()
    self.assertEqual(vars(defaults), vars(options))
