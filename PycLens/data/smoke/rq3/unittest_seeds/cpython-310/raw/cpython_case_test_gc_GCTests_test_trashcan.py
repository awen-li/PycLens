# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_trashcan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Ouch:
        n = 0

        def __del__(self):
            Ouch.n = Ouch.n + 1
            if Ouch.n % 17 == 0:
                gc.collect()
    gc.enable()
    N = 150
    for count in range(2):
        t = []
        for i in range(N):
            t = [t, Ouch()]
        u = []
        for i in range(N):
            u = [u, Ouch()]
        v = {}
        for i in range(N):
            v = {1: v, 2: Ouch()}
    gc.disable()
