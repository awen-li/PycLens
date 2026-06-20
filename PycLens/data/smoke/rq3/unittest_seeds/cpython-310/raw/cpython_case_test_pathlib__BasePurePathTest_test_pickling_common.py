# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_pickling_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P('/a/b')
    for proto in range(0, pickle.HIGHEST_PROTOCOL + 1):
        dumped = pickle.dumps(p, proto)
        pp = pickle.loads(dumped)
        self.assertIs(pp.__class__, p.__class__)
        self.assertEqual(pp, p)
        self.assertEqual(hash(pp), hash(p))
        self.assertEqual(str(pp), str(p))
