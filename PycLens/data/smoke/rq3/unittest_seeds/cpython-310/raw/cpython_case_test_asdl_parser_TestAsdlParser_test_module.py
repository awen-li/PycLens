# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asdl_parser.py
# case: TestAsdlParser_test_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.mod.name, 'Python')
    self.assertIn('stmt', self.types)
    self.assertIn('expr', self.types)
    self.assertIn('mod', self.types)
