# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestSnapshot_test_filter_traces_domain_filter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (snapshot, snapshot2) = create_snapshots()
    filter1 = tracemalloc.DomainFilter(False, domain=3)
    filter2 = tracemalloc.DomainFilter(True, domain=3)
    snapshot3 = snapshot.filter_traces((filter1,))
    self.assertEqual(snapshot3.traces._traces, [(0, 10, (('a.py', 2), ('b.py', 4)), 3), (0, 10, (('a.py', 2), ('b.py', 4)), 3), (0, 10, (('a.py', 2), ('b.py', 4)), 3), (1, 2, (('a.py', 5), ('b.py', 4)), 3), (2, 66, (('b.py', 1),), 1)])
    snapshot3 = snapshot.filter_traces((filter2,))
    self.assertEqual(snapshot3.traces._traces, [(3, 7, (('<unknown>', 0),), 1)])
