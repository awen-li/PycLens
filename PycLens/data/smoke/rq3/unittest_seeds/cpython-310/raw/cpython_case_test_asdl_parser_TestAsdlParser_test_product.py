# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asdl_parser.py
# case: TestAsdlParser_test_product

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    alias = self.types['alias']
    self.assertEqual(str(alias), 'Product([Field(identifier, name), Field(identifier, asname, opt=True)], [Field(int, lineno), Field(int, col_offset), Field(int, end_lineno, opt=True), Field(int, end_col_offset, opt=True)])')
