# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDialectRegistry_test_registry_badargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, csv.list_dialects, None)
    self.assertRaises(TypeError, csv.get_dialect)
    self.assertRaises(csv.Error, csv.get_dialect, None)
    self.assertRaises(csv.Error, csv.get_dialect, 'nonesuch')
    self.assertRaises(TypeError, csv.unregister_dialect)
    self.assertRaises(csv.Error, csv.unregister_dialect, None)
    self.assertRaises(csv.Error, csv.unregister_dialect, 'nonesuch')
    self.assertRaises(TypeError, csv.register_dialect, None)
    self.assertRaises(TypeError, csv.register_dialect, None, None)
    self.assertRaises(TypeError, csv.register_dialect, 'nonesuch', 0, 0)
    self.assertRaises(TypeError, csv.register_dialect, 'nonesuch', badargument=None)
    self.assertRaises(TypeError, csv.register_dialect, 'nonesuch', quoting=None)
    self.assertRaises(TypeError, csv.register_dialect, [])
