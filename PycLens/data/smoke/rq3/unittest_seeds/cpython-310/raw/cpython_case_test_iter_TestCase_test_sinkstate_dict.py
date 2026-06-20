# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_sinkstate_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = {1: 1, 2: 2, 0: 0, 4: 4, 3: 3}
    for b in (iter(a), a.keys(), a.items(), a.values()):
        b = iter(a)
        self.assertEqual(len(list(b)), 5)
        self.assertEqual(list(b), [])
