# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asdl_parser.py
# case: TestAsdlParser_test_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stmt = self.types['stmt']
    self.assertEqual(len(stmt.attributes), 4)
    self.assertEqual(repr(stmt.attributes[0]), 'Field(int, lineno)')
    self.assertEqual(repr(stmt.attributes[1]), 'Field(int, col_offset)')
    self.assertEqual(repr(stmt.attributes[2]), 'Field(int, end_lineno, opt=True)')
    self.assertEqual(repr(stmt.attributes[3]), 'Field(int, end_col_offset, opt=True)')
