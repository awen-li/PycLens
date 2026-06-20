# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: HamtTest_test_hamt_getitem_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    A = HashKey(100, 'A')
    AA = HashKey(100, 'A')
    B = HashKey(101, 'B')
    h = hamt()
    h = h.set(A, 1)
    self.assertEqual(h[A], 1)
    self.assertEqual(h[AA], 1)
    with self.assertRaises(KeyError):
        h[B]
    with self.assertRaises(EqError):
        with HaskKeyCrasher(error_on_eq=True):
            h[AA]
    with self.assertRaises(HashingError):
        with HaskKeyCrasher(error_on_hash=True):
            h[AA]
