# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: PkgutilTests_test_walkpackages_filesys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pkg1 = 'test_walkpackages_filesys'
    pkg1_dir = os.path.join(self.dirname, pkg1)
    os.mkdir(pkg1_dir)
    f = open(os.path.join(pkg1_dir, '__init__.py'), 'wb')
    f.close()
    os.mkdir(os.path.join(pkg1_dir, 'sub'))
    f = open(os.path.join(pkg1_dir, 'sub', '__init__.py'), 'wb')
    f.close()
    f = open(os.path.join(pkg1_dir, 'sub', 'mod.py'), 'wb')
    f.close()
    pkg2 = 'sub'
    pkg2_dir = os.path.join(self.dirname, pkg2)
    os.mkdir(pkg2_dir)
    f = open(os.path.join(pkg2_dir, '__init__.py'), 'wb')
    f.close()
    os.mkdir(os.path.join(pkg2_dir, 'test_walkpackages_filesys'))
    f = open(os.path.join(pkg2_dir, 'test_walkpackages_filesys', '__init__.py'), 'wb')
    f.close()
    f = open(os.path.join(pkg2_dir, 'test_walkpackages_filesys', 'mod.py'), 'wb')
    f.close()
    expected = ['sub', 'sub.test_walkpackages_filesys', 'sub.test_walkpackages_filesys.mod', 'test_walkpackages_filesys', 'test_walkpackages_filesys.sub', 'test_walkpackages_filesys.sub.mod']
    actual = [e[1] for e in pkgutil.walk_packages([self.dirname])]
    self.assertEqual(actual, expected)
    for pkg in expected:
        if pkg.endswith('mod'):
            continue
        del sys.modules[pkg]
