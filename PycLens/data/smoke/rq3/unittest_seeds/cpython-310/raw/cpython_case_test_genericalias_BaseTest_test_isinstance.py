# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_isinstance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(isinstance([], list))
    with self.assertRaises(TypeError):
        isinstance([], list[str])
