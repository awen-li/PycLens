# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: ContextManagerTestCase_test_nokeepref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        pass

    @contextmanager
    def woohoo(a, b):
        a = weakref.ref(a)
        b = weakref.ref(b)
        support.gc_collect()
        self.assertIsNone(a())
        self.assertIsNone(b())
        yield
    with woohoo(A(), b=A()):
        pass
