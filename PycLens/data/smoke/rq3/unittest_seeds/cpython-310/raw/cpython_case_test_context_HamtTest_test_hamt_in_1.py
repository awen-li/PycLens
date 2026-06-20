# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: HamtTest_test_hamt_in_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    A = HashKey(100, 'A')
    AA = HashKey(100, 'A')
    B = HashKey(101, 'B')
    h = hamt()
    h = h.set(A, 1)
    self.assertTrue(A in h)
    self.assertFalse(B in h)
    with self.assertRaises(EqError):
        with HaskKeyCrasher(error_on_eq=True):
            AA in h
    with self.assertRaises(HashingError):
        with HaskKeyCrasher(error_on_hash=True):
            AA in h
