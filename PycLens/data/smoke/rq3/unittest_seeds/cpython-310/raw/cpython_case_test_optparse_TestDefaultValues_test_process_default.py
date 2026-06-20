# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestDefaultValues_test_process_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser.option_class = DurationOption
    self.parser.add_option('-d', type='duration', default=300)
    self.parser.add_option('-e', type='duration', default='6m')
    self.parser.set_defaults(n='42')
    self.expected.update({'d': 300, 'e': 360, 'n': 42})
    self.assertEqual(self.parser.get_default_values(), self.expected)
    self.parser.set_process_default_values(False)
    self.expected.update({'d': 300, 'e': '6m', 'n': '42'})
    self.assertEqual(self.parser.get_default_values(), self.expected)
