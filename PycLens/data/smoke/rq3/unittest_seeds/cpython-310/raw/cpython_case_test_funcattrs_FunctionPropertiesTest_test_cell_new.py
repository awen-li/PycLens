# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionPropertiesTest_test_cell_new

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cell_obj = types.CellType(1)
    self.assertEqual(cell_obj.cell_contents, 1)
    cell_obj = types.CellType()
    msg = "shouldn't be able to read an empty cell"
    with self.assertRaises(ValueError, msg=msg):
        cell_obj.cell_contents
