# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_copy_maintains_tracking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        pass
    key = A()
    for d in ({}, {'a': 1}, {key: 'val'}):
        d2 = d.copy()
        self.assertEqual(gc.is_tracked(d), gc.is_tracked(d2))
