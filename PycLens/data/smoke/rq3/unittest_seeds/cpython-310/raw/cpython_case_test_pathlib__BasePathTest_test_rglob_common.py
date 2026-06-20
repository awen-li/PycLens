# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_rglob_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _check(glob, expected):
        self.assertEqual(set(glob), {P(BASE, q) for q in expected})
    P = self.cls
    p = P(BASE)
    it = p.rglob('fileA')
    self.assertIsInstance(it, collections.abc.Iterator)
    _check(it, ['fileA'])
    _check(p.rglob('fileB'), ['dirB/fileB'])
    _check(p.rglob('*/fileA'), [])
    if not os_helper.can_symlink():
        _check(p.rglob('*/fileB'), ['dirB/fileB'])
    else:
        _check(p.rglob('*/fileB'), ['dirB/fileB', 'dirB/linkD/fileB', 'linkB/fileB', 'dirA/linkC/fileB'])
    _check(p.rglob('file*'), ['fileA', 'dirB/fileB', 'dirC/fileC', 'dirC/dirD/fileD'])
    p = P(BASE, 'dirC')
    _check(p.rglob('file*'), ['dirC/fileC', 'dirC/dirD/fileD'])
    _check(p.rglob('*/*'), ['dirC/dirD/fileD'])
