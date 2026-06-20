# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(pickle.HIGHEST_PROTOCOL + 1):
        p = pickle.dumps(self.s, i)
        dup = pickle.loads(p)
        self.assertEqual(self.s, dup, '%s != %s' % (self.s, dup))
        if type(self.s) not in (set, frozenset):
            self.s.x = 10
            p = pickle.dumps(self.s, i)
            dup = pickle.loads(p)
            self.assertEqual(self.s.x, dup.x)
