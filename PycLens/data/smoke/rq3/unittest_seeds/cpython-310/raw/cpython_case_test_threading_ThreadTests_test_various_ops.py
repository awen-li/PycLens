# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_various_ops

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NUMTASKS = 10
    sema = threading.BoundedSemaphore(value=3)
    mutex = threading.RLock()
    numrunning = Counter()
    threads = []
    for i in range(NUMTASKS):
        t = TestThread('<thread %d>' % i, self, sema, mutex, numrunning)
        threads.append(t)
        self.assertIsNone(t.ident)
        self.assertRegex(repr(t), '^<TestThread\\(.*, initial\\)>$')
        t.start()
    if hasattr(threading, 'get_native_id'):
        native_ids = set((t.native_id for t in threads)) | {threading.get_native_id()}
        self.assertNotIn(None, native_ids)
        self.assertEqual(len(native_ids), NUMTASKS + 1)
    if verbose:
        print('waiting for all tasks to complete')
    for t in threads:
        t.join()
        self.assertFalse(t.is_alive())
        self.assertNotEqual(t.ident, 0)
        self.assertIsNotNone(t.ident)
        self.assertRegex(repr(t), '^<TestThread\\(.*, stopped -?\\d+\\)>$')
    if verbose:
        print('all tasks done')
    self.assertEqual(numrunning.get(), 0)
