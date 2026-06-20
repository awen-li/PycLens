# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pickletools.py
# case: OptimizedPickleTests_test_optimize_long_binget

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [str(i) for i in range(257)]
    data.append(data[-1])
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        pickled = pickle.dumps(data, proto)
        unpickled = pickle.loads(pickled)
        self.assertEqual(unpickled, data)
        self.assertIs(unpickled[-1], unpickled[-2])
        pickled2 = pickletools.optimize(pickled)
        unpickled2 = pickle.loads(pickled2)
        self.assertEqual(unpickled2, data)
        self.assertIs(unpickled2[-1], unpickled2[-2])
        self.assertNotIn(pickle.LONG_BINGET, pickled2)
        self.assertNotIn(pickle.LONG_BINPUT, pickled2)
