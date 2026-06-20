# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestDefaultValues_test_mixed_defaults_pre

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser.set_defaults(x='barf', y='blah')
    self.parser.add_option('-x', default='frob')
    self.parser.add_option('-y')
    self.expected.update({'x': 'frob', 'y': 'blah'})
    self.assertEqual(self.parser.get_default_values(), self.expected)
    self.parser.remove_option('-y')
    self.parser.add_option('-y', default=None)
    self.expected.update({'y': None})
    self.assertEqual(self.parser.get_default_values(), self.expected)
