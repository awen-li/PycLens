# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_mixing_slot_wrappers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X(dict):
        __setattr__ = dict.__setitem__
        __neg__ = dict.copy
    x = X()
    x.y = 42
    self.assertEqual(x['y'], 42)
    self.assertEqual(x, -x)
