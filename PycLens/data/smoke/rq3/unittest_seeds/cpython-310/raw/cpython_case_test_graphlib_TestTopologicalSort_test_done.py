# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_graphlib.py
# case: TestTopologicalSort_test_done

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ts = graphlib.TopologicalSorter()
    ts.add(1, 2, 3, 4)
    ts.add(2, 3)
    ts.prepare()
    self.assertEqual(ts.get_ready(), (3, 4))
    self.assertEqual(ts.get_ready(), ())
    ts.done(3)
    self.assertEqual(ts.get_ready(), (2,))
    self.assertEqual(ts.get_ready(), ())
    ts.done(4)
    ts.done(2)
    self.assertEqual(ts.get_ready(), (1,))
    self.assertEqual(ts.get_ready(), ())
    ts.done(1)
    self.assertEqual(ts.get_ready(), ())
    self.assertFalse(ts.is_active())
