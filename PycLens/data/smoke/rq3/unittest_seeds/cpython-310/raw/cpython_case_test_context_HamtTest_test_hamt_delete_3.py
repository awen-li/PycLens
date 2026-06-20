# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: HamtTest_test_hamt_delete_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    A = HashKey(100, 'A')
    B = HashKey(101, 'B')
    C = HashKey(100100, 'C')
    D = HashKey(100100, 'D')
    E = HashKey(104, 'E')
    h = hamt()
    h = h.set(A, 'a')
    h = h.set(B, 'b')
    h = h.set(C, 'c')
    h = h.set(D, 'd')
    h = h.set(E, 'e')
    orig_len = len(h)
    h = h.delete(A)
    self.assertEqual(len(h), orig_len - 1)
    h = h.delete(E)
    self.assertEqual(len(h), orig_len - 2)
    self.assertEqual(h.get(C), 'c')
    self.assertEqual(h.get(B), 'b')
