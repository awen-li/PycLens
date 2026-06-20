# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: StatAttributeTests_test_statvfs_result_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = os.statvfs(self.fname)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        p = pickle.dumps(result, proto)
        self.assertIn(b'statvfs_result', p)
        if proto < 4:
            self.assertIn(b'cos\nstatvfs_result\n', p)
        unpickled = pickle.loads(p)
        self.assertEqual(result, unpickled)
