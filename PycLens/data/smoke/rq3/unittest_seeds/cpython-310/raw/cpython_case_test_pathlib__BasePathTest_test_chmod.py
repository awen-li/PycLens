# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_chmod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE) / 'fileA'
    mode = p.stat().st_mode
    new_mode = mode & ~146
    p.chmod(new_mode)
    self.assertEqual(p.stat().st_mode, new_mode)
    new_mode = mode | 146
    p.chmod(new_mode)
    self.assertEqual(p.stat().st_mode, new_mode)
