# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading_local.py
# case: BaseLocalTest_test_derived_cycle_dealloc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Local(self._local):
        pass
    locals = None
    passed = False
    e1 = threading.Event()
    e2 = threading.Event()

    def f():
        nonlocal passed
        cycle = [Local()]
        cycle.append(cycle)
        cycle[0].foo = 'bar'
        del cycle
        support.gc_collect()
        e1.set()
        e2.wait()
        passed = all((not hasattr(local, 'foo') for local in locals))
    t = threading.Thread(target=f)
    t.start()
    e1.wait()
    locals = [Local() for i in range(10)]
    e2.set()
    t.join()
    self.assertTrue(passed)
