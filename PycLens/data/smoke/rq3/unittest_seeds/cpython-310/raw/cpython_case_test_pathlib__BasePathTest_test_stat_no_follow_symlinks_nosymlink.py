# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_stat_no_follow_symlinks_nosymlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE) / 'fileA'
    st = p.stat()
    self.assertEqual(st, p.stat(follow_symlinks=False))
