# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_numeric_tower.py
# case: HashTest_test_hash_normalization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class HalibutProxy:

        def __hash__(self):
            return hash('halibut')

        def __eq__(self, other):
            return other == 'halibut'
    x = {'halibut', HalibutProxy()}
    self.assertEqual(len(x), 1)
