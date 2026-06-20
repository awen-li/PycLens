# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_stat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE) / 'fileA'
    st = p.stat()
    self.assertEqual(p.stat(), st)
    p.chmod(st.st_mode ^ 146)
    self.addCleanup(p.chmod, st.st_mode)
    self.assertNotEqual(p.stat(), st)
