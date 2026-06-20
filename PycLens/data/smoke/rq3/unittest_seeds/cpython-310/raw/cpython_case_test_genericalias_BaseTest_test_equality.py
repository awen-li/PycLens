# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list[int], list[int])
    self.assertEqual(dict[str, int], dict[str, int])
    self.assertNotEqual(dict[str, int], dict[str, str])
    self.assertNotEqual(list, list[int])
    self.assertNotEqual(list[int], list)
