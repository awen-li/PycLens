# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestCachedProperty_test_threaded

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    go = threading.Event()
    item = CachedCostItemWait(go)
    num_threads = 3
    orig_si = sys.getswitchinterval()
    sys.setswitchinterval(1e-06)
    try:
        threads = [threading.Thread(target=lambda : item.cost) for k in range(num_threads)]
        with threading_helper.start_threads(threads):
            go.set()
    finally:
        sys.setswitchinterval(orig_si)
    self.assertEqual(item.cost, 2)
