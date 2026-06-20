# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_threads_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cvar = contextvars.ContextVar('cvar')

    def sub(num):
        for i in range(10):
            cvar.set(num + i)
            time.sleep(random.uniform(0.001, 0.05))
            self.assertEqual(cvar.get(), num + i)
        return num
    tp = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    try:
        results = list(tp.map(sub, range(10)))
    finally:
        tp.shutdown()
    self.assertEqual(results, list(range(10)))
