# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestTypeAliases_test_str_aliases_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser.add_option('-s', type='str')
    self.assertEqual(self.parser.get_option('-s').type, 'string')
