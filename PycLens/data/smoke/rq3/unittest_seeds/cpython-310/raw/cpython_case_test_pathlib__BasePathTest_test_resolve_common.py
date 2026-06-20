# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_resolve_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P(BASE, 'foo')
    with self.assertRaises(OSError) as cm:
        p.resolve(strict=True)
    self.assertEqual(cm.exception.errno, errno.ENOENT)
    self.assertEqualNormCase(str(p.resolve(strict=False)), os.path.join(BASE, 'foo'))
    p = P(BASE, 'foo', 'in', 'spam')
    self.assertEqualNormCase(str(p.resolve(strict=False)), os.path.join(BASE, 'foo', 'in', 'spam'))
    p = P(BASE, '..', 'foo', 'in', 'spam')
    self.assertEqualNormCase(str(p.resolve(strict=False)), os.path.abspath(os.path.join('foo', 'in', 'spam')))
    p = P(BASE, 'dirB', 'fileB')
    self._check_resolve_relative(p, p)
    p = P(BASE, 'linkA')
    self._check_resolve_relative(p, P(BASE, 'fileA'))
    p = P(BASE, 'dirA', 'linkC', 'fileB')
    self._check_resolve_relative(p, P(BASE, 'dirB', 'fileB'))
    p = P(BASE, 'dirB', 'linkD', 'fileB')
    self._check_resolve_relative(p, P(BASE, 'dirB', 'fileB'))
    p = P(BASE, 'dirA', 'linkC', 'fileB', 'foo', 'in', 'spam')
    self._check_resolve_relative(p, P(BASE, 'dirB', 'fileB', 'foo', 'in', 'spam'), False)
    p = P(BASE, 'dirA', 'linkC', '..', 'foo', 'in', 'spam')
    if os.name == 'nt':
        self._check_resolve_relative(p, P(BASE, 'dirA', 'foo', 'in', 'spam'), False)
    else:
        self._check_resolve_relative(p, P(BASE, 'foo', 'in', 'spam'), False)
    d = os_helper._longpath(tempfile.mkdtemp(suffix='-dirD', dir=os.getcwd()))
    self.addCleanup(os_helper.rmtree, d)
    os.symlink(os.path.join(d), join('dirA', 'linkX'))
    os.symlink(join('dirB'), os.path.join(d, 'linkY'))
    p = P(BASE, 'dirA', 'linkX', 'linkY', 'fileB')
    self._check_resolve_absolute(p, P(BASE, 'dirB', 'fileB'))
    p = P(BASE, 'dirA', 'linkX', 'linkY', 'foo', 'in', 'spam')
    self._check_resolve_relative(p, P(BASE, 'dirB', 'foo', 'in', 'spam'), False)
    p = P(BASE, 'dirA', 'linkX', 'linkY', '..', 'foo', 'in', 'spam')
    if os.name == 'nt':
        self._check_resolve_relative(p, P(d, 'foo', 'in', 'spam'), False)
    else:
        self._check_resolve_relative(p, P(BASE, 'foo', 'in', 'spam'), False)
