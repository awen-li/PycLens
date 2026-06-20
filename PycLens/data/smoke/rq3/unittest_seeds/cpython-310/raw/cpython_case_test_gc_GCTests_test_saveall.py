# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_saveall

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gc.collect()
    self.assertEqual(gc.garbage, [])
    L = []
    L.append(L)
    id_L = id(L)
    debug = gc.get_debug()
    gc.set_debug(debug | gc.DEBUG_SAVEALL)
    del L
    gc.collect()
    gc.set_debug(debug)
    self.assertEqual(len(gc.garbage), 1)
    obj = gc.garbage.pop()
    self.assertEqual(id(obj), id_L)
