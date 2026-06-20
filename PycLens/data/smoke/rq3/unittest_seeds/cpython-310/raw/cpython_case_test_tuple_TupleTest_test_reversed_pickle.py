# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tuple.py
# case: TupleTest_test_reversed_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = self.type2test([4, 5, 6, 7])
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        itorg = reversed(data)
        d = pickle.dumps(itorg, proto)
        it = pickle.loads(d)
        self.assertEqual(type(itorg), type(it))
        self.assertEqual(self.type2test(it), self.type2test(reversed(data)))
        it = pickle.loads(d)
        next(it)
        d = pickle.dumps(it, proto)
        self.assertEqual(self.type2test(it), self.type2test(reversed(data))[1:])
