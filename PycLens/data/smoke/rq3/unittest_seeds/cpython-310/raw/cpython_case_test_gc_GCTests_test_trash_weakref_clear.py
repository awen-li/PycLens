# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_trash_weakref_clear

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    callback = unittest.mock.Mock()

    class A:
        __slots__ = ['a', 'y', 'wz']

    class Z:
        pass
    a = A()
    a.a = a
    a.y = ContainerNoGC(Z())
    a.wz = weakref.ref(a.y.value, callback)
    wr_cycle = [a.wz]
    wr_cycle.append(wr_cycle)
    gc.collect()
    gc.disable()
    del a, wr_cycle
    gc.collect()
    callback.assert_not_called()
    gc.enable()
