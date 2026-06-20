# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test__struct_reference_cycle_cleaned_up

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _struct_module = import_helper.import_fresh_module('_struct')
    module_ref = weakref.ref(_struct_module)
    _struct_module.calcsize('b')
    del _struct_module
    gc.collect()
    self.assertIsNone(module_ref(), '_struct module was not garbage collected')
