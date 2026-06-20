# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestSnapshot_test_slices

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (snapshot, snapshot2) = create_snapshots()
    self.assertEqual(snapshot.traces[:2], (snapshot.traces[0], snapshot.traces[1]))
    traceback = snapshot.traces[0].traceback
    self.assertEqual(traceback[:2], (traceback[0], traceback[1]))
