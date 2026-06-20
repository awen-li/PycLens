# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestTracemallocEnabled_test_snapshot_save_attr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    snapshot = tracemalloc.take_snapshot()
    snapshot.test_attr = 'new'
    snapshot.dump(os_helper.TESTFN)
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    snapshot2 = tracemalloc.Snapshot.load(os_helper.TESTFN)
    self.assertEqual(snapshot2.test_attr, 'new')
