# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_get_stats

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stats = gc.get_stats()
    self.assertEqual(len(stats), 3)
    for st in stats:
        self.assertIsInstance(st, dict)
        self.assertEqual(set(st), {'collected', 'collections', 'uncollectable'})
        self.assertGreaterEqual(st['collected'], 0)
        self.assertGreaterEqual(st['collections'], 0)
        self.assertGreaterEqual(st['uncollectable'], 0)
    if gc.isenabled():
        self.addCleanup(gc.enable)
        gc.disable()
    old = gc.get_stats()
    gc.collect(0)
    new = gc.get_stats()
    self.assertEqual(new[0]['collections'], old[0]['collections'] + 1)
    self.assertEqual(new[1]['collections'], old[1]['collections'])
    self.assertEqual(new[2]['collections'], old[2]['collections'])
    gc.collect(2)
    new = gc.get_stats()
    self.assertEqual(new[0]['collections'], old[0]['collections'] + 1)
    self.assertEqual(new[1]['collections'], old[1]['collections'])
    self.assertEqual(new[2]['collections'], old[2]['collections'] + 1)
