# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestContext_test_3611

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import gc

    class C:

        def __del__(self):
            try:
                1 / 0
            except:
                raise

    def f():
        x = C()
        try:
            try:
                f.x
            except AttributeError:
                del x
                gc.collect()
                raise TypeError
        except Exception as e:
            self.assertNotEqual(e.__context__, None)
            self.assertIsInstance(e.__context__, AttributeError)
    with support.catch_unraisable_exception() as cm:
        f()
        self.assertEqual(ZeroDivisionError, cm.unraisable.exc_type)
