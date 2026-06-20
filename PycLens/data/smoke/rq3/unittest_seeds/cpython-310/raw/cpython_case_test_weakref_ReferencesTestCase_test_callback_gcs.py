# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_callback_gcs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ObjectWithDel(Object):

        def __del__(self):
            pass
    x = ObjectWithDel(1)
    ref1 = weakref.ref(x, lambda ref: support.gc_collect())
    del x
    support.gc_collect()
