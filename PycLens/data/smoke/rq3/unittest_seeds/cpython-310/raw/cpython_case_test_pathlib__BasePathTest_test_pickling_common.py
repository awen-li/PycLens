# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_pickling_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE, 'fileA')
    for proto in range(0, pickle.HIGHEST_PROTOCOL + 1):
        dumped = pickle.dumps(p, proto)
        pp = pickle.loads(dumped)
        self.assertEqual(pp.stat(), p.stat())
