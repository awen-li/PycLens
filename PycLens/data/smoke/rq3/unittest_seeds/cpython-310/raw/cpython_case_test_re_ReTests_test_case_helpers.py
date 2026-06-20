# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_case_helpers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _sre
    for i in range(128):
        c = chr(i)
        lo = ord(c.lower())
        self.assertEqual(_sre.ascii_tolower(i), lo)
        self.assertEqual(_sre.unicode_tolower(i), lo)
        iscased = c in string.ascii_letters
        self.assertEqual(_sre.ascii_iscased(i), iscased)
        self.assertEqual(_sre.unicode_iscased(i), iscased)
    for i in list(range(128, 4096)) + [66560, 66600]:
        c = chr(i)
        self.assertEqual(_sre.ascii_tolower(i), i)
        if i != 304:
            self.assertEqual(_sre.unicode_tolower(i), ord(c.lower()))
        iscased = c != c.lower() or c != c.upper()
        self.assertFalse(_sre.ascii_iscased(i))
        self.assertEqual(_sre.unicode_iscased(i), c != c.lower() or c != c.upper())
    self.assertEqual(_sre.ascii_tolower(304), 304)
    self.assertEqual(_sre.unicode_tolower(304), ord('i'))
    self.assertFalse(_sre.ascii_iscased(304))
    self.assertTrue(_sre.unicode_iscased(304))
