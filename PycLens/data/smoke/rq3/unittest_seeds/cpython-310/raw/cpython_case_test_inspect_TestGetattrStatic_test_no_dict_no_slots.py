# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_no_dict_no_slots

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(inspect.getattr_static(1, 'foo', None), None)
    self.assertNotEqual(inspect.getattr_static('foo', 'lower'), None)
