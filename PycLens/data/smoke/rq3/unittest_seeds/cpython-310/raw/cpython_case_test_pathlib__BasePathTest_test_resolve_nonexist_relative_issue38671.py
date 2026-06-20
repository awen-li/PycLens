# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_resolve_nonexist_relative_issue38671

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls('non', 'exist')
    old_cwd = os.getcwd()
    os.chdir(BASE)
    try:
        self.assertEqual(p.resolve(), self.cls(BASE, p))
    finally:
        os.chdir(old_cwd)
