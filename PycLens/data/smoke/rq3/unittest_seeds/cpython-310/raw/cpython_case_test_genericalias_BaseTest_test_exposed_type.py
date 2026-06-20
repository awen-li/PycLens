# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_exposed_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import types
    a = types.GenericAlias(list, int)
    self.assertEqual(str(a), 'list[int]')
    self.assertIs(a.__origin__, list)
    self.assertEqual(a.__args__, (int,))
    self.assertEqual(a.__parameters__, ())
