# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_bug21435

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gc.collect()

    class A:
        pass

    class B:

        def __init__(self, x):
            self.x = x

        def __del__(self):
            self.attr = None

    def do_work():
        a = A()
        b = B(A())
        a.attr = b
        b.attr = a
    do_work()
    gc.collect()
