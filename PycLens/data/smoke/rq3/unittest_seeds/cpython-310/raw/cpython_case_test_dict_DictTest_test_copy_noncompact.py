# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_copy_noncompact

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {k: k for k in range(1000)}
    for k in range(950):
        del d[k]
    d2 = d.copy()
    self.assertEqual(d2, d)
