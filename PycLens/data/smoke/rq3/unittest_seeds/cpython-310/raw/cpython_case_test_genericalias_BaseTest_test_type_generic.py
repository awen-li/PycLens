# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_type_generic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = type[int]
    Test = t('Test', (), {})
    self.assertTrue(isinstance(Test, type))
    test = Test()
    self.assertEqual(t(test), Test)
    self.assertEqual(t(0), int)
