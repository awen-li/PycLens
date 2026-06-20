# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pickletools.py
# case: OptimizedPickleTests_test_optimize_binput_and_memoize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pickled = b'\x80\x04\x95\x15\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x04spamq\x01\x8c\x03ham\x94h\x02e.'
    self.assertIn(pickle.BINPUT, pickled)
    unpickled = pickle.loads(pickled)
    self.assertEqual(unpickled, ['spam', 'ham', 'ham'])
    self.assertIs(unpickled[1], unpickled[2])
    pickled2 = pickletools.optimize(pickled)
    unpickled2 = pickle.loads(pickled2)
    self.assertEqual(unpickled2, ['spam', 'ham', 'ham'])
    self.assertIs(unpickled2[1], unpickled2[2])
    self.assertNotIn(pickle.BINPUT, pickled2)
