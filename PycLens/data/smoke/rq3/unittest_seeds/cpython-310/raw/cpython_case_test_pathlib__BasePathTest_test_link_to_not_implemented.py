# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_link_to_not_implemented

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    p = P / 'fileA'
    q = P / 'dirA' / 'fileAA'
    with self.assertRaises(NotImplementedError):
        p.link_to(q)
