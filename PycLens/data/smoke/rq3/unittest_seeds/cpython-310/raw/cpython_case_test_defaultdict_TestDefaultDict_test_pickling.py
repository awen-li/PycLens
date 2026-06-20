# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_defaultdict.py
# case: TestDefaultDict_test_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = defaultdict(int)
    d[1]
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        s = pickle.dumps(d, proto)
        o = pickle.loads(s)
        self.assertEqual(d, o)
