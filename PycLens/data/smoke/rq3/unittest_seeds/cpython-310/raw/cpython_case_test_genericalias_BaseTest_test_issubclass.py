# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_issubclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class L(list):
        ...
    self.assertTrue(issubclass(L, list))
    with self.assertRaises(TypeError):
        issubclass(L, list[str])
