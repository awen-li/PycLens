# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_commonpath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(paths, expected):
        tester(('ntpath.commonpath(%r)' % paths).replace('\\\\', '\\'), expected)

    def check_error(exc, paths):
        self.assertRaises(exc, ntpath.commonpath, paths)
        self.assertRaises(exc, ntpath.commonpath, [os.fsencode(p) for p in paths])
    self.assertRaises(ValueError, ntpath.commonpath, [])
    check_error(ValueError, ['C:\\Program Files', 'Program Files'])
    check_error(ValueError, ['C:\\Program Files', 'C:Program Files'])
    check_error(ValueError, ['\\Program Files', 'Program Files'])
    check_error(ValueError, ['Program Files', 'C:\\Program Files'])
    check(['C:\\Program Files'], 'C:\\Program Files')
    check(['C:\\Program Files', 'C:\\Program Files'], 'C:\\Program Files')
    check(['C:\\Program Files\\', 'C:\\Program Files'], 'C:\\Program Files')
    check(['C:\\Program Files\\', 'C:\\Program Files\\'], 'C:\\Program Files')
    check(['C:\\\\Program Files', 'C:\\Program Files\\\\'], 'C:\\Program Files')
    check(['C:\\.\\Program Files', 'C:\\Program Files\\.'], 'C:\\Program Files')
    check(['C:\\', 'C:\\bin'], 'C:\\')
    check(['C:\\Program Files', 'C:\\bin'], 'C:\\')
    check(['C:\\Program Files', 'C:\\Program Files\\Bar'], 'C:\\Program Files')
    check(['C:\\Program Files\\Foo', 'C:\\Program Files\\Bar'], 'C:\\Program Files')
    check(['C:\\Program Files', 'C:\\Projects'], 'C:\\')
    check(['C:\\Program Files\\', 'C:\\Projects'], 'C:\\')
    check(['C:\\Program Files\\Foo', 'C:/Program Files/Bar'], 'C:\\Program Files')
    check(['C:\\Program Files\\Foo', 'c:/program files/bar'], 'C:\\Program Files')
    check(['c:/program files/bar', 'C:\\Program Files\\Foo'], 'c:\\program files')
    check_error(ValueError, ['C:\\Program Files', 'D:\\Program Files'])
    check(['spam'], 'spam')
    check(['spam', 'spam'], 'spam')
    check(['spam', 'alot'], '')
    check(['and\\jam', 'and\\spam'], 'and')
    check(['and\\\\jam', 'and\\spam\\\\'], 'and')
    check(['and\\.\\jam', '.\\and\\spam'], 'and')
    check(['and\\jam', 'and\\spam', 'alot'], '')
    check(['and\\jam', 'and\\spam', 'and'], 'and')
    check(['C:and\\jam', 'C:and\\spam'], 'C:and')
    check([''], '')
    check(['', 'spam\\alot'], '')
    check_error(ValueError, ['', '\\spam\\alot'])
    self.assertRaises(TypeError, ntpath.commonpath, [b'C:\\Program Files', 'C:\\Program Files\\Foo'])
    self.assertRaises(TypeError, ntpath.commonpath, [b'C:\\Program Files', 'Program Files\\Foo'])
    self.assertRaises(TypeError, ntpath.commonpath, [b'Program Files', 'C:\\Program Files\\Foo'])
    self.assertRaises(TypeError, ntpath.commonpath, ['C:\\Program Files', b'C:\\Program Files\\Foo'])
    self.assertRaises(TypeError, ntpath.commonpath, ['C:\\Program Files', b'Program Files\\Foo'])
    self.assertRaises(TypeError, ntpath.commonpath, ['Program Files', b'C:\\Program Files\\Foo'])
