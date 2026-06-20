# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: PkgutilTests_test_getdata_filesys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pkg = 'test_getdata_filesys'
    RESOURCE_DATA = b'Hello, world!\nSecond line\r\nThird line'
    package_dir = os.path.join(self.dirname, pkg)
    os.mkdir(package_dir)
    f = open(os.path.join(package_dir, '__init__.py'), 'wb')
    f.close()
    f = open(os.path.join(package_dir, 'res.txt'), 'wb')
    f.write(RESOURCE_DATA)
    f.close()
    os.mkdir(os.path.join(package_dir, 'sub'))
    f = open(os.path.join(package_dir, 'sub', 'res.txt'), 'wb')
    f.write(RESOURCE_DATA)
    f.close()
    res1 = pkgutil.get_data(pkg, 'res.txt')
    self.assertEqual(res1, RESOURCE_DATA)
    res2 = pkgutil.get_data(pkg, 'sub/res.txt')
    self.assertEqual(res2, RESOURCE_DATA)
    del sys.modules[pkg]
