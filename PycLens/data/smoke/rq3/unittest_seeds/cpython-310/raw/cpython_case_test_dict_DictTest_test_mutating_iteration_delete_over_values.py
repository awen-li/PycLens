# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_mutating_iteration_delete_over_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {}
    d[0] = 0
    with self.assertRaises(RuntimeError):
        for i in d.values():
            del d[0]
            d[0] = 0
