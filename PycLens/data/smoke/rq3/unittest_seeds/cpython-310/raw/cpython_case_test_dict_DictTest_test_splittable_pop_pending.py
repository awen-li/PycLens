# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_splittable_pop_pending

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (a, b) = self.make_shared_key_dict(2)
    a['a'] = 4
    with self.assertRaises(KeyError):
        b.pop('a')
