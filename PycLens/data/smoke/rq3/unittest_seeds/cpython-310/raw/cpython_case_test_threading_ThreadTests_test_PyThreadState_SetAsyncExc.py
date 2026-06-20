# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_PyThreadState_SetAsyncExc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctypes = import_module('ctypes')
    set_async_exc = ctypes.pythonapi.PyThreadState_SetAsyncExc
    set_async_exc.argtypes = (ctypes.c_ulong, ctypes.py_object)

    class AsyncExc(Exception):
        pass
    exception = ctypes.py_object(AsyncExc)
    tid = threading.get_ident()
    self.assertIsInstance(tid, int)
    self.assertGreater(tid, 0)
    try:
        result = set_async_exc(tid, exception)
        while True:
            pass
    except AsyncExc:
        pass
    else:
        self.fail('AsyncExc not raised')
    try:
        self.assertEqual(result, 1)
    except UnboundLocalError:
        pass
    worker_started = threading.Event()
    worker_saw_exception = threading.Event()

    class Worker(threading.Thread):

        def run(self):
            self.id = threading.get_ident()
            self.finished = False
            try:
                while True:
                    worker_started.set()
                    time.sleep(0.1)
            except AsyncExc:
                self.finished = True
                worker_saw_exception.set()
    t = Worker()
    t.daemon = True
    t.start()
    if verbose:
        print('    started worker thread')
    if verbose:
        print('    trying nonsensical thread id')
    result = set_async_exc(-1, exception)
    self.assertEqual(result, 0)
    if verbose:
        print('    waiting for worker thread to get started')
    ret = worker_started.wait()
    self.assertTrue(ret)
    if verbose:
        print("    verifying worker hasn't exited")
    self.assertFalse(t.finished)
    if verbose:
        print('    attempting to raise asynch exception in worker')
    result = set_async_exc(t.id, exception)
    self.assertEqual(result, 1)
    if verbose:
        print('    waiting for worker to say it caught the exception')
    worker_saw_exception.wait(timeout=support.SHORT_TIMEOUT)
    self.assertTrue(t.finished)
    if verbose:
        print('    all OK -- joining worker')
    if t.finished:
        t.join()
