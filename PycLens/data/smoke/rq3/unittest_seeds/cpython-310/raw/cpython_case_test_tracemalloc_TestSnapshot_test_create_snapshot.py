# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestSnapshot_test_create_snapshot

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw_traces = [(0, 5, (('a.py', 2),), 10)]
    with contextlib.ExitStack() as stack:
        stack.enter_context(patch.object(tracemalloc, 'is_tracing', return_value=True))
        stack.enter_context(patch.object(tracemalloc, 'get_traceback_limit', return_value=5))
        stack.enter_context(patch.object(tracemalloc, '_get_traces', return_value=raw_traces))
        snapshot = tracemalloc.take_snapshot()
        self.assertEqual(snapshot.traceback_limit, 5)
        self.assertEqual(len(snapshot.traces), 1)
        trace = snapshot.traces[0]
        self.assertEqual(trace.size, 5)
        self.assertEqual(trace.traceback.total_nframe, 10)
        self.assertEqual(len(trace.traceback), 1)
        self.assertEqual(trace.traceback[0].filename, 'a.py')
        self.assertEqual(trace.traceback[0].lineno, 2)
