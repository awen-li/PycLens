# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading_local.py
# case: BaseLocalTest_test_derived

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import time

    class Local(self._local):

        def __init__(self):
            time.sleep(0.01)
    local = Local()

    def f(i):
        local.x = i
        self.assertEqual(local.x, i)
    with threading_helper.start_threads((threading.Thread(target=f, args=(i,)) for i in range(10))):
        pass
