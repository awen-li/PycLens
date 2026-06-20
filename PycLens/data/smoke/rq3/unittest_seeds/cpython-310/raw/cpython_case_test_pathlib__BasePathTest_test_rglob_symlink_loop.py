# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_rglob_symlink_loop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P(BASE)
    given = set(p.rglob('*'))
    expect = {'brokenLink', 'dirA', 'dirA/linkC', 'dirB', 'dirB/fileB', 'dirB/linkD', 'dirC', 'dirC/dirD', 'dirC/dirD/fileD', 'dirC/fileC', 'dirE', 'fileA', 'linkA', 'linkB', 'brokenLinkLoop'}
    self.assertEqual(given, {p / x for x in expect})
