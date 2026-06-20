# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pwd.py
# case: PwdTest_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, pwd.getpwuid)
    self.assertRaises(TypeError, pwd.getpwuid, 3.14)
    self.assertRaises(TypeError, pwd.getpwnam)
    self.assertRaises(TypeError, pwd.getpwnam, 42)
    self.assertRaises(TypeError, pwd.getpwall, 42)
    self.assertRaisesRegex(ValueError, 'null', pwd.getpwnam, 'a\x00b')
    bynames = {}
    byuids = {}
    for (n, p, u, g, gecos, d, s) in pwd.getpwall():
        bynames[n] = u
        byuids[u] = n
    allnames = list(bynames.keys())
    namei = 0
    fakename = allnames[namei]
    while fakename in bynames:
        chars = list(fakename)
        for i in range(len(chars)):
            if chars[i] == 'z':
                chars[i] = 'A'
                break
            elif chars[i] == 'Z':
                continue
            else:
                chars[i] = chr(ord(chars[i]) + 1)
                break
        else:
            namei = namei + 1
            try:
                fakename = allnames[namei]
            except IndexError:
                break
        fakename = ''.join(chars)
    self.assertRaises(KeyError, pwd.getpwnam, fakename)
    fakeuid = sys.maxsize
    self.assertNotIn(fakeuid, byuids)
    self.assertRaises(KeyError, pwd.getpwuid, fakeuid)
    self.assertRaises(KeyError, pwd.getpwuid, -1)
    self.assertRaises(KeyError, pwd.getpwuid, 2 ** 128)
    self.assertRaises(KeyError, pwd.getpwuid, -2 ** 128)
