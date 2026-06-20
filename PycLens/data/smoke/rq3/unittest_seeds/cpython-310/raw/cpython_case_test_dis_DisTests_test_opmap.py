# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: DisTests_test_opmap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(dis.opmap['NOP'], 9)
    self.assertIn(dis.opmap['LOAD_CONST'], dis.hasconst)
    self.assertIn(dis.opmap['STORE_NAME'], dis.hasname)
