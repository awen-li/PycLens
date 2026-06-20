# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_graphlib.py
# case: TestTopologicalSort_test_is_active

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ts = graphlib.TopologicalSorter()
    ts.add(1, 2)
    ts.prepare()
    self.assertTrue(ts.is_active())
    self.assertEqual(ts.get_ready(), (2,))
    self.assertTrue(ts.is_active())
    ts.done(2)
    self.assertTrue(ts.is_active())
    self.assertEqual(ts.get_ready(), (1,))
    self.assertTrue(ts.is_active())
    ts.done(1)
    self.assertFalse(ts.is_active())
