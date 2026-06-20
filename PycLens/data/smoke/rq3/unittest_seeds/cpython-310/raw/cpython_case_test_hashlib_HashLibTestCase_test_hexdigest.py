# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_hexdigest

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for cons in self.hash_constructors:
        h = cons(usedforsecurity=False)
        if h.name in self.shakes:
            self.assertIsInstance(h.digest(16), bytes)
            self.assertEqual(hexstr(h.digest(16)), h.hexdigest(16))
        else:
            self.assertIsInstance(h.digest(), bytes)
            self.assertEqual(hexstr(h.digest()), h.hexdigest())
