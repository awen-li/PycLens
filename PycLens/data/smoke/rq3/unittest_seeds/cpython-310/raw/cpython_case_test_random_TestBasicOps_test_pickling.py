# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        state = pickle.dumps(self.gen, proto)
        origseq = [self.gen.random() for i in range(10)]
        newgen = pickle.loads(state)
        restoredseq = [newgen.random() for i in range(10)]
        self.assertEqual(origseq, restoredseq)
