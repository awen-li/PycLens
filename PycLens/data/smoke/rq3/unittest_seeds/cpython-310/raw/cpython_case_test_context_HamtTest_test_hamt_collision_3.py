# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: HamtTest_test_hamt_collision_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    C = HashKey(2147483648, 'C')
    D = HashKey(2147483648, 'D')
    E = HashKey(0, 'E')
    h = hamt()
    h = h.set(C, 'C')
    h = h.set(D, 'D')
    h = h.set(E, 'E')
    self.assertEqual({k.name for k in h.keys()}, {'C', 'D', 'E'})
