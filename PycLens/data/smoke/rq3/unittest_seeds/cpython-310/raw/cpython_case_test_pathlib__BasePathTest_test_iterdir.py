# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_iterdir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P(BASE)
    it = p.iterdir()
    paths = set(it)
    expected = ['dirA', 'dirB', 'dirC', 'dirE', 'fileA']
    if os_helper.can_symlink():
        expected += ['linkA', 'linkB', 'brokenLink', 'brokenLinkLoop']
    self.assertEqual(paths, {P(BASE, q) for q in expected})
