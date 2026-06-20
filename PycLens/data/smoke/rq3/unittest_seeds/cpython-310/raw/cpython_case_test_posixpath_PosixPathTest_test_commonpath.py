# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_commonpath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(paths, expected):
        self.assertEqual(posixpath.commonpath(paths), expected)
        self.assertEqual(posixpath.commonpath([os.fsencode(p) for p in paths]), os.fsencode(expected))

    def check_error(exc, paths):
        self.assertRaises(exc, posixpath.commonpath, paths)
        self.assertRaises(exc, posixpath.commonpath, [os.fsencode(p) for p in paths])
    self.assertRaises(ValueError, posixpath.commonpath, [])
    check_error(ValueError, ['/usr', 'usr'])
    check_error(ValueError, ['usr', '/usr'])
    check(['/usr/local'], '/usr/local')
    check(['/usr/local', '/usr/local'], '/usr/local')
    check(['/usr/local/', '/usr/local'], '/usr/local')
    check(['/usr/local/', '/usr/local/'], '/usr/local')
    check(['/usr//local', '//usr/local'], '/usr/local')
    check(['/usr/./local', '/./usr/local'], '/usr/local')
    check(['/', '/dev'], '/')
    check(['/usr', '/dev'], '/')
    check(['/usr/lib/', '/usr/lib/python3'], '/usr/lib')
    check(['/usr/lib/', '/usr/lib64/'], '/usr')
    check(['/usr/lib', '/usr/lib64'], '/usr')
    check(['/usr/lib/', '/usr/lib64'], '/usr')
    check(['spam'], 'spam')
    check(['spam', 'spam'], 'spam')
    check(['spam', 'alot'], '')
    check(['and/jam', 'and/spam'], 'and')
    check(['and//jam', 'and/spam//'], 'and')
    check(['and/./jam', './and/spam'], 'and')
    check(['and/jam', 'and/spam', 'alot'], '')
    check(['and/jam', 'and/spam', 'and'], 'and')
    check([''], '')
    check(['', 'spam/alot'], '')
    check_error(ValueError, ['', '/spam/alot'])
    self.assertRaises(TypeError, posixpath.commonpath, [b'/usr/lib/', '/usr/lib/python3'])
    self.assertRaises(TypeError, posixpath.commonpath, [b'/usr/lib/', 'usr/lib/python3'])
    self.assertRaises(TypeError, posixpath.commonpath, [b'usr/lib/', '/usr/lib/python3'])
    self.assertRaises(TypeError, posixpath.commonpath, ['/usr/lib/', b'/usr/lib/python3'])
    self.assertRaises(TypeError, posixpath.commonpath, ['/usr/lib/', b'usr/lib/python3'])
    self.assertRaises(TypeError, posixpath.commonpath, ['usr/lib/', b'/usr/lib/python3'])
