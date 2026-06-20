# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestVec2D_test_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    vec = Vec2D(0.5, 2)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.subTest(proto=proto):
            pickled = pickle.dumps(vec, protocol=proto)
            unpickled = pickle.loads(pickled)
            self.assertEqual(unpickled, vec)
            self.assertIsInstance(unpickled, Vec2D)
