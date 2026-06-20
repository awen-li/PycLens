# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_slots

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nd = self.module.NormalDist(300, 23)
    with self.assertRaises(TypeError):
        vars(nd)
    self.assertEqual(tuple(nd.__slots__), ('_mu', '_sigma'))
