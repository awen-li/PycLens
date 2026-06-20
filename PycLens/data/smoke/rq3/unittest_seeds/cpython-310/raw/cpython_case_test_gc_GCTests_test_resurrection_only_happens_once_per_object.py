# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_resurrection_only_happens_once_per_object

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def __init__(self):
            self.me = self

    class Lazarus(A):
        resurrected = 0
        resurrected_instances = []

        def __del__(self):
            Lazarus.resurrected += 1
            Lazarus.resurrected_instances.append(self)
    gc.collect()
    gc.disable()
    laz = Lazarus()
    self.assertEqual(Lazarus.resurrected, 0)
    del laz
    gc.collect()
    self.assertEqual(Lazarus.resurrected, 1)
    self.assertEqual(len(Lazarus.resurrected_instances), 1)
    Lazarus.resurrected_instances.clear()
    self.assertEqual(Lazarus.resurrected, 1)
    gc.collect()
    self.assertEqual(Lazarus.resurrected, 1)
    gc.enable()
