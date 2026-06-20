# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CIOTest_test_IOBase_finalize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyIO(self.IOBase):

        def close(self):
            pass
    MyIO()
    obj = MyIO()
    obj.obj = obj
    wr = weakref.ref(obj)
    del MyIO
    del obj
    support.gc_collect()
    self.assertIsNone(wr(), wr)
