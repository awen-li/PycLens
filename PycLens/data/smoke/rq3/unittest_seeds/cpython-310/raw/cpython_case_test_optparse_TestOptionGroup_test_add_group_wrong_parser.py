# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestOptionGroup_test_add_group_wrong_parser

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    group = OptionGroup(self.parser, 'Spam')
    group.parser = OptionParser()
    self.assertRaises(self.parser.add_option_group, (group,), None, ValueError, 'invalid OptionGroup (wrong parser)')
