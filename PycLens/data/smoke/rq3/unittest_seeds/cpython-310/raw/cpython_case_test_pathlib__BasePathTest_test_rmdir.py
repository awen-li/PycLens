# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_rmdir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE) / 'dirA'
    for q in p.iterdir():
        q.unlink()
    p.rmdir()
    self.assertFileNotFound(p.stat)
    self.assertFileNotFound(p.unlink)
