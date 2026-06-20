# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: PkgutilTests_test_getdata_zipfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zip = 'test_getdata_zipfile.zip'
    pkg = 'test_getdata_zipfile'
    RESOURCE_DATA = b'Hello, world!\nSecond line\r\nThird line'
    zip_file = os.path.join(self.dirname, zip)
    z = zipfile.ZipFile(zip_file, 'w')
    z.writestr(pkg + '/__init__.py', '')
    z.writestr(pkg + '/res.txt', RESOURCE_DATA)
    z.writestr(pkg + '/sub/res.txt', RESOURCE_DATA)
    z.close()
    sys.path.insert(0, zip_file)
    res1 = pkgutil.get_data(pkg, 'res.txt')
    self.assertEqual(res1, RESOURCE_DATA)
    res2 = pkgutil.get_data(pkg, 'sub/res.txt')
    self.assertEqual(res2, RESOURCE_DATA)
    names = []
    for moduleinfo in pkgutil.iter_modules([zip_file]):
        self.assertIsInstance(moduleinfo, pkgutil.ModuleInfo)
        names.append(moduleinfo.name)
    self.assertEqual(names, ['test_getdata_zipfile'])
    del sys.path[0]
    del sys.modules[pkg]
