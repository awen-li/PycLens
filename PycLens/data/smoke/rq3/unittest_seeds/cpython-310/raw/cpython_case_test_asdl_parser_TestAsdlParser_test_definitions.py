# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asdl_parser.py
# case: TestAsdlParser_test_definitions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    defs = self.mod.dfns
    self.assertIsInstance(defs[0], self.asdl.Type)
    self.assertIsInstance(defs[0].value, self.asdl.Sum)
    self.assertIsInstance(self.types['withitem'], self.asdl.Product)
    self.assertIsInstance(self.types['alias'], self.asdl.Product)
