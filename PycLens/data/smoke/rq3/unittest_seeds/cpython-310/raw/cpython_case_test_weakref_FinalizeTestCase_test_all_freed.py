# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: FinalizeTestCase_test_all_freed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyFinalizer(weakref.finalize):
        pass
    a = self.A()
    res = []

    def callback():
        res.append(123)
    f = MyFinalizer(a, callback)
    wr_callback = weakref.ref(callback)
    wr_f = weakref.ref(f)
    del callback, f
    self.assertIsNotNone(wr_callback())
    self.assertIsNotNone(wr_f())
    del a
    self._collect_if_necessary()
    self.assertIsNone(wr_callback())
    self.assertIsNone(wr_f())
    self.assertEqual(res, [123])
