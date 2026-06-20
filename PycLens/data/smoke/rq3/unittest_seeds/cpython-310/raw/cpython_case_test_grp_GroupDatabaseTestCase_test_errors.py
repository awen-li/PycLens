# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grp.py
# case: GroupDatabaseTestCase_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, grp.getgrgid)
    self.assertRaises(TypeError, grp.getgrgid, 3.14)
    self.assertRaises(TypeError, grp.getgrnam)
    self.assertRaises(TypeError, grp.getgrnam, 42)
    self.assertRaises(TypeError, grp.getgrall, 42)
    self.assertRaisesRegex(ValueError, 'null', grp.getgrnam, 'a\x00b')
    bynames = {}
    bygids = {}
    for (n, p, g, mem) in grp.getgrall():
        if not n or n == '+':
            continue
        bynames[n] = g
        bygids[g] = n
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
    self.assertRaises(KeyError, grp.getgrnam, fakename)
    fakegid = 4127
    while fakegid in bygids:
        fakegid = fakegid * 3 % 65536
    self.assertRaises(KeyError, grp.getgrgid, fakegid)
