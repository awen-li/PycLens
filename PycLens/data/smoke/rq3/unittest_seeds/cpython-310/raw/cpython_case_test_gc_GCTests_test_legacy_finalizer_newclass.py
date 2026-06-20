# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_legacy_finalizer_newclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @with_tp_del
    class A(object):

        def __tp_del__(self):
            pass

    class B(object):
        pass
    a = A()
    a.a = a
    id_a = id(a)
    b = B()
    b.b = b
    gc.collect()
    del a
    del b
    self.assertNotEqual(gc.collect(), 0)
    for obj in gc.garbage:
        if id(obj) == id_a:
            del obj.a
            break
    else:
        self.fail("didn't find obj in garbage (finalizer)")
    gc.garbage.remove(obj)
