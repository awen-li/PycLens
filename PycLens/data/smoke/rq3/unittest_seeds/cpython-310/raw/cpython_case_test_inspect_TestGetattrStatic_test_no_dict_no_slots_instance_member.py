# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_no_dict_no_slots_instance_member

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(__file__, encoding='utf-8') as handle:
        self.assertEqual(inspect.getattr_static(handle, 'name'), type(handle).name)
