# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestDefaultValues_test_mixed_defaults_post

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser.set_defaults(n=42, m=-100)
    self.expected.update({'n': 42, 'm': -100})
    self.assertEqual(self.parser.get_default_values(), self.expected)
