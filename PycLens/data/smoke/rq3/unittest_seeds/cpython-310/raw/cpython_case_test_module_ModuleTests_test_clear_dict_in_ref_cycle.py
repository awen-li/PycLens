# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_clear_dict_in_ref_cycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    destroyed = []
    m = ModuleType('foo')
    m.destroyed = destroyed
    s = 'class A:\n    def __init__(self, l):\n        self.l = l\n    def __del__(self):\n        self.l.append(1)\na = A(destroyed)'
    exec(s, m.__dict__)
    del m
    gc_collect()
    self.assertEqual(destroyed, [1])
