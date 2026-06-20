# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: HamtTest_test_hamt_delete_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    A = HashKey(100, 'A')
    B = HashKey(101, 'B')
    C = HashKey(102, 'C')
    D = HashKey(103, 'D')
    E = HashKey(104, 'E')
    Z = HashKey(-100, 'Z')
    Er = HashKey(103, 'Er', error_on_eq_to=D)
    h = hamt()
    h = h.set(A, 'a')
    h = h.set(B, 'b')
    h = h.set(C, 'c')
    h = h.set(D, 'd')
    h = h.set(E, 'e')
    orig_len = len(h)
    h = h.delete(C)
    self.assertEqual(len(h), orig_len - 1)
    with self.assertRaisesRegex(ValueError, 'cannot compare'):
        h.delete(Er)
    h = h.delete(D)
    self.assertEqual(len(h), orig_len - 2)
    h2 = h.delete(Z)
    self.assertIs(h2, h)
    h = h.delete(A)
    self.assertEqual(len(h), orig_len - 3)
    self.assertEqual(h.get(A, 42), 42)
    self.assertEqual(h.get(B), 'b')
    self.assertEqual(h.get(E), 'e')
