# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCCallbackTests_test_collect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.preclean()
    gc.collect()
    n = [v[0] for v in self.visit]
    n1 = [i for i in n if i == 1]
    n2 = [i for i in n if i == 2]
    self.assertEqual(n1, [1] * 2)
    self.assertEqual(n2, [2] * 2)
    n = [v[1] for v in self.visit]
    n1 = [i for i in n if i == 'start']
    n2 = [i for i in n if i == 'stop']
    self.assertEqual(n1, ['start'] * 2)
    self.assertEqual(n2, ['stop'] * 2)
    for v in self.visit:
        info = v[2]
        self.assertTrue('generation' in info)
        self.assertTrue('collected' in info)
        self.assertTrue('uncollectable' in info)
