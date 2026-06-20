# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestStandard_test_ambiguous_option

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser.add_option('--foz', action='store', type='string', dest='foo')
    self.assertParseFail(['--f=bar'], 'ambiguous option: --f (--foo, --foz?)')
