# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_trashcan_threads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NESTING = 60
    N_THREADS = 2

    def sleeper_gen():
        """A generator that releases the GIL when closed or dealloc'ed."""
        try:
            yield
        finally:
            time.sleep(1e-06)

    class C(list):
        inits = []
        dels = []

        def __init__(self, alist):
            self[:] = alist
            C.inits.append(None)

        def __del__(self):
            C.dels.append(None)
            g = sleeper_gen()
            next(g)

    def make_nested():
        """Create a sufficiently nested container object so that the
            trashcan mechanism is invoked when deallocating it."""
        x = C([])
        for i in range(NESTING):
            x = [C([x])]
        del x

    def run_thread():
        """Exercise make_nested() in a loop."""
        while not exit:
            make_nested()
    old_switchinterval = sys.getswitchinterval()
    sys.setswitchinterval(1e-05)
    try:
        exit = []
        threads = []
        for i in range(N_THREADS):
            t = threading.Thread(target=run_thread)
            threads.append(t)
        with threading_helper.start_threads(threads, lambda : exit.append(1)):
            time.sleep(1.0)
    finally:
        sys.setswitchinterval(old_switchinterval)
    gc.collect()
    self.assertEqual(len(C.inits), len(C.dels))
