# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_parts_interning

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P('/usr/bin/foo')
    q = P('/usr/local/bin')
    self.assertIs(p.parts[1], q.parts[1])
    self.assertIs(p.parts[2], q.parts[3])
