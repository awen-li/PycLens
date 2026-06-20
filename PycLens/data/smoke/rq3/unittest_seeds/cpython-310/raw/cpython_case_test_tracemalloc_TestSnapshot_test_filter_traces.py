# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestSnapshot_test_filter_traces

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (snapshot, snapshot2) = create_snapshots()
    filter1 = tracemalloc.Filter(False, 'b.py')
    filter2 = tracemalloc.Filter(True, 'a.py', 2)
    filter3 = tracemalloc.Filter(True, 'a.py', 5)
    original_traces = list(snapshot.traces._traces)
    snapshot3 = snapshot.filter_traces((filter1,))
    self.assertEqual(snapshot3.traces._traces, [(0, 10, (('a.py', 2), ('b.py', 4)), 3), (0, 10, (('a.py', 2), ('b.py', 4)), 3), (0, 10, (('a.py', 2), ('b.py', 4)), 3), (1, 2, (('a.py', 5), ('b.py', 4)), 3), (3, 7, (('<unknown>', 0),), 1)])
    self.assertEqual(snapshot.traces._traces, original_traces)
    snapshot4 = snapshot3.filter_traces((filter2, filter3))
    self.assertEqual(snapshot4.traces._traces, [(0, 10, (('a.py', 2), ('b.py', 4)), 3), (0, 10, (('a.py', 2), ('b.py', 4)), 3), (0, 10, (('a.py', 2), ('b.py', 4)), 3), (1, 2, (('a.py', 5), ('b.py', 4)), 3)])
    snapshot5 = snapshot.filter_traces(())
    self.assertIsNot(snapshot5, snapshot)
    self.assertIsNot(snapshot5.traces, snapshot.traces)
    self.assertEqual(snapshot5.traces, snapshot.traces)
    self.assertRaises(TypeError, snapshot.filter_traces, filter1)
