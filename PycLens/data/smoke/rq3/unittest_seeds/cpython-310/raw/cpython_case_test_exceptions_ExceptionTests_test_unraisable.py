# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_unraisable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BrokenDel:

        def __del__(self):
            exc = ValueError('del is broken')
            raise exc
    obj = BrokenDel()
    with support.catch_unraisable_exception() as cm:
        del obj
        gc_collect()
        self.assertEqual(cm.unraisable.object, BrokenDel.__del__)
        self.assertIsNotNone(cm.unraisable.exc_traceback)
