# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: PkgutilTests_test_walkpackages_zipfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zip = 'test_walkpackages_zipfile.zip'
    pkg1 = 'test_walkpackages_zipfile'
    pkg2 = 'sub'
    zip_file = os.path.join(self.dirname, zip)
    z = zipfile.ZipFile(zip_file, 'w')
    z.writestr(pkg2 + '/__init__.py', '')
    z.writestr(pkg2 + '/' + pkg1 + '/__init__.py', '')
    z.writestr(pkg2 + '/' + pkg1 + '/mod.py', '')
    z.writestr(pkg1 + '/__init__.py', '')
    z.writestr(pkg1 + '/' + pkg2 + '/__init__.py', '')
    z.writestr(pkg1 + '/' + pkg2 + '/mod.py', '')
    z.close()
    sys.path.insert(0, zip_file)
    expected = ['sub', 'sub.test_walkpackages_zipfile', 'sub.test_walkpackages_zipfile.mod', 'test_walkpackages_zipfile', 'test_walkpackages_zipfile.sub', 'test_walkpackages_zipfile.sub.mod']
    actual = [e[1] for e in pkgutil.walk_packages([zip_file])]
    self.assertEqual(actual, expected)
    del sys.path[0]
    for pkg in expected:
        if pkg.endswith('mod'):
            continue
        del sys.modules[pkg]
