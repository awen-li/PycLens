# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestChainMap_test_ordering

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    baseline = {'music': 'bach', 'art': 'rembrandt'}
    adjustments = {'art': 'van gogh', 'opera': 'carmen'}
    cm = ChainMap(adjustments, baseline)
    combined = baseline.copy()
    combined.update(adjustments)
    self.assertEqual(list(combined.items()), list(cm.items()))
