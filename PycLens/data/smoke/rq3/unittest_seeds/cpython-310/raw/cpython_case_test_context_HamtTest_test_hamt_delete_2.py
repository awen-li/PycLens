# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: HamtTest_test_hamt_delete_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    A = HashKey(100, 'A')
    B = HashKey(201001, 'B')
    C = HashKey(101001, 'C')
    D = HashKey(103, 'D')
    E = HashKey(104, 'E')
    Z = HashKey(-100, 'Z')
    Er = HashKey(201001, 'Er', error_on_eq_to=B)
    h = hamt()
    h = h.set(A, 'a')
    h = h.set(B, 'b')
    h = h.set(C, 'c')
    h = h.set(D, 'd')
    h = h.set(E, 'e')
    orig_len = len(h)
    with self.assertRaisesRegex(ValueError, 'cannot compare'):
        h.delete(Er)
    h = h.delete(Z)
    self.assertEqual(len(h), orig_len)
    h = h.delete(C)
    self.assertEqual(len(h), orig_len - 1)
    h = h.delete(B)
    self.assertEqual(len(h), orig_len - 2)
    h = h.delete(A)
    self.assertEqual(len(h), orig_len - 3)
    self.assertEqual(h.get(D), 'd')
    self.assertEqual(h.get(E), 'e')
    h = h.delete(A)
    h = h.delete(B)
    h = h.delete(D)
    h = h.delete(E)
    self.assertEqual(len(h), 0)
