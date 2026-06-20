# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestOptionGroup_test_option_group_create_instance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    group = OptionGroup(self.parser, 'Spam')
    self.parser.add_option_group(group)
    group.add_option('--spam', action='store_true', help='spam spam spam spam')
    self.assertParseOK(['--spam'], {'spam': 1}, [])
