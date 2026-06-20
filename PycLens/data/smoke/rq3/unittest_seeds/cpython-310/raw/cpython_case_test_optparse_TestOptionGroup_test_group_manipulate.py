# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestOptionGroup_test_group_manipulate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    group = self.parser.add_option_group('Group 2', description='Some more options')
    group.set_title('Bacon')
    group.add_option('--bacon', type='int')
    self.assertTrue(self.parser.get_option_group('--bacon'), group)
