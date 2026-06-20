# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestChainMap_test_dict_coercion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = ChainMap(dict(a=1, b=2), dict(b=20, c=30))
    self.assertEqual(dict(d), dict(a=1, b=2, c=30))
    self.assertEqual(dict(d.items()), dict(a=1, b=2, c=30))
