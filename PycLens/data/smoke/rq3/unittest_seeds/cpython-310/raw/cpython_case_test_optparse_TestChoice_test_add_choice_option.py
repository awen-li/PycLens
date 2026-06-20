# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestChoice_test_add_choice_option

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser.add_option('-d', '--default', choices=['four', 'five', 'six'])
    opt = self.parser.get_option('-d')
    self.assertEqual(opt.type, 'choice')
    self.assertEqual(opt.action, 'store')
