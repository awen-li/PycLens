# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_BoundedSemaphore_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for limit in range(1, 10):
        bs = threading.BoundedSemaphore(limit)
        threads = [threading.Thread(target=bs.acquire) for _ in range(limit)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        threads = [threading.Thread(target=bs.release) for _ in range(limit)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertRaises(ValueError, bs.release)
