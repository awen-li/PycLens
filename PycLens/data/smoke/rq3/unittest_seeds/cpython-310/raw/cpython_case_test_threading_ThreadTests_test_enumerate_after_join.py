# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_enumerate_after_join

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    enum = threading.enumerate
    old_interval = sys.getswitchinterval()
    try:
        for i in range(1, 100):
            sys.setswitchinterval(i * 0.0002)
            t = threading.Thread(target=lambda : None)
            t.start()
            t.join()
            l = enum()
            self.assertNotIn(t, l, '#1703448 triggered after %d trials: %s' % (i, l))
    finally:
        sys.setswitchinterval(old_interval)
