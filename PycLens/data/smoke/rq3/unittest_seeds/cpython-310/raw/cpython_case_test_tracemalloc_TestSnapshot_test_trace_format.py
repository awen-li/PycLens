# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestSnapshot_test_trace_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (snapshot, snapshot2) = create_snapshots()
    trace = snapshot.traces[0]
    self.assertEqual(str(trace), 'b.py:4: 10 B')
    traceback = trace.traceback
    self.assertEqual(str(traceback), 'b.py:4')
    frame = traceback[0]
    self.assertEqual(str(frame), 'b.py:4')
