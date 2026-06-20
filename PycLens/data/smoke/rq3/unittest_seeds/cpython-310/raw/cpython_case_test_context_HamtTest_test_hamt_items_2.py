# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: HamtTest_test_hamt_items_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    A = HashKey(100, 'A')
    B = HashKey(101, 'B')
    C = HashKey(100100, 'C')
    D = HashKey(100100, 'D')
    E = HashKey(100100, 'E')
    F = HashKey(110, 'F')
    h = hamt()
    h = h.set(A, 'a')
    h = h.set(B, 'b')
    h = h.set(C, 'c')
    h = h.set(D, 'd')
    h = h.set(E, 'e')
    h = h.set(F, 'f')
    it = h.items()
    self.assertEqual(set(list(it)), {(A, 'a'), (B, 'b'), (C, 'c'), (D, 'd'), (E, 'e'), (F, 'f')})
