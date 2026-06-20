# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threadedtempfile.py
# case: ThreadedTempFileTest_test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    threads = [TempFileGreedy() for i in range(NUM_THREADS)]
    with threading_helper.start_threads(threads, startEvent.set):
        pass
    ok = sum((t.ok_count for t in threads))
    errors = [str(t.name) + str(t.errors.getvalue()) for t in threads if t.error_count]
    msg = 'Errors: errors %d ok %d\n%s' % (len(errors), ok, '\n'.join(errors))
    self.assertEqual(errors, [], msg)
    self.assertEqual(ok, NUM_THREADS * FILES_PER_THREAD)
