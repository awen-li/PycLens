# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_link_to

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    p = P / 'fileA'
    size = p.stat().st_size
    q = P / 'dirA' / 'fileAA'
    try:
        with self.assertWarns(DeprecationWarning):
            p.link_to(q)
    except PermissionError as e:
        self.skipTest('os.link(): %s' % e)
    self.assertEqual(q.stat().st_size, size)
    self.assertEqual(os.path.samefile(p, q), True)
    self.assertTrue(p.stat)
    r = rel_join('fileAAA')
    with self.assertWarns(DeprecationWarning):
        q.link_to(r)
    self.assertEqual(os.stat(r).st_size, size)
    self.assertTrue(q.stat)
