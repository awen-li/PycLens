# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code.py
# case: CoExtra_test_free_different_thread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.get_func()

    class ThreadTest(threading.Thread):

        def __init__(self, f, test):
            super().__init__()
            self.f = f
            self.test = test

        def run(self):
            del self.f
            self.test.assertEqual(LAST_FREED, 500)
    SetExtra(f.__code__, FREE_INDEX, ctypes.c_voidp(500))
    tt = ThreadTest(f, self)
    del f
    tt.start()
    tt.join()
    self.assertEqual(LAST_FREED, 500)
