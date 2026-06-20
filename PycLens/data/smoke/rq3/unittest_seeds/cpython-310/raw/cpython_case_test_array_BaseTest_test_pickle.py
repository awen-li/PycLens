# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
        a = array.array(self.typecode, self.example)
        b = pickle.loads(pickle.dumps(a, protocol))
        self.assertNotEqual(id(a), id(b))
        self.assertEqual(a, b)
        a = ArraySubclass(self.typecode, self.example)
        a.x = 10
        b = pickle.loads(pickle.dumps(a, protocol))
        self.assertNotEqual(id(a), id(b))
        self.assertEqual(a, b)
        self.assertEqual(a.x, b.x)
        self.assertEqual(type(a), type(b))
