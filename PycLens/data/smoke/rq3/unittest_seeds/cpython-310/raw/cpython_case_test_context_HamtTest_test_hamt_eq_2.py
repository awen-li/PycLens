# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: HamtTest_test_hamt_eq_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    A = HashKey(100, 'A')
    Er = HashKey(100, 'Er', error_on_eq_to=A)
    h1 = hamt()
    h1 = h1.set(A, 'a')
    h2 = hamt()
    h2 = h2.set(Er, 'a')
    with self.assertRaisesRegex(ValueError, 'cannot compare'):
        h1 == h2
    with self.assertRaisesRegex(ValueError, 'cannot compare'):
        h1 != h2
