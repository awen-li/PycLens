# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_resurrection_is_transitive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Cargo:

        def __init__(self):
            self.me = self

    class Lazarus:
        resurrected_instances = []

        def __del__(self):
            Lazarus.resurrected_instances.append(self)
    gc.collect()
    gc.disable()
    laz = Lazarus()
    cargo = Cargo()
    cargo_id = id(cargo)
    laz.cargo = cargo
    cargo.laz = laz
    del laz, cargo
    gc.collect()
    self.assertEqual(len(Lazarus.resurrected_instances), 1)
    instance = Lazarus.resurrected_instances.pop()
    self.assertTrue(hasattr(instance, 'cargo'))
    self.assertEqual(id(instance.cargo), cargo_id)
    gc.collect()
    gc.enable()
