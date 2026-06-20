# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCCallbackTests_test_collect_garbage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.preclean()
    Uncollectable()
    Uncollectable()
    C1055820(666)
    gc.collect()
    for v in self.visit:
        if v[1] != 'stop':
            continue
        info = v[2]
        self.assertEqual(info['collected'], 2)
        self.assertEqual(info['uncollectable'], 8)
    self.assertEqual(len(gc.garbage), 4)
    for e in gc.garbage:
        self.assertIsInstance(e, Uncollectable)
    self.cleanup = True
    self.visit = []
    gc.garbage[:] = []
    gc.collect()
    for v in self.visit:
        if v[1] != 'stop':
            continue
        info = v[2]
        self.assertEqual(info['collected'], 0)
        self.assertEqual(info['uncollectable'], 4)
    self.assertEqual(len(gc.garbage), 0)
