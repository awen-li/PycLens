# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: CreateTests_test_in_thread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lock = threading.Lock()
    interp = None

    def f():
        nonlocal interp
        interp = interpreters.create()
        lock.acquire()
        lock.release()
    t = threading.Thread(target=f)
    with lock:
        t.start()
    t.join()
    self.assertIn(interp, interpreters.list_all())
