# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestTracemallocEnabled_test_snapshot

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (obj, source) = allocate_bytes(123)
    snapshot = tracemalloc.take_snapshot()
    self.assertGreater(snapshot.traces[1].traceback.total_nframe, 10)
    snapshot.dump(os_helper.TESTFN)
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    snapshot2 = tracemalloc.Snapshot.load(os_helper.TESTFN)
    self.assertEqual(snapshot2.traces, snapshot.traces)
    tracemalloc.stop()
    with self.assertRaises(RuntimeError) as cm:
        tracemalloc.take_snapshot()
    self.assertEqual(str(cm.exception), 'the tracemalloc module must be tracing memory allocations to take a snapshot')
